# Báo cáo cá nhân — Vũ Quang Minh — 2A202603729

## 1. Thông tin thành viên

- Họ tên: Vũ Quang Minh.
- MSSV: 2A202603729.
- Email: chưa xác nhận trong phiên làm việc.
- GitHub: minh240804.
- Vai trò: Thành viên #2; người kiểm số (A1–A4, B1–B4); nhận bàn giao viết code `src/lab13.py` sau giải lao (D1, E1).

## 2. Phần việc phụ trách

| Giai đoạn theo phân công | Công việc | Sản phẩm / bằng chứng |
| --- | --- | --- |
| GĐ1 · 14:00–14:53 | Cài sẵn `.venv` trong `src/`, chuẩn bị phần A1–A4 trong `bang_chi_phi.md`, chạy `lab13.py` lấy số điền vào (nhãn `simulated`, so `12.000 đ` bằng `5.865 đ = 0,49×`) | `report/team/bang_chi_phi.md` (A1–A4); PR #4 (`dee13b6`) |
| GĐ2 · 14:53–15:35 | Điền bảng B1–B4 và câu trả lời (≤ 3 dòng, có số) vào `bang_chi_phi.md`; nhận bàn giao `src/lab13.py` từ #1 sau giải lao | `report/team/bang_chi_phi.md` (B1–B4); PR #7 (`baa1aec`) |
| GĐ3 · 15:35–16:36 | Code phần D1 (cỡ mẫu a–e, `power = 0,6417`) và tính 3 chỉ số E1 + tỉ lệ `mo_lai_trong_7_ngay` (`4,25%` / `3,97%`) vào `src/lab13.py`, push lên Git | `src/lab13.py` (`co_mau`, `bao_cao_d_e`); commit `5f1b39f` |
| GĐ4 · 16:36–18:00 | Điền 3 con số chỉ số E1 vào `report/team/chi_so.md`; hỗ trợ soi số liệu nhóm khác lúc duyệt chéo; chạy lại `python lab13.py` lần cuối; hoàn thiện báo cáo cá nhân và tự nộp link repo lên LMS | `report/team/2A202603729_VuQuangMinh.md`, `report/team/chi_so.md` (đang hoàn tất) |

Mốc giờ ở bảng là lịch phân công, không phải tuyên bố thời gian thực tế đã làm từng thao tác. Việc nộp link repo lên LMS trước 23:59 do tôi tự thực hiện.

## 3. Đóng góp cụ thể

- A1 đạt `1,20`, `1,25`, `1,25`. A2 ghi `4.373.585,13 đ` tổng (`978` việc thành công), CPS `4.471,97 đ/việc` (`simulated`), gấp `16,28 lần` hoá đơn `274,65 đ/yc`; cả hệ thống `5.864,65 đ = 0,49×` của `12.000 đ` (`simulated`).
- A3 tách 4 loại (`noi_dia` `0,225×`, `hang_nang` `0,685×`, `quoc_te` `1,876×`, `doi_tac` `0,851×`, `simulated`), loại `quoc_te` vì tỉ lệ `ok` giảm `30,0% → 11,43% → 2,15%`. A4 tính phần cố định `40 triệu/tháng` cho `noi_dia + hang_nang`: `4.599,09 đ = 0,383×` (45.000 yc/tháng) và `5.784,27 đ = 0,482×` (22.500 yc/tháng, `simulated`).
- B1 đủ 9 kịch bản (`simulated`); B2 `Token + xem lại gấp đôi` đạt `6.543,12 đ (+46,31%)` (`simulated`), xếp hạng 3 yếu tố mạnh nhất: số ca làm lại (`+51,77%`), tỉ lệ xem lại (`+40,70%`), lương nhân viên (`+23,12%`).
- B3: giới hạn 2 lần rẻ nhất cho cả hệ thống (`6.901.220,23 đ`), trong khi 1 lần có CPS thấp nhất (`4.110,99 đ`, `simulated`) nhưng đẩy thêm 85 ca sang nhân viên. B4: xem lại 100% phạm vi `noi_dia + hang_nang` cho `11.742,79 đ = 0,979×` (9 phút làm lại, hoà vốn `5,12` phút) và `12.414,79 đ = 1,035×` (15,3 phút, hoà vốn `4,80` phút, `simulated`).
- D1 trong `src/lab13.py`: `a = 1.251` yc/nhánh; `b: DE = 2,48`, `3.103` yc/nhánh (`42` người/nhánh, tổng `84 > 40`); `c: trần 1.000`; `d: trần 300`; `e: MDE 6 điểm`, `n = 859`, `m = 299`, `DE = 6,96`, `power` ở 5 điểm = `0,6417`.
- E1 trong `src/lab13.py`: Chính `994/1.200 = 82,83%`, Dùng `48/177 = 27,12%`, An toàn `51/1.200 = 4,25%`, An toàn trong phạm vi `39/982 = 3,97%`, Tỉ lệ làm lại trong phạm vi `4,89%`.

## 4. Bằng chứng

- Code: [lab13.py](../../src/lab13.py) (đã chạy `python lab13.py` thoát mã `0`, có fallback chuẩn hoá khi thiếu `statsmodels`; giữ nguyên `lab13_starter.py`).
- Bảng tính: [bang_chi_phi.md](bang_chi_phi.md) (đầy đủ A1–A4 và B1–B4, gắn nhãn `simulated`).
- Chỉ số: [chi_so.md](chi_so.md) (mục tiêu điền 3 chỉ số E1 ở GĐ4).
- Git: PR #4 (`dee13b6`), commit `5f1b39f` (`Update GĐ3`), PR #7 (`baa1aec`).

## 5. Công cụ AI đã dùng

Dùng trợ lý AI trong IDE (Antigravity) để chuẩn hoá bảng A1–A4 và B1–B4 trong `report/team/bang_chi_phi.md` (nhãn `simulated`, câu trả lời ≤ 3 dòng), bổ sung fallback tính `power` cho `src/lab13.py` khi môi trường thiếu `statsmodels`, và định dạng báo cáo cá nhân.

Tự kiểm tra bằng cách chạy trực tiếp `python lab13.py` trong `src/` và đối chiếu toàn bộ kết quả A1–A4, B1–B4, D1 (`power = 0,6417`) và E1 (`82,83%`, `27,12%`, `4,25%`, `3,97%`, `4,89%`) với bảng số liệu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`. Không tự bịa số liệu hay xác nhận các bước chưa chạy.

## 6. Tự đánh giá

Các phần A1–A4, B1–B4 trong `report/team/bang_chi_phi.md` và phần D1, E1 trong `src/lab13.py` đã hoàn thiện và chạy sạch lỗi; mọi chi phí có thời gian nhân viên đều gắn nhãn `simulated`. Cần hoàn tất điền 3 chỉ số E1 vào `report/team/chi_so.md`, hỗ trợ duyệt chéo, chạy kiểm tra cuối và tự nộp link repo lên LMS trước 23:59.
