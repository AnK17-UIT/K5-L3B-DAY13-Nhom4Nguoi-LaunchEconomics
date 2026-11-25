# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm Nhom4Nguoi · L3B · Người tổng hợp: Nguyễn Hoàng Gia An (Trưởng nhóm). Bản đề xuất để rà soát; chưa có kết quả hội đồng. Số liệu từ `lab13.py` và `report/evidence/lab13-output.txt`.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu 4.471,97 đ; phạm vi 3.413,90 đ chưa cố định/làm thay; cộng cố định ở 45.000 yêu cầu tổng/tháng: 4.599,09 đ/việc (simulated) | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2: +51,77%; xem lại ×2: +40,70%; lương +25%: +23,12% trên toàn mẫu (simulated) | Giả lập | Người viết code |
| 3 · So với nhân viên tự làm | Toàn mẫu gồm làm thay: 5.864,65 đ/yêu cầu; B4 trong phạm vi: 11.742,79 hoặc 12.414,79 đ/việc (simulated), tùy làm lại 9/15,3 phút; chưa cố định/làm thay trong B4 | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số và event | Chính 994/1.200=82,83%; bỏ qua 48/177=27,12%; mở lại 51/1.200=4,25%; 11 event thiết kế có trace_id, 5 chỉ số có bảng đối chiếu; chưa có log pilot thật | Xong, có bằng chứng | Trưởng nhóm |
| 5 · Lỗi và khắc phục | Chưa có 2 bộ nhãn độc lập cho 20 ca, chưa tính đồng thuận; chưa thể xác nhận mục C đạt | Chưa | Người gắn nhãn 1 và người gắn nhãn 2 chịu trách nhiệm bộ nhãn riêng |
| 6 · Pilot plan | Đề xuất 20+20 cụm staff, MDE 6 điểm, 859 hiệu dụng/nhánh, 299 yêu cầu/người, DE 6,96; power 0,6417 ở 5 điểm; 5 luật dừng; YAML đã kiểm, chưa ký duyệt | Chưa | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | B4 100% xem lại có thể vượt baseline 12.000 đ; một nửa khối lượng tăng cố định/việc 1.185,19 đ (simulated); 3 dòng rủi ro trong chi_so.md | Giả lập | PM trợ lý hoàn phí |

Điều kiện bắt buộc trước ngày đề xuất bắt đầu 2026-11-30:

- Người gắn nhãn 1 và 2 hoàn thành độc lập 20 ca, so nhãn và bổ sung bảng khắc phục; Trưởng nhóm kiểm bằng chứng ngày 2026-11-27.
- Kỹ sư trưởng agent sửa khóa chống trùng và đối soát sổ cái, kiểm chứng trước 2026-11-27.
- Giám đốc vận hành ký chấp nhận MDE 6 điểm và power 0,6417 ở 5 điểm; PM khóa roster, phân bổ và kế hoạch phân tích trước 2026-11-27.
- Trưởng nhóm CSKH bật đủ event, đo phút thật và có lộ trình giảm xem lại; kiểm mức đầy đủ log ngày 2026-11-27, thay phút simulated sau tuần đầu.
- Người giữ hồ sơ bổ sung phiếu hội đồng từ hồ sơ nhóm được phân công; hiện chưa có bằng chứng chấm chéo.

Ngày trên là lịch đề xuất, chưa phải cam kết đã được xác nhận. Thiếu điều kiện thì không bắt đầu và cập nhật lịch trước thu thập dữ liệu; chỉ xét pilot noi_dia + hang_nang.

**Đề xuất: Go có điều kiện.**
