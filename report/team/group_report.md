# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính. 

## 1. Thông tin nhóm

- Tên nhóm: Nhom4Nguoi
- Lớp: L3B
- Repo: https://github.com/AnK17-UIT/K5-L3B-DAY13-Nhom4Nguoi-LaunchEconomics, nhánh nộp `main`
- Thành viên: Nguyễn Hoàng Gia An (trưởng nhóm, viết code A/B), Vũ Quang Minh (kiểm số, nhận code sau giải lao), Hoàng Minh Diệp (gắn nhãn 1), Nguyễn Đức Mạnh (gắn nhãn 2, giữ hồ sơ). Chi tiết ở `TEAM.md`.

## 2. Mục tiêu và cách tiếp cận

Nhóm cần trả lời: trợ lý hoàn phí LogiX-VN có rẻ hơn nhân viên làm tay (12.000 đ/yêu cầu) không, và nếu có thì pilot thế nào để đo được tác động thật.

Chi phí tính trên **việc thành công**, cộng mọi lần chạy kể cả lần lỗi, cộng phút nhân viên xem lại và làm lại. Sau đó thu hẹp phạm vi theo loại yêu cầu, thử độ nhạy, rồi mới thiết kế pilot có đối chứng ngẫu nhiên. Công thức theo `docs/du_lieu_va_cong_thuc.md`; số được tính bằng `src/lab13.py`, người kiểm số đối chiếu lại với bảng trong hướng dẫn.

## 3. Giải pháp

- **A, B (`bang_chi_phi.md`):** A1–A4 và B1–B4 trong `src/lab13.py`. Loại `quoc_te` (27,33% thành công, 22.515,17 đ = 1,876× baseline) và `doi_tac` (54,41% thành công, có điều khoản riêng) bị loại khỏi phạm vi; pilot chỉ gồm `noi_dia` và `hang_nang`.
- **C (`bang_loi.md`):** hai người gắn nhãn độc lập 20 ca theo năm loại của Google PAIR, trùng 17/20 (85%). Ba ca lệch (6, 13, 18) được thống nhất theo nguyên nhân gốc, mỗi ca một quy tắc. Bảng khắc phục có đủ năm loại, mỗi dòng có event, ngưỡng và một vai trò phụ trách.
- **D (`pilot_plan.yaml`):** chia theo `staff`, 20 can thiệp và 20 đối chứng, bốc thăm bằng seed `20261125`, phân tầng theo depot; rollout 10/25/50%; năm luật dừng có ngưỡng, thời hạn và người có quyền tắt. File đọc được bằng `yaml.safe_load`.
- **E (`chi_so.md`, `ho_so_launch_v0.md`):** ba chỉ số chính/dùng/an toàn, thêm hai chỉ số mới (tiếp nhận trợ lý, sai tiền kiểm toán), 11 event có `trace_id`, ba dòng rủi ro kinh tế lấy số từ bảng độ nhạy. Hồ sơ launch một trang, bảy mục.

## 4. Kết quả

| Câu hỏi | Kết quả |
| --- | --- |
| A1 | ĐẠT: 1.20 / 1.25 / 1.25 |
| Chi phí mỗi việc thành công (A2, toàn mẫu) | 4.471,97 đ, gấp 16,28 lần hoá đơn 274,65 đ/yêu cầu |
| Phạm vi `noi_dia` + `hang_nang`, có phần cố định (A4) | 4.599,09 đ ở 45.000 yêu cầu/tháng; 5.784,27 đ nếu khối lượng giảm một nửa |
| Yếu tố nhạy nhất (B2) | Làm lại ×2: +51,77%; xem lại ×2: +40,70%; lương +25%: +23,12% |
| Giới hạn lần chạy (B3) | 2 lần cho tổng hệ thống thấp nhất (6.901.220,23 đ); 1 lần có CPS thấp nhất nhưng đẩy thêm 85 ca sang nhân viên |
| Xem lại 100% (B4) | 11.742,79 đ với 9 phút làm lại (0,979×); 12.414,79 đ với 15,3 phút (1,035×, **vượt** 12.000 đ) |
| Chỉ số E1 (mẫu chạy thử, không có đối chứng) | Chính 82,83%; bỏ qua gợi ý 27,12%; mở lại 7 ngày 4,25% (3,97% trong phạm vi) |
| Cỡ mẫu D1 | MDE 5 điểm cần 84 nhân viên, nhóm chỉ có 40. Chọn MDE 6 điểm: 299 yêu cầu/nhân viên, DE 6,96, 859 hiệu dụng/nhánh |

**Đề xuất trong hồ sơ: Go có điều kiện.** Con số bất lợi nhóm giữ lại trong hồ sơ: B4 vượt baseline nếu làm lại mất 15,3 phút, và power chỉ 0,6417 nếu tác động thật là 5 điểm. Bốn điều kiện trước pilot có người phụ trách và hạn 27/11/2026, trong đó quan trọng nhất là khoá chống trùng (ca 20 hoàn tiền hai lần) và việc Giám đốc vận hành ký chấp nhận đánh đổi MDE/power.


## 5. Khó khăn và cách xử lý

- Cài thư viện và push Git cần quyền mạng ngoài sandbox của công cụ AI; nhóm chạy lại sau khi được cấp quyền. Biên bản ở `report/evidence/kiem_tra.md`.
- Repo tắt Issues nên An bàn giao code cho Minh bằng bình luận commit (`report/evidence/ban_giao.md`, link ở `ban_giao-url.txt`).
- Máy của Minh thiếu `statsmodels`, Minh thêm cách tính power dự phòng trong `lab13.py`; script chạy lại thoát mã 0, power vẫn ra 0,6417.

## 6. Tổng hợp đóng góp

| Thành viên | Phần chính | Bằng chứng |
| --- | --- | --- |
| Nguyễn Hoàng Gia An | A1–A4, B1–B4, đặc tả chỉ số và event, bổ sung D1, kiểm tra YAML và từ cấm | `de4d995`, `18c079a`, `report/evidence/` |
| Vũ Quang Minh | Kiểm số và điền `bang_chi_phi.md`, code D1 và E1 sau giải lao | PR #4, `5f1b39f`, PR #7 |
| Hoàng Minh Diệp | Bộ nhãn 1, bản đầu bảng khắc phục, chốt chia theo `staff` và dòng ngẫu nhiên hoá trong pilot | `c3fdbb6`, `9318df8`, `e7bda16` |
| Nguyễn Đức Mạnh | Bộ nhãn 2, thống nhất 3 ca lệch, hồ sơ launch v0 và bốn điều kiện Go | `4660d15`, `22496f1`, `82a4ca0`, `d2c6951` |

Báo cáo cá nhân của từng người ở `report/team/<MSSV>_<HoTen>.md`.

## 7. Hạn chế và hướng cải thiện

- 82,83% là số của mẫu chạy thử, không có đối chứng, chưa phải bằng chứng tác động.
- Với 40 nhân viên, pilot chỉ đủ phát hiện tác động từ 6 điểm; nếu tác động thật là 5 điểm thì khả năng bỏ sót khoảng 36%.

## 8. Tài liệu tham khảo

`docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, `RULES.md`, `SUBMISSION.md`. Hai file CSV và `src/lab13_starter.py` giữ nguyên.
