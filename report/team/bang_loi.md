# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Hoàng Minh Diệp · Người gắn nhãn 2: Nguyễn Đức Mạnh (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100% (đạt ngưỡng ≥ 80%). Nhãn thống nhất khớp bảng nhãn tham khảo trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` 20/20.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Không có ca lệch (20/20 trùng), nên không cần chốt lại hay viết lại định nghĩa. Ghi chú các ca dễ lẫn mà hai người đều gắn giống nhau:
- **Ca 6, 9 là Do người dùng:** gốc lỗi là khách chọn sai mục hoặc nhập sai mã; việc trợ lý không gợi ý nằm ở cột khắc phục.
- **Ca 13 là Giới hạn hệ thống:** ngoài phạm vi thì là giới hạn, kể cả khi trợ lý xử lý giới hạn đó kém.
- **Ca 8, 15 là Hệ thống, không phải Ngầm:** sai đã lộ ra (trích dẫn nhìn thấy được, nhân viên bắt được).
- **Ca 18 là Ngữ cảnh:** số tiền đúng chính sách, chỉ giả định "khách hiểu cách tính" là không khớp.
- **Ca 12 là Ngầm:** kết quả đúng nhưng chi phí token gấp 3 lần suốt 3 tuần mà không ai thấy.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, ghi rõ một vai trò chịu trách nhiệm.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (reason = sai_dinh_dang_ma); đếm theo ngày, cảnh báo khi > 2% số yêu cầu/ngày | Nhận diện mã đơn sàn TMĐT và tự tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh chỉ vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Job đối soát mỗi giờ: tin nhắn "đã hoàn" không có bản ghi sổ cái `status = ok` cùng `trace_id`; ngưỡng 0 ca, vượt là báo động ngay | Chỉ gửi "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thử thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Event `request_reopened` với reason = so_tien, lọc các ca kiểm tra lại thấy số tiền đúng; theo dõi hằng tuần, cảnh báo khi > 3% số yêu cầu đã hoàn | Mẫu tin nhắn luôn ghi cách tính, ví dụ: 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với reason = thieu_du_lieu, nhóm theo loại yêu cầu; báo cáo hằng ngày, cảnh báo khi một loại > 5% số yêu cầu | Giữ cách chuyển nhân viên kèm tóm tắt; đưa đơn quốc tế (quoc_te) ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần, so số tiền hoàn với bảng giá hiện hành; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới; ghi phiên bản bảng giá vào trace để đối soát | Kế toán trưởng |

# Gán nhãn 2

| Ca | Nhãn tham khảo | Lý do ngắn |
| --: | --- | --- |
| 1 | Do người dùng | Khách nhập thiếu chữ số tài khoản. |
| 2 | Hệ thống | Trợ lý dùng sai bảng giá, gây hoàn thiếu. |
| 3 | Ngữ cảnh | Trợ lý làm theo thiết kế nhưng kỳ vọng của khách khác với cách hoàn tiền. |
| 4 | Giới hạn hệ thống | Thiếu dữ liệu về chặng của hãng nước ngoài. |
| 5 | Ngầm | Hoàn thừa tiền nhưng khách và hệ thống đều không phát hiện. |
| 6 | Do người dùng | Khách chọn nhầm loại yêu cầu. |
| 7 | Hệ thống | Ghi sổ thất bại nhưng trợ lý vẫn báo đã hoàn tiền. |
| 8 | Hệ thống | Trợ lý viện dẫn điều khoản không tồn tại. |
| 9 | Do người dùng | Khách nhập mã đơn sàn thay vì mã vận đơn. |
| 10 | Ngữ cảnh | Trợ lý áp dụng chính sách đúng nhưng khách thấy không hợp lý với cam kết giao hàng. |
| 11 | Giới hạn hệ thống | Trợ lý không xử lý được tin nhắn thoại. |
| 12 | Ngầm | Dữ liệu tool thiếu làm chi phí tăng kéo dài mà không ai nhận ra. |
| 13 | Giới hạn hệ thống | Yêu cầu bảo hiểm đối tác ngoài phạm vi trợ lý; câu trả lời chung chung cho thấy xử lý giới hạn chưa tốt. |
| 14 | Do người dùng | Khách bấm nhầm xác nhận đã nhận tiền. |
| 15 | Hệ thống | Trợ lý tính sai mức hoàn theo chính sách. |
| 16 | Ngữ cảnh | Trợ lý gửi đúng theo thiết kế nhưng thời điểm gửi không phù hợp với khách. |
| 17 | Ngầm | Bảng giá cũ gây sai tiền nhiều ngày mà không có cảnh báo hay yêu cầu mở lại. |
| 18 | Ngữ cảnh | Số tiền đúng nhưng thiếu giải thích khiến khách hiểu nhầm. |
| 19 | Giới hạn hệ thống | Trợ lý không truy cập được dữ liệu quá 12 tháng và chuyển nhân viên. |
| 20 | Hệ thống | Thiếu khóa chống trùng khiến trợ lý hoàn tiền hai lần. |
