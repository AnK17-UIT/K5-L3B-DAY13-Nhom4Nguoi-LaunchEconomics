# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm Nhom4Nguoi · L3B · Người tổng hợp: Nguyễn Hoàng Gia An (Trưởng nhóm). Bản đề xuất để rà soát; chưa có kết quả hội đồng. Số liệu từ `lab13.py` và `report/evidence/lab13-output.txt`.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | A2 toàn mẫu: 4.471,97 đ/việc; A4 nội địa + hàng nặng ở 45.000 yêu cầu/tháng: 4.599,09 đ/việc gồm 1.185,19 đ chi phí cố định (simulated) | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2: +51,77%; xem lại ×2: +40,70%; lương +25%: +23,12% trên toàn mẫu (simulated) | Giả lập | Người viết code |
| 3 · So với nhân viên tự làm | B3 toàn mẫu gồm làm thay: 5.864,65 đ/yêu cầu (0,49× 12.000 đ); B4 trong phạm vi: 11.742,79 đ/việc ở 9 phút hoặc 12.414,79 đ ở 15,3 phút (simulated), chưa gồm cố định/làm thay | Giả lập | Người kiểm số |
| 4 · Chỉ số và event | Chính 994/1.200=82,83%; bỏ qua 48/177=27,12%; mở lại 51/1.200=4,25%; 11 event thiết kế có trace_id, 5 chỉ số có bảng đối chiếu; chưa có log pilot thật | Xong, có bằng chứng | Trưởng nhóm |
| 5 · Lỗi và khắc phục | 17/20 nhãn trùng (85%); 3 ca bất đồng đã thống nhất; đủ 5 loại lỗi và cách phát hiện/khắc phục | Xong, có bằng chứng | Người gắn nhãn 2, kiêm giữ hồ sơ |
| 6 · Pilot plan | Phạm vi `noi_dia` + `hang_nang`; 20 nhân viên/nhánh, ngẫu nhiên theo depot; rollout 10/25/50%; MDE 6 điểm, 859 hiệu dụng/nhánh (DE 6,96), ≥299 yêu cầu/nhân viên; power 0,6417 nếu tác động thật là 5 điểm; 5 luật dừng; quyết định 2027-01-05 | Chưa | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | B4 100% xem lại có thể vượt baseline 12.000 đ; một nửa khối lượng tăng cố định/việc 1.185,19 đ (simulated); 3 dòng rủi ro trong chi_so.md | Giả lập | PM trợ lý hoàn phí |

Điều kiện bắt buộc trước ngày đề xuất bắt đầu 2026-11-30:

- Người gắn nhãn 1 và 2 lưu hai bộ nhãn độc lập cùng kết quả thống nhất 3 ca bất đồng; Trưởng nhóm kiểm bằng chứng ngày 2026-11-27.
- Kỹ sư trưởng agent sửa khóa chống trùng và đối soát sổ cái, kiểm chứng trước 2026-11-27.
- Giám đốc vận hành ký chấp nhận MDE 6 điểm và power 0,6417 ở 5 điểm; PM khóa roster, phân bổ và kế hoạch phân tích trước 2026-11-27.
- Trưởng nhóm CSKH bật đủ event, đo phút thật và có lộ trình giảm xem lại; kiểm mức đầy đủ log ngày 2026-11-27, thay phút simulated sau tuần đầu.
- Người giữ hồ sơ bổ sung phiếu hội đồng từ hồ sơ nhóm được phân công; hiện chưa có bằng chứng chấm chéo.

Ngày trên là lịch đề xuất, chưa phải cam kết đã được xác nhận. Thiếu điều kiện thì không bắt đầu và cập nhật lịch trước thu thập dữ liệu; chỉ xét pilot noi_dia + hang_nang.

**Đề xuất: Go có điều kiện.**
