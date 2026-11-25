"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from pathlib import Path
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# Ba hàm dùng giả định các lần chạy độc lập với xác suất p không đổi.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1 or (k is not None and (not isinstance(k, int) or k < 1)):
        raise ValueError('Cần 0 < p <= 1 và k nguyên dương hoặc None')
    return 1 / p if k is None else -math.expm1(k * math.log1p(-p)) / p if p < 1 else 1.0


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    expected = so_lan_chay_ky_vong(p, k)
    return 1.0 if k is None else p * expected


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT (1.20, 1.25, 1.25)')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# Mô hình dùng lại cho phân tích độ nhạy và giới hạn lần chạy.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs.request_id.isin(reqs.request_id)]
    if max_lan_chay is not None:
        if not isinstance(max_lan_chay, int) or max_lan_chay < 1:
            raise ValueError('Giới hạn chạy phải là số nguyên dương')
        runs = runs[runs.attempt <= max_lan_chay]
        vuot = reqs.so_lan_chay > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    token = runs.tokens_in / 1000 * gia_vao + runs.tokens_out / 1000 * gia_ra
    tool = runs.tool_calls * gia_tool
    xem_lai = reqs.phut_xem_lai_simulated.sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs.phut_lam_lai_simulated.sum() * luong_phut * he_so_lam_lai
    tong = token.sum() + tool.sum() + xem_lai + lam_lai
    thanh_cong = int(reqs.ket_qua.eq('thanh_cong').sum())
    return dict(token=float(token.sum()), tool=float(tool.sum()),
                chay_lai=float((token + tool)[runs.attempt > 1].sum()),
                xem_lai=float(xem_lai), lam_lai=float(lam_lai), tong=float(tong),
                thanh_cong=thanh_cong, cps=float(tong / thanh_cong) if thanh_cong else math.inf,
                hoa_don_moi_yc=float((token.sum() + tool.sum()) / len(reqs)) if len(reqs) else math.nan)


def bao_cao_a(runs, reqs):
    """In bảng A1–A4; mọi chi phí có phút nhân viên mang nhãn simulated."""
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print('\nA2 · Chi phí (tổng, xem lại, làm lại, cps: simulated)')
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:20s} {gia_tri:14,.2f}')
    print(f"CPS / hóa đơn mỗi yêu cầu: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.2f} lần (simulated)")
    print('\nA3 · Loại | số yêu cầu | thành công | lần chạy/yc | cps simulated | /12.000')
    for loai, nhom in reqs.groupby('loai', sort=False):
        m = mo_hinh(runs, nhom)
        print(f"{loai} | {len(nhom)} | {m['thanh_cong']/len(nhom):.2%} | "
              f"{nhom.so_lan_chay.mean():.2f} | {m['cps']:,.2f} | {m['cps']/BASELINE:.3f}")
    ok = runs.assign(ok=runs.status.eq('ok')).merge(reqs[['request_id', 'loai']], on='request_id')
    print('Tỉ lệ ok theo loại và attempt:')
    print(ok.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').to_string())
    scope = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    m = mo_hinh(runs, scope)
    print('\nA4 · Khối lượng tổng/tháng | thành công trong phạm vi | cố định/việc | cps + cố định simulated')
    for volume in (45000, 22500):
        success = volume * m['thanh_cong'] / len(reqs)
        fixed = 40000000 / success
        print(f"{volume} | {success:,.0f} | {fixed:,.2f} | {m['cps']+fixed:,.2f}")


if __name__ == '__main__':
    data = Path(__file__).resolve().parent
    runs = pd.read_csv(data / 'logix_runs.csv', keep_default_na=False)
    reqs = pd.read_csv(data / 'logix_requests.csv', keep_default_na=False)
    bao_cao_a(runs, reqs)
