# Báo cáo cá nhân — Hoàng Minh Diệp — 2A202603764

## 1. Thông tin thành viên

- Họ tên: Hoàng Minh Diệp.
- MSSV: 2A202603764.
- Email: hoangminhdiepnd2004@gmail.com.
- GitHub: diep142 (nhánh làm việc `Vai_3/Diep`).
- Vai trò: Thành viên #3; người gắn nhãn 1 (đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3); hỗ trợ chốt phương án phân bổ trong kế hoạch pilot (D).

## 2. Phần việc phụ trách

| Giai đoạn theo phân công | Công việc | Sản phẩm / bằng chứng |
| --- | --- | --- |
| GĐ1–GĐ2 | Đọc đề, theo dõi điều kiện "Xong khi" của từng nhiệm vụ; gắn độc lập bộ nhãn 1 cho 20 ca lỗi theo 5 loại Google PAIR, ghi lý do theo nguyên nhân gốc | `report/team/nhap_nhan_nguoi_1.md`; commit `c3fdbb6` |
| GĐ2 · CP3 | Chép bộ nhãn 1 sang `bang_loi.md`, điền tên hai người gắn nhãn, soạn bản đầu bảng khắc phục 5 ca (mỗi loại một ca) | `report/team/bang_loi.md`; commit `9318df8` (PR #6) |
| GĐ3 | So nhãn với người gắn nhãn 2, thống nhất 3 ca bất đồng; chốt phương án chia theo `staff` (20+20, MDE 0,06) và bổ sung dòng bốc thăm ngẫu nhiên trong `pilot_plan.yaml` | `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`; commit `e7bda16` |
| GĐ4 | Viết báo cáo cá nhân, đối chiếu số trong báo cáo với file nhóm | `report/team/2A202603764_HoangMinhDiep.md` |

Mốc giai đoạn là lịch phân công, không phải tuyên bố thời gian thực tế của từng thao tác.

## 3. Đóng góp cụ thể

- **Bộ nhãn 1 (C):** gắn độc lập 20 ca, mỗi ca có lý do một dòng theo nguyên nhân gốc, không theo chỗ cần sửa. Phân bố: Do người dùng 4 (ca 1, 6, 9, 14); Hệ thống 5 (2, 7, 8, 15, 20); Ngữ cảnh 4 (3, 10, 16, 18); Giới hạn hệ thống 4 (4, 11, 13, 19); Ngầm 3 (5, 12, 17).
- **Các ca dễ nhầm, đã ghi rõ lý do:** ca 13 gắn Giới hạn hệ thống (bảo hiểm đối tác ngoài phạm vi; trả lời mập mờ là chỗ cần sửa chứ không phải gốc); ca 15 gắn Hệ thống chứ không phải Ngầm (nhân viên xem lại đã bắt được); ca 20 gắn Hệ thống (khách gửi lại là hành vi bình thường, gốc là thiếu khoá chống trùng).
- **Đồng thuận:** sau khi có bộ nhãn 2 của Nguyễn Đức Mạnh, hai bộ trùng 17/20 = 85% (trên ngưỡng 80% nên không cần viết lại định nghĩa). Ba ca bất đồng: ca 6 và 13 giữ theo nhãn của tôi (Do người dùng, Giới hạn hệ thống); ca 18 thống nhất về Hệ thống (tôi gắn Ngữ cảnh) vì đầu ra thiếu cách tính số tiền là thiếu hụt của phản hồi.
- **Bảng khắc phục:** soạn bản đầu 5 ca (1, 2, 3, 4, 5 — mỗi loại một ca) với event phát hiện, ngưỡng/tần suất và một vai trò phụ trách; bản cuối trong `bang_loi.md` đã được người gắn nhãn 2 chỉnh lại.
- **Kế hoạch pilot (D):** cùng nhóm chốt phương án chia theo `staff` 20+20, MDE 6 điểm (vì 40 nhân viên không đủ cho MDE 5 điểm cần 84 người); bổ sung `identifiability.randomization`: bốc thăm bằng code với seed `20261125` ghi trước, phân tầng theo depot, không để quản lý hay nhân viên tự chọn nhóm.

## 4. Bằng chứng

- [nhap_nhan_nguoi_1.md](nhap_nhan_nguoi_1.md): bộ nhãn 1 gốc, kèm bảng đếm nhanh 20 ca; commit `c3fdbb6` ("gán nhãn số 1").
- [bang_loi.md](bang_loi.md): cột "Nhãn người 1", tỉ lệ 17/20 = 85%, quy tắc cho 3 ca bất đồng, bảng khắc phục; commit `9318df8`, merge qua PR #6 (`db01992`).
- [pilot_plan.yaml](pilot_plan.yaml): dòng `randomization` trong `identifiability`; commit `e7bda16`.
- Ghi chú trung thực: commit `9318df8` ban đầu ghi cột "Nhãn người 2" trùng hoàn toàn với bộ của tôi và thông điệp "đồng thuận 20/20 = 100%". Đây không phải bộ nhãn độc lập của người 2; Nguyễn Đức Mạnh đã thay bằng bộ nhãn thật ở commit `4660d15`, cho kết quả đúng 17/20 = 85%. Số 85% là số chính thức của nhóm.

## 5. Công cụ AI đã dùng

Dùng Claude Code (trong VS Code) để định dạng bảng nhãn trong `bang_loi.md`, soạn câu chữ cho bảng khắc phục, gợi ý dòng `randomization` cho `pilot_plan.yaml` và soạn báo cáo này.

Phần gắn nhãn 20 ca do tôi tự đọc đề và tự quyết định theo định nghĩa 5 loại; AI không chọn nhãn thay. Cách tự kiểm: đếm lại phân bố nhãn khớp 20 ca; đối chiếu cột "Nhãn người 1" trong `bang_loi.md` với `nhap_nhan_nguoi_1.md`; kiểm tra seed `20261125`, 20+20 staff và MDE 0,06 khớp với `pilot_plan.yaml` và output D1 của `src/lab13.py`. 

## 6. Tự đánh giá

Tôi hoàn thành vai người gắn nhãn 1: bộ nhãn độc lập có lý do cho từng ca, tham gia thống nhất 3 ca bất đồng và có thể giải thích vì sao từng ca thuộc loại đó. Điểm cần cải thiện: không điền hộ phần việc của người khác (cột nhãn người 2) dù chỉ là tạm, và ghi thời điểm so nhãn rõ hơn để chứng minh tính độc lập. Phần D tôi chỉ đóng góp quyết định phân bổ và dòng ngẫu nhiên hoá; phần tính cỡ mẫu do thành viên khác code.
