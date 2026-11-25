"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so sánh hai tỉ lệ (Nhiệm vụ D1)."""
    from statistics import NormalDist
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil(
        (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
        / (p2 - p1) ** 2
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()

    print('\n--- A2 · Mô hình chi phí từ trace ---')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        fmt = f'{gia_tri:>14,.1f}' if ten == 'hoa_don_moi_yc' else f'{gia_tri:>14,.0f}'
        print(f'{ten:16s} {fmt}')
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong_yc = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'he_thong/yc      {he_thong_yc:>14,.0f} đ ({he_thong_yc / BASELINE:.2f}x của 12.000 đ) [simulated]')

    print('\n--- A3 · Tách theo loại yêu cầu ---')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        ti_le_tc = kq['thanh_cong'] / len(sub) * 100
        lan_chay_yc = sub['so_lan_chay'].mean()
        print(f'{loai:10s} n={len(sub):3d} tc={ti_le_tc:5.1f}% lan={lan_chay_yc:.2f} cps={kq["cps"]:>7,.0f} đ ({kq["cps"] / BASELINE:.2f}x) [simulated]')

    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    runs_loai['is_ok'] = (runs_loai['status'] == 'ok').astype(int)
    print('\nTỉ lệ ok theo attempt:')
    print((runs_loai.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100).round(1))

    print('\n--- A4 · Chi phí cố định (noi_dia + hang_nang) ---')
    pilot_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pilot = mo_hinh(runs, pilot_reqs)
    ti_le_pilot = kq_pilot['thanh_cong'] / len(reqs)
    for nhan, khoi_luong in [('45.000/tháng', 45000), ('22.500/tháng', 22500)]:
        viec_tc_thang = khoi_luong * ti_le_pilot
        co_dinh_viec = 40_000_000 / viec_tc_thang
        tong_viec = kq_pilot['cps'] + co_dinh_viec
        print(f'{nhan:14s} tc/tháng={viec_tc_thang:>7,.0f} cố_định={co_dinh_viec:>5,.0f} tổng={tong_viec:>5,.0f} đ ({tong_viec / BASELINE:.2f}x) [simulated]')

    # print('\n--- B1 · Bảng độ nhạy ---')
    # kich_ban = {
    #     'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
    #     'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
    #     'Xem lại gấp đôi': dict(he_so_xem_lai=2),
    #     'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
    #     'Làm lại gấp đôi': dict(he_so_lam_lai=2),
    #     'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
    #     'Lương tăng 25%': dict(luong_phut=2500),
    #     'Tối đa 2 lần chạy': dict(max_lan_chay=2),
    #     'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    # }
    # goc = ket_qua['cps']
    # for ten, kw in kich_ban.items():
    #     cps = mo_hinh(runs, reqs, **kw)['cps']
    #     print(f'{ten:25s} {cps:8,.0f} đ {(cps / goc - 1) * 100:+6.1f}% [simulated]')

    # print('\n--- B2 · Đổi một cặp ---')
    # cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    # print(f'Token 2x + Xem lại 2x:    {cps_cap:8,.0f} đ {(cps_cap / goc - 1) * 100:+6.1f}% [simulated]')

    # print('\n--- B3 · Giới hạn chạy lại ---')
    # for gio_han in [1, 2, 3]:
    #     kq_gh = mo_hinh(runs, reqs, max_lan_chay=gio_han)
    #     khong_tc_gh = len(reqs) - kq_gh['thanh_cong']
    #     he_thong_gh = kq_gh['tong'] + khong_tc_gh * BASELINE
    #     print(f'{gio_han} lần: trợ_lý={kq_gh["tong"]:>10,.0f} đ không_tc={khong_tc_gh:3d} cả_hệ_thống={he_thong_gh:>10,.0f} đ cps={kq_gh["cps"]:>5,.0f} đ [simulated]')

    # print('\n--- B4 · Xem lại 100% (noi_dia + hang_nang) ---')
    # pilot_runs = runs[runs['request_id'].isin(pilot_reqs['request_id'])]
    # ok_ids = set(pilot_runs[pilot_runs['status'] == 'ok']['request_id'])
    # so_xem_lai_100 = pilot_reqs['request_id'].isin(ok_ids).sum()
    # so_lam_lai = (pilot_reqs['ket_qua'] == 'lam_lai').sum()
    # hoa_don_pilot = kq_pilot['token'] + kq_pilot['tool']
    # tb_lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    # for phut_ll in [9.0, tb_lam_lai]:
    #     tong_100 = hoa_don_pilot + so_xem_lai_100 * 5 * LUONG_PHUT + so_lam_lai * phut_ll * LUONG_PHUT
    #     cps_100 = tong_100 / kq_pilot['thanh_cong']
    #     print(f'làm_lại={phut_ll:4.1f}p: tổng={tong_100:>10,.0f} đ cps={cps_100:>6,.0f} đ ({cps_100 / BASELINE:.2f}x) [simulated]')

    # print('\n--- D · Cỡ mẫu & mở lại ---')
    # print(f'co_mau(0.70, 0.75) = {co_mau(0.70, 0.75)} | co_mau(0.70, 0.76) = {co_mau(0.70, 0.76)}')
    # print(f'mo_lai_trong_7_ngay (toàn bộ) = {reqs["mo_lai_trong_7_ngay"].mean() * 100:.2f}%')
    # print(f'mo_lai_trong_7_ngay (pilot)   = {pilot_reqs["mo_lai_trong_7_ngay"].mean() * 100:.2f}%')
