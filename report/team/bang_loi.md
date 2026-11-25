# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: ... · Người gắn nhãn 2: ... (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |
| 6 | ... | ... | ... | ... |
| 7 | ... | ... | ... | ... |
| 8 | ... | ... | ... | ... |
| 9 | ... | ... | ... | ... |
| 10 | ... | ... | ... | ... |
| 11 | ... | ... | ... | ... |
| 12 | ... | ... | ... | ... |
| 13 | ... | ... | ... | ... |
| 14 | ... | ... | ... | ... |
| 15 | ... | ... | ... | ... |
| 16 | ... | ... | ... | ... |
| 17 | ... | ... | ... | ... |
| 18 | ... | ... | ... | ... |
| 19 | ... | ... | ... | ... |
| 20 | ... | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| ... | Do người dùng | ... | ... | ... |
| ... | Hệ thống | ... | ... | ... |
| ... | Ngữ cảnh | ... | ... | ... |
| ... | Giới hạn hệ thống | ... | ... | ... |
| ... | Ngầm | ... | ... | ... |

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
