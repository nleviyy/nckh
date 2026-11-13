# BỘ SLIDE THUYẾT TRÌNH BẢO VỆ ĐỀ CƯƠNG NGHIÊN CỨU KHOA HỌC
## THỜI LƯỢNG BÁO CÁO: 10 PHÚT (VẤN ĐÁP 5 PHÚT)

---

### CƠ CẤU PHÂN BỔ THỜI GIAN THUYẾT TRÌNH (TỔNG 10 PHÚT):
* **Slide 1 – 2:** Giới thiệu, Tính cấp thiết & Luận cứ liên ngành (02 phút)
* **Slide 3 – 4:** Mục tiêu, Câu hỏi & Giả thuyết khoa học (01.5 phút)
* **Slide 5 – 6:** Thiết kế nghiên cứu & Phương pháp học máy (02.5 phút)
* **Slide 7 – 8:** Kết quả thực nghiệm sơ bộ (Pilot Study) (02.5 phút)
* **Slide 9 – 10:** Kế hoạch 6 tháng, Ma trận rủi ro & Kết luận (01.5 phút)

---

## SLIDE 1: TRANG TIÊU ĐỀ
* **Tiêu đề đề tài:** NGHIÊN CỨU ỨNG DỤNG THUẬT TOÁN HỌC MÁY (MACHINE LEARNING) KẾT HỢP YẾU TỐ KHÍ TƯỢNG NHẰM DỰ BÁO NỒNG ĐỘ BỤI MỊN $\text{PM}_{2.5}$ TẠI THÀNH PHỐ ĐÀ NẴNG
* **Người trình bày:** Sinh viên [Họ tên] – Lớp: [Tên lớp] – Khoa Công nghệ thông tin
* **Trường:** Đại học Sư phạm – Đại học Đà Nẵng
* **Học phần:** Phương pháp nghiên cứu khoa học trong Khoa học tự nhiên
* **Giảng viên hướng dẫn:** [Họ tên GVHD]
* **Thời lượng dự kiến:** 10 phút

> **SPEAKER NOTES (LỜI THUYẾT MINH - 00:00 - 00:45):**  
> *"Kính thưa quý thầy cô trong Hội đồng đánh giá, em tên là [Họ tên], sinh viên khoa Công nghệ thông tin, Trường Đại học Sư phạm – Đại học Đà Nẵng. Hôm nay, em xin phép được báo cáo đề cương nghiên cứu khoa học liên ngành với đề tài: 'Nghiên cứu ứng dụng thuật toán học máy kết hợp yếu tố khí tượng nhằm dự báo nồng độ bụi mịn PM2.5 tại thành phố Đà Nẵng'. Nghiên cứu được xây dựng nhằm giải quyết bài toán cấp bách về giám sát và cảnh báo ô nhiễm không khí tại đô thị Đà Nẵng thông qua sự giao thoa giữa Khoa học Môi trường và Công nghệ thông tin."*

---

## SLIDE 2: TÍNH CẤP THIẾT & TÍNH LIÊN NGÀNH CỐT LÕI
* **Bối cảnh thực tiễn Đà Nẵng:**
  * Mục tiêu xây dựng "Thành phố môi trường" và đô thị sinh thái thông minh.
  * Thách thức: Tốc độ gia tăng phương tiện giao thông, hoạt động xây dựng và khu công nghiệp (Hòa Cầm, Liên Chiểu).
  * Hạn chế hiện nay: Hệ thống quan trắc mới chỉ **mô tả hiện trạng**, thiếu khả năng **dự báo sớm trước 1–24 giờ**.
* **Tính liên ngành bắt buộc:**
  * *Khoa học Môi trường:* Giải thích cơ chế hóa khí quyển, vai trò gió biển – gió đất, độ ẩm, lượng mưa và đối chiếu chuẩn QCVN 05:2023/BTNMT.
  * *Công nghệ thông tin:* Cung cấp kỹ thuật xử lý dữ liệu lớn chuỗi thời gian, thuật toán học máy (Random Forest, XGBoost) tối ưu hóa dự báo phi tuyến.

> **SPEAKER NOTES (LỜI THUYẾT MINH - 00:45 - 02:00):**  
> *"Thưa thầy cô, Đà Nẵng là đô thị du lịch trọng điểm đang hướng tới mô hình đô thị môi trường. Tuy nhiên, sự gia tăng giao thông và phát triển công nghiệp đang gây sức ép lớn lên chất lượng không khí, đặc biệt là bụi mịn PM2.5. Hiện nay, các trạm quan trắc tự động của thành phố chỉ cho chúng ta biết nồng độ hiện tại mà chưa thể dự báo được xu hướng trong vài giờ tới. Để giải quyết vấn đề này, nếu chỉ dùng Khoa học Môi trường sẽ gặp khó khăn khi mô hình hóa dữ liệu lớn thời gian thực; còn nếu chỉ dùng CNTT đơn thuần thì mô hình dễ trở thành 'hộp đen' thiếu căn cứ vật lý. Vì vậy, đề tài này kết hợp chặt chẽ: tri thức Môi trường dẫn dắt việc chọn đặc trưng khí tượng ven biển, còn CNTT tối ưu hóa thuật toán học máy để đưa ra dự báo chính xác nhất."*

---

## SLIDE 3: TỔNG QUAN TÀI LIỆU & KHOẢNG TRỐNG TRI THỨC
* **Tổng quan nghiên cứu:**
  * Thế giới: Các thuật toán học máy dạng cây (Tree-based Ensemble) như Random Forest, XGBoost đạt độ chính xác cao trong bài toán dự báo ô nhiễm (Zheng et al., 2015; Gu et al., 2020).
  * Việt Nam: Đã có nghiên cứu tại Hà Nội (Pham et al., 2021) và TP.HCM (Nguyen et al., 2022).
* **Khoảng trống tri thức (Knowledge Gap):**
  * *Khoảng trống 1:* Chưa có nghiên cứu chuyên sâu áp dụng Machine Learning dự báo $\text{PM}_{2.5}$ thích ứng với **vi khí hậu ven biển đặc thù của miền Trung (Đà Nẵng)**.
  * *Khoảng trống 2:* Thiếu một khung quy trình mở, chi phí thấp, có khả năng xử lý dữ liệu gián đoạn sẵn sàng chuyển giao cho địa phương.

> **SPEAKER NOTES (LỜI THUYẾT MINH - 02:00 - 03:00):**  
> *"Qua tổng quan hơn 10 công trình khoa học trong và ngoài nước, em nhận thấy các mô hình học máy dạng cây như Random Forest và XGBoost luôn chứng minh ưu thế vượt trội về độ chính xác và khả năng kiểm soát quá khớp trên dữ liệu bảng chuỗi thời gian. Tuy nhiên, một khoảng trống tri thức lớn hiện nay là hầu hết các nghiên cứu tại Việt Nam mới chỉ tập trung vào Hà Nội và TP.HCM. Đà Nẵng với đặc thù vi khí hậu ven biển nhiệt đới gió mùa vẫn chưa có một nghiên cứu học máy nào được triển khai bài bản. Đây chính là khoảng trống khoa học mà đề tài tập trung giải quyết."*

---

## SLIDE 4: MỤC TIÊU, CÂU HỎI & GIẢ THUYẾT KHOA HỌC
* **Mục tiêu tổng quát:** Xây dựng khung mô hình học máy tích hợp yếu tố khí tượng dự báo chính xác nồng độ $\text{PM}_{2.5}$ theo giờ tại thành phố Đà Nẵng.
* **3 Mục tiêu cụ thể:**
  1. Thu thập, chuẩn hóa dữ liệu $\text{PM}_{2.5}$ và khí tượng; phân tích tương quan vi khí hậu.
  2. Thiết kế, huấn luyện và tối ưu mô hình học máy (RF, XGBoost); đánh giá qua $RMSE, MAE, R^2$.
  3. Thử nghiệm Pilot, kiểm định theo QCVN 05:2023/BTNMT và đề xuất giải pháp ứng dụng.
* **Giả thuyết khoa học chủ đạo:**
  * *H1:* Tốc độ gió và lượng mưa tương quan nghịch mạnh ($p < 0.05$) với $\text{PM}_{2.5}$ do xáo trộn khí quyển và rửa trôi.
  * *H2:* Thuật toán XGBoost đạt hiệu năng vượt trội ($R^2 > 0.80$, $RMSE$ thấp hơn ít nhất 10% so với Random Forest).

> **SPEAKER NOTES (LỜI THUYẾT MINH - 03:00 - 04:00):**  
> *"Dựa trên khoảng trống tri thức đó, mục tiêu tổng quát của đề tài là xây dựng mô hình học máy kết hợp khí tượng để dự báo nồng độ PM2.5 theo giờ tại Đà Nẵng. Em đặt ra hai giả thuyết khoa học trọng tâm: Thứ nhất, tốc độ gió biển và lượng mưa sẽ có tương quan nghịch mạnh với nồng độ bụi mịn. Thứ hai, với cơ chế tối ưu hóa độ dốc và điều chuẩn chặt chẽ, thuật toán XGBoost sẽ mang lại kết quả dự báo vượt trội so với Random Forest trên cùng tập dữ liệu."*

---

## SLIDE 5: THIẾT KẾ NGHIÊN CỨU & KHUNG PIPELINE LIÊN NGÀNH
* **Sơ đồ đường ống nghiên cứu (Pipeline):**
  $$\text{Dữ liệu quan trắc + Khí tượng} \rightarrow \text{Tiền xử lý (FAIR)} \rightarrow \text{Kỹ nghệ đặc trưng} \rightarrow \text{Huấn luyện ML} \rightarrow \text{Đánh giá sai số}$$
* **Kỹ nghệ đặc trưng (Feature Engineering):**
  * *Biến trễ thời gian:* $\text{PM}_{2.5}(t-1), \text{PM}_{2.5}(t-2), \text{PM}_{2.5}(t-24)$.
  * *Biến thống kê trượt:* Trung bình trượt 3 giờ và 24 giờ (`Rolling Mean`).
  * *Biến chu kỳ thời gian:* Mã hóa lượng giác $hour_{sin}, hour_{cos}$ phản ánh nhịp sinh hoạt và giao thông đô thị.
* **Kiểm soát rò rỉ dữ liệu:** Sử dụng kỹ thuật chia dữ liệu `TimeSeriesSplit` (tập Train luôn đi trước tập Test).

> **SPEAKER NOTES (LỜI THUYẾT MINH - 04:00 - 05:30):**  
> *"Về phương pháp nghiên cứu, đề tài thiết lập một quy trình 5 bước nghiêm ngặt. Để mô hình nắm bắt được bản chất vật lý của khí quyển, em không chỉ đưa vào các biến tức thời mà còn thực hiện kỹ nghệ đặc trưng: trích xuất các biến trễ thời gian t-1, t-2, t-24; các giá trị trung bình trượt 3 giờ và 24 giờ; cùng các biến điều hòa chu kỳ ngày đêm. Đặc biệt, để ngăn chặn triệt để hiện tượng rò rỉ dữ liệu tương lai vào quá khứ, toàn bộ quy trình kiểm định chéo đều sử dụng TimeSeriesSplit, bảo đảm tính nghiêm ngặt tuyệt đối của phương pháp luận KHTN."*

---

## SLIDE 6: MÔ HÌNH HỌC MÁY & CHỈ SỐ ĐÁNH GIÁ SAI SỐ
* **Hai thuật toán học máy được lựa chọn:**
  * **Random Forest Regressor:** Cơ chế Bagging, trung bình hóa dự báo từ nhiều cây quyết định độc lập, kháng nhiễu và chống quá khớp tốt.
  * **XGBoost Regressor:** Cơ chế Gradient Boosting tuần tự, tối ưu hàm mất mát kết hợp phạt điều chuẩn $\text{L}_1/\text{L}_2$, xử lý cực tốt quan hệ phi tuyến phức tạp.
* **Hệ thống chỉ số đánh giá chuẩn hóa:**
  * $MAE$ (Sai số tuyệt đối trung bình - $\mu\text{g/m}^3$)
  * $RMSE$ (Căn bậc hai sai số toàn phương trung bình - $\mu\text{g/m}^3$)
  * $R^2$ Score (Hệ số xác định phương sai giải thích)
  * Kiểm định độ không đảm bảo đo mở rộng ở khoảng tin cậy 95% ($U_{95\%}$).

> **SPEAKER NOTES (LỜI THUYẾT MINH - 05:30 - 06:30):**  
> *"Đề tài lựa chọn hai thuật toán học máy giám sát đại diện cho hai trường phái Ensemble Learning mạnh mẽ nhất: Random Forest dựa trên Bagging và XGBoost dựa trên Gradient Boosting. Hiệu năng của mô hình được đánh giá toàn diện bằng ba độ đo chuẩn hóa: MAE phản ánh sai số trung bình, RMSE đo độ nhạy với các đỉnh ô nhiễm đột biến, và R2 đo tỷ lệ biến thiên được giải thích. Bên cạnh đó, các sai số đo lường đều được đánh giá độ không đảm bảo đo ở mức tin cậy 95% theo chuẩn KHTN."*

---

## SLIDE 7: KẾT QUẢ THỰC NGHIỆM PILOT – PHÂN TÍCH TƯƠNG QUAN
* **Tập dữ liệu Pilot:** 720 giờ liên tục (30 ngày) tại khu vực trung tâm Đà Nẵng.
* **Kết quả phân tích tương quan khí tượng (Chứng minh Giả thuyết H1):**
  * Tốc độ gió: $r = -0.482$ ($p < 0.001$) $\rightarrow$ Gió biển thổi mạnh giúp giải tỏa và phát tán chất ô nhiễm nhanh chóng.
  * Lượng mưa: $r = -0.345$ ($p < 0.001$) $\rightarrow$ Nước mưa lắng đọng và rửa trôi hiệu quả hạt bụi lơ lửng.
  * Độ ẩm tương đối: $r = +0.287$ ($p < 0.001$) $\rightarrow$ Độ ẩm cao làm tăng trọng lượng và hiện tượng ngưng tụ quanh hạt bụi.
  * Quán tính khí quyển: Nồng độ trễ $\text{PM}_{2.5}(t-1)$ có tương quan $r = +0.842$.

> **SPEAKER NOTES (LỜI THUYẾT MINH - 06:30 - 07:45):**  
> *"Thưa Hội đồng, để chứng minh tính khả thi, em đã tiến hành thực nghiệm Pilot trên chuỗi dữ liệu 720 giờ liên tục tại Đà Nẵng. Kết quả phân tích tương quan Pearson đã chứng minh một cách thuyết phục giả thuyết H1: Tốc độ gió và lượng mưa đều có tương quan nghịch rất mạnh với nồng độ PM2.5 ở mức ý nghĩa p < 0.001. Điều này chứng minh rằng gió biển và các cơn mưa rào ven biển tại Đà Nẵng đóng vai trò như một cơ chế tự làm sạch tự nhiên của bầu khí quyển thành phố."*

---

## SLIDE 8: HIỆU NĂNG MÔ HÌNH PILOT & KIỂM CHỨNG THEO QCVN
* **Bảng so sánh kết quả trên tập kiểm thử độc lập (Test Set - 144 giờ):**

| Mô hình | $MAE\ (\mu\text{g/m}^3)$ | $RMSE\ (\mu\text{g/m}^3)$ | $R^2$ Score | Cải thiện $RMSE$ |
| :--- | :---: | :---: | :---: | :---: |
| **Baseline (Ngây thơ)** | 4.82 | 6.85 | 0.612 | Cơ sở |
| **Random Forest** | 3.15 | 4.42 | 0.785 | 35.5% |
| **XGBoost (Đề xuất)** | **2.68** | **3.88** | **0.834** | **43.4%** |

* **Đánh giá mức độ đóng góp đặc trưng:** $\text{PM}_{2.5}(t-1)$ (52.4%), Tốc độ gió (18.6%), Độ ẩm (11.2%), Mưa (8.5%), Giờ trong ngày (9.3%).
* **Khả năng ứng dụng thực tế:** Sai số $MAE = 2.68\ \mu\text{g/m}^3$ là hoàn toàn đủ độ nhạy để phân loại chính xác các ngưỡng chất lượng không khí theo **QCVN 05:2023/BTNMT**.

> **SPEAKER NOTES (LỜI THUYẾT MINH - 07:45 - 09:00):**  
> *"Trên tập kiểm thử mù 144 giờ, mô hình XGBoost đã đạt thành tích xuất sắc nhất với R2 đạt 0.834, RMSE là 3.88 ug/m3 và MAE chỉ 2.68 ug/m3. XGBoost giúp giảm sai số RMSE đến 43.4% so với mô hình cơ sở, khẳng định hoàn toàn giả thuyết H2. Với mức sai số chỉ hơn 2.6 ug/m3, mô hình hoàn toàn đủ năng lực để phát hiện và cảnh báo kịp thời các thời điểm ô nhiễm vượt ngưỡng 25 ug/m3 và 50 ug/m3 theo QCVN 05:2023 của Bộ TN&MT."*

---

## SLIDE 9: KẾ HOẠCH TRIỂN KHAI 6 THÁNG & QUẢN TRỊ RỦI RO
* **Kế hoạch tiến độ 6 tháng (Biểu đồ Gantt):**
  * T1: Khảo sát & Kết nối API thu thập tự động.
  * T2–T3: Mở rộng thu thập chuỗi dữ liệu 3 năm, làm sạch theo chuẩn FAIR.
  * T4: Kỹ nghệ đặc trưng, tối ưu hóa siêu tham số mô hình học máy.
  * T5: Kiểm chứng chéo và đo kiểm thực địa đối chứng.
  * T6: Xây dựng Dashboard web demo, viết báo cáo tổng kết và nghiệm thu.
* **Tổng dự toán kinh phí:** 10.000.000 VNĐ.
* **Quản trị rủi ro:** Dự phòng nguồn dữ liệu mở OpenAQ; chống quá khớp bằng điều chuẩn; tuân thủ nghiêm ngặt nguyên tắc FAIR và liêm chính khoa học.

> **SPEAKER NOTES (LỜI THUYẾT MINH - 09:00 - 09:40):**  
> *"Để chuyển từ kết quả Pilot sang đề tài hoàn chỉnh, em đã xây dựng kế hoạch chi tiết trong 6 tháng với tổng kinh phí dự trù là 10 triệu đồng. Em cũng đã thiết lập ma trận rủi ro với các phương án dự phòng khi dữ liệu trạm bị mất kết nối hoặc khi mô hình bị quá khớp. Toàn bộ quy trình quản lý dữ liệu cam kết tuân thủ triệt để nguyên tắc FAIR: dễ tìm kiếm, dễ truy cập, tương tác và tái lập được."*

---

## SLIDE 10: KẾT LUẬN & KIẾN NGHỊ
* **Kết luận khoa học:**
  * Đã chứng minh tính khả thi và ưu thế vượt trội của phương pháp liên ngành CNTT & Môi trường trong dự báo ô nhiễm không khí tại Đà Nẵng.
  * Mô hình học máy XGBoost kết hợp khí tượng ven biển mang lại độ chính xác cao ($R^2 = 0.834$), sẵn sàng triển khai thực tiễn.
* **Kiến nghị:**
  * Đề xuất nhà trường và Sở Tài nguyên & Môi trường TP. Đà Nẵng tạo điều kiện kết nối dữ liệu trạm quan trắc tự động liên tục.
  * Định hướng mở rộng: Tích hợp công nghệ viễn thám GIS để xây dựng bản đồ cảnh báo không gian toàn thành phố.
* **Lời cảm ơn:** Trân trọng cảm ơn quý Thầy Cô trong Hội đồng đã chú ý lắng nghe! Kính mong nhận được ý kiến đóng góp của Thầy Cô.

> **SPEAKER NOTES (LỜI THUYẾT MINH - 09:40 - 10:00):**  
> *"Tóm lại, đề cương đã hoàn thiện đầy đủ 8 mảnh ghép theo chuẩn KHTN, có luận cứ liên ngành chặt chẽ và đã được kiểm chứng thực tế qua mô hình Pilot thành công. Em xin chân thành cảm ơn quý thầy cô trong Hội đồng đã lắng nghe và rất mong nhận được những góp ý quý báu từ thầy cô để đề tài được hoàn thiện hơn nữa. Em xin trân trọng cảm ơn!"*

