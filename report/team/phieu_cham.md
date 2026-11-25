# Phiếu chấm hội đồng Gate 2a

- Nhóm chấm (hội đồng): Nhom4Nguoi, lớp L3B.
- Nhóm được chấm: DatTanhHai, lớp L3B.
- Hồ sơ được chấm: [repo DatTanhHai](https://github.com/datkunal/K5-L3B-DAY13-DatTanhHai-LaunchEconomics), commit `b3c8989443a480c2e49243d2679506e4f40e7a9f`.
- Người tổng hợp phiếu: Nguyễn Đức Mạnh (người giữ hồ sơ).
- Nội dung hỏi–đáp được Nguyễn Hoàng Gia An cung cấp sau trao đổi giữa hai nhóm.

## Điểm và quyết định

| Tiêu chí | Điểm / 10 | Lý do và bằng chứng |
| --- | ---: | --- |
| Đề xuất khớp bằng chứng | 10 | Go có điều kiện khớp phạm vi pilot. Hồ sơ nêu xem lại 100% cộng cố định tốn 12.928 đ/việc, hàng nặng riêng 16.638 đ/việc (simulated), power chỉ 0,64 nếu tác động thật 5 điểm; có cổng an toàn khi giảm xem lại, điều kiện không mở rộng hàng nặng và yêu cầu ký chấp nhận đánh đổi. Bằng chứng: ho_so_launch_v0.md, mục 3, 6, 7 và các điều kiện pilot. |
| Số giả lập và phạm vi | 10 | Các chi phí phụ thuộc phút giả lập và tỉ số tương ứng có nhãn simulated. Chỉ pilot nội địa và hàng nặng; loại quốc tế vì CPS 22.515 đ = 1,88× baseline (simulated), loại đối tác vì chỉ 54,4% thành công, mẫu 68 yêu cầu và điều khoản riêng. Bằng chứng: bang_chi_phi.md, A3–A4, B4; pilot_plan.yaml, scope và simulated_inputs. |
| Pilot ra được quyết định | 10 | Phân bổ ngẫu nhiên 20+20 nhân viên, có đối chứng cùng thời gian; với ICC 0,02 và MDE 6 điểm, ≥299 yêu cầu/người đạt 859 hiệu dụng/nhánh. Bước 50% kéo dài 14 ngày; có 6 luật dừng với ngưỡng, thời gian, hành động và người có quyền dừng. Bằng chứng: pilot_plan.yaml, assignment, schedule, primary_metric, stop_rules và decision_rule. |
| Tổng / 30 | 30 | Đạt mức 10 ở cả 3 tiêu chí của hội đồng. |

Quyết định của hội đồng: **Go có điều kiện**.

Lý do: cho phép pilot trong phạm vi đã thu hẹp khi khóa chống trùng, đối soát sổ cái, event và đo phút thật sẵn sàng; Giám đốc vận hành ký chấp nhận đánh đổi cỡ mẫu và ngân sách. Chưa đủ cơ sở mở rộng ngay: xem lại toàn bộ có thể đắt hơn làm tay, power chỉ khoảng 0,64 nếu tác động thật là 5 điểm phần trăm. Riêng hàng nặng không được mở rộng nếu tỉ lệ gợi ý sai cuối pilot vẫn trên 7%.

## Nhóm mình hỏi DatTanhHai

Câu hỏi:

> Hàng nặng đang tốn 16.638 đ/việc thành công khi xem lại 100%, cao hơn mức làm tay 12.000 đ. Vì sao nhóm vẫn giữ loại này trong pilot? Nếu cuối pilot tỉ lệ gợi ý sai vẫn trên 7%, nhóm sẽ quyết định thế nào với riêng hàng nặng?

Câu trả lời của DatTanhHai, theo nội dung được cung cấp:

> 16.638 đồng là 1,39 lần làm tay, chúng tôi ghi thẳng trong hồ sơ. Đó là chi phí khi xem lại 100%, cách chạy an toàn lúc thử. Trong đợt chạy thử, chỉ xem lại 22%, hàng nặng tốn 8.221 đồng, bằng 0,69 lần. Vậy câu hỏi là: giảm xem lại được không? Chưa trả lời được, vì gợi ý sai là 13,3%, 18 trên 135 ca, và mở lại 8,23%. Pilot giữ hàng nặng để đo cho chắc, chứ không phải để tiết kiệm.
>
> Nếu cuối pilot vẫn trên 7% thì không mở rộng hàng nặng: trả về nhân viên làm tay, còn nội địa quyết định riêng. Chúng tôi không hạ xem lại để kéo chi phí xuống khi AI còn sai nhiều, và không kéo dài để chờ số đẹp. Giám đốc vận hành là người chốt, ngày 13/01/2027.

Các chi phí và tỉ số chi phí trong câu trả lời trên là simulated. Ngày 13/01/2027 là lịch quyết định chính; theo luật 5 trong hồ sơ, chỉ được dời sang 20/01/2027 nếu phải kéo dài do nhiễm đối chứng.

## DatTanhHai hỏi nhóm mình

Câu hỏi:

> Ở bước 10% (30/11–06/12) nhóm xem lại bao nhiêu phần trăm câu trả lời? Nếu 100% thì chi phí là 11.742,79 đ [simulated], vượt ngưỡng dừng 8.000 đ của chính nhóm; nếu ít hơn thì cái gì chặn lỗi tới khách, khi luật mở lại chưa có yêu cầu nào đủ 7 ngày trong tuần đó?

Câu trả lời của nhóm mình:

> Hồ sơ đang thiếu tỉ lệ xem lại ở bước 10%; nhóm sẽ bổ sung duyệt 100% trước khi gửi khách hoặc hoàn tiền. Tuần đầu chấp nhận chi phí cao để kiểm chứng an toàn.
>
> Ngưỡng 8.000 đ hiện chỉ kích hoạt sau hai tuần vượt liên tiếp, nhưng nhóm cần bổ sung rõ ngân sách giai đoạn đầu và thời điểm áp dụng ngưỡng.
>
> Khi chưa đủ dữ liệu mở lại 7 ngày, nhóm dùng duyệt trước, khóa chống trùng và đối soát sổ cái để chặn lỗi; chưa đủ bằng chứng thì chưa giảm xem lại hoặc tăng rollout.

Việc cần cập nhật sau bảo vệ: tỉ lệ duyệt 100% ở bước 10%, ngân sách giai đoạn đầu và thời điểm áp dụng ngưỡng 8.000 đ trong pilot_plan.yaml. Đây là các bổ sung đã nêu trong câu trả lời, chưa coi là đã có trong YAML.
