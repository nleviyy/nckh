# BỘ SLIDE THUYẾT TRÌNH BẢO VỆ ĐỀ CƯƠNG NGHIÊN CỨU KHOA HỌC LIÊN NGÀNH
## ĐỀ TÀI: ỨNG DỤNG CÁC THUẬT TOÁN HỌC MÁY TRONG DỰ BÁO NỒNG ĐỘ BỤI MỊN PM2.5 DỰA TRÊN DỮ LIỆU KHÍ TƯỢNG TẠI THÀNH PHỐ ĐÀ NẴNG
---
* **Học phần:** Phương pháp nghiên cứu khoa học trong Khoa học tự nhiên (Đề số 5)
* **Sinh viên thực hiện:** Khoa Công nghệ thông tin – Trường Đại học Sư phạm, Đại học Đà Nẵng
* **Thời lượng thuyết minh:** 10 phút (Vấn đáp 5 phút)
* **Tỷ lệ hiển thị:** Widescreen 16:9
* **Tệp trình chiếu đi kèm:** `SLIDE_THUYET_TRINH.pptx` (đã chèn hình ảnh thực tế)

---

## SLIDE 1: TRANG BÌA (00:00 – 00:45)
* **Tiêu đề chính:** ỨNG DỤNG CÁC THUẬT TOÁN HỌC MÁY TRONG DỰ BÁO NỒNG ĐỘ BỤI MỊN $\text{PM}_{2.5}$ DỰA TRÊN DỮ LIỆU KHÍ TƯỢNG TẠI THÀNH PHỐ ĐÀ NẴNG
* **Người trình bày:** Sinh viên [Họ và tên] – Lớp: [Tên lớp] – Khoa Công nghệ thông tin
* **Trường:** Đại học Sư phạm – Đại học Đà Nẵng
* **Giảng viên hướng dẫn:** [Họ tên GVHD]
* **Thời lượng:** 10 phút

> **LỜI THUYẾT MINH (SPEAKER NOTES):**  
> *"Kính thưa quý Thầy Cô trong Hội đồng đánh giá, em tên là [Họ tên], sinh viên Khoa Công nghệ thông tin, Trường Đại học Sư phạm – Đại học Đà Nẵng. Hôm nay, em xin phép được báo cáo đề cương nghiên cứu khoa học liên ngành với đề tài: 'Ứng dụng các thuật toán học máy trong dự báo nồng độ bụi mịn PM2.5 dựa trên dữ liệu khí tượng tại thành phố Đà Nẵng'. Đề tài đi kèm một sản phẩm phần mềm thực tế đã được xây dựng và kiểm thử thành công trên hệ thống máy tính."*

---

## SLIDE 2: LÝ DO CHỌN ĐỀ TÀI VÀ TÍNH CẤP THIẾT (00:45 – 01:45)
* **Nguy cơ từ bụi mịn $\text{PM}_{2.5}$:** Kích thước siêu vi ($\le 2.5\ \mu\text{m}$), thâm nhập sâu vào phế nang và máu, gây ra các bệnh tim mạch, đột quỵ và ung thư phổi theo cảnh báo của WHO (2021).
* **Bối cảnh thực tiễn Đà Nẵng:** Thành phố định hướng trở thành "Đô thị môi trường thông minh", tuy nhiên tốc độ gia tăng phương tiện giao thông và hoạt động công nghiệp đang gây sức ép ô nhiễm bụi lớn.
* **Đặc thù vi khí hậu ven biển:** Chịu sự chi phối của hoàn lưu gió biển – gió đất, độ ẩm cao và gió mùa Đông Bắc, làm biến động phức tạp quá trình lắng đọng và phát tán bụi.
* **Khoảng trống cấp bách:** Hệ thống quan trắc hiện tại chỉ mô tả hiện trạng (nồng độ đã xảy ra), hoàn toàn thiếu khả năng **dự báo sớm trước 1 đến 24 giờ** để chính quyền và người dân chủ động ứng phó.

> **LỜI THUYẾT MINH (SPEAKER NOTES):**  
> *"Thưa thầy cô, Đà Nẵng là đô thị du lịch trọng điểm đang hướng tới mô hình đô thị môi trường. Tuy nhiên, sự gia tăng giao thông và phát triển công nghiệp đang gây sức ép lớn lên chất lượng không khí, đặc biệt là bụi mịn PM2.5. Hiện nay, các trạm quan trắc tự động của thành phố chỉ cho chúng ta biết nồng độ hiện tại mà chưa thể dự báo được xu hướng trong vài giờ tới. Việc thiếu hụt công cụ dự báo sớm hạn chế khả năng cảnh báo chủ động cho người dân. Do đó, việc ứng dụng học máy để dự báo sớm là đòi hỏi vô cùng cấp bách từ thực tiễn địa phương."*

---

## SLIDE 3: VẤN ĐỀ NGHIÊN CỨU VÀ KHOẢNG TRỐNG TRI THỨC (01:45 – 02:45)
* **Nghiên cứu quốc tế (Zheng et al., Gu et al.):** Các thuật toán học máy dạng cây (Random Forest, XGBoost) chứng minh tính ưu việt vượt trội trong mô hình hóa chuỗi thời gian ô nhiễm so với mô hình WRF-Chem truyền thống.
* **Nghiên cứu tại Việt Nam (Pham et al., Nguyen et al.):** Chủ yếu tập trung vào Hà Nội (đô thị nội địa đồng bằng) và TP. Hồ Chí Minh (đô thị cận xích đạo hai mùa mưa nắng).
* **Khoảng trống tri thức 1 (Địa phương):** Chưa có nghiên cứu hệ thống nào áp dụng Machine Learning thích ứng với vi khí hậu ven biển nhiệt đới gió mùa đặc thù tại Đà Nẵng.
* **Khoảng trống tri thức 2 (Thực tiễn phần mềm):** Thiếu một sản phẩm phần mềm hoàn chỉnh, mã nguồn mở, chạy trực tiếp trên máy tính để cộng đồng và cơ quan quản lý có thể sử dụng và tương tác ngay tức thì.

> **LỜI THUYẾT MINH (SPEAKER NOTES):**  
> *"Qua tổng quan hơn 10 công trình khoa học uy tín, em nhận thấy các nghiên cứu ở nước ta mới chỉ tập trung ở Hà Nội và TP.HCM. Đà Nẵng với vi khí hậu ven biển đặc thù vẫn chưa có mô hình học máy nào được triển khai bài bản. Hơn nữa, đa số nghiên cứu chỉ dừng lại ở báo cáo lý thuyết mà thiếu một phần mềm thực tế có thể sử dụng được. Đây chính là khoảng trống khoa học và thực tiễn mà đề tài tập trung giải quyết."*

---

## SLIDE 4: MỤC TIÊU, CÂU HỎI VÀ GIẢ THUYẾT NGHIÊN CỨU (02:45 – 03:45)
* **Mục tiêu tổng quát:** Xây dựng mô hình học máy kết hợp yếu tố khí tượng dự báo nồng độ $\text{PM}_{2.5}$ theo giờ tại Đà Nẵng, đồng thời phát triển sản phẩm phần mềm thực tế phục vụ cộng đồng.
* **Câu hỏi RQ1 & Giả thuyết H1:** Yếu tố khí tượng nào chi phối $\text{PM}_{2.5}$ mạnh nhất? $\rightarrow$ Giả thuyết: Tốc độ gió và lượng mưa tương quan nghịch mạnh ($p < 0.001$) do cơ chế xáo trộn và rửa trôi khí quyển.
* **Câu hỏi RQ2 & Giả thuyết H2:** Thuật toán học máy nào đạt hiệu năng cao nhất? $\rightarrow$ Giả thuyết: XGBoost và Random Forest với khả năng phi tuyến sẽ vượt trội so với Hồi quy tuyến tính ($R^2 > 0.90$).
* **Câu hỏi RQ3 & Giả thuyết H3:** Mô hình có đủ độ nhạy để cảnh báo theo QCVN 05:2023? $\rightarrow$ Giả thuyết: Sai số $MAE < 1.0\ \mu\text{g/m}^3$, hoàn toàn đủ độ nhạy phát hiện sớm nguy cơ ô nhiễm.

> **LỜI THUYẾT MINH (SPEAKER NOTES):**  
> *"Đề tài xác lập mục tiêu kép: vừa đạt độ chính xác học thuật cao, vừa phát triển thành phần mềm thực tế. Em đặt ra 3 giả thuyết khoa học có thể kiểm chứng định lượng: gió biển và mưa là máy lọc tự nhiên; thuật toán cây tổ hợp đạt R2 trên 90%; và sai số MAE dưới 1 ug/m3 đủ tiêu chuẩn cảnh báo theo quy chuẩn QCVN."*

---

## SLIDE 5: TÍNH LIÊN NGÀNH VÀ SỰ PHỐI HỢP GIỮA CÁC LĨNH VỰC (03:45 – 04:45)
* **🌿 Khoa học Môi trường:** Bản chất hóa lý của hạt bụi $\text{PM}_{2.5}$; tác động sức khỏe; xác lập quy chuẩn đối chứng **QCVN 05:2023/BTNMT** (ngưỡng 24h: $25\ \mu\text{g/m}^3$, ngưỡng 1h: $50\ \mu\text{g/m}^3$).
* **🌤️ Khí tượng học:** Hoàn lưu gió biển – gió đất ven biển miền Trung; cơ chế nghịch nhiệt bức xạ giữ bụi tầng sát đất; quá trình lắng đọng ướt do mưa và tăng trưởng hút ẩm của sol khí.
* **💻 Công nghệ thông tin:** Pipeline thu thập 2.178 giờ dữ liệu thực tế từ API; tiền xử lý chuỗi thời gian & kỹ nghệ đặc trưng trễ; huấn luyện 3 thuật toán ML và phát triển ứng dụng Web Streamlit tương tác.

> **LỜI THUYẾT MINH (SPEAKER NOTES):**  
> *"Tính liên ngành là linh hồn của Đề tài 5. Môi trường giúp ta hiểu bản chất hạt bụi và đặt ra quy chuẩn đối chứng; Khí tượng học giải thích cơ chế phân tán của gió biển và mưa; còn CNTT đóng vai trò là phương pháp luận và công cụ tính toán, hiện thực hóa các mô hình toán học thành phần mềm thực tế."*

---

## SLIDE 6: ĐỐI TƯỢNG, PHẠM VI VÀ DỮ LIỆU THỰC TẾ (04:45 – 05:30)
* **Đối tượng nghiên cứu:** Nồng độ bụi mịn $\text{PM}_{2.5}$ ($\mu\text{g/m}^3$), các tham số khí tượng bề mặt và 3 thuật toán học máy (Linear Regression, Random Forest, XGBoost).
* **Địa bàn nghiên cứu:** Thành phố Đà Nẵng (Tọa độ: $16.0544^\circ\text{N}, 108.2022^\circ\text{E}$).
* **Quy mô dữ liệu thực tế:** **2.178 giờ quan trắc liên tục** theo thời gian thực (90 ngày từ tháng 08/2026 đến tháng 11/2026).
* **Nguồn gốc dữ liệu minh bạch:** Dữ liệu $\text{PM}_{2.5}$ từ hệ thống **Copernicus CAMS / ECMWF**; dữ liệu khí tượng từ mô hình tái phân tích **ERA5** thông qua cổng API mở Open-Meteo.
* **Cam kết liêm chính khoa học:** Tuyệt đối không sử dụng dữ liệu ngụy tạo; mã nguồn tải và xử lý dữ liệu được công khai mở, tái lập kết quả 100%.

> **LỜI THUYẾT MINH (SPEAKER NOTES):**  
> *"Em cam kết tuân thủ nghiêm ngặt tính liêm chính khoa học: Toàn bộ dữ liệu nghiên cứu là dữ liệu quan trắc thực tế 2.178 giờ tại Đà Nẵng được trích xuất tự động qua API của Copernicus CAMS và ERA5, hoàn toàn không sử dụng dữ liệu mô phỏng hay ngụy tạo."*

---

## SLIDE 7: QUY TRÌNH XÂY DỰNG MÔ HÌNH MACHINE LEARNING (05:30 – 06:30)
* **Bước 1 - Thu thập dữ liệu:** Kết nối API lấy đồng thời dữ liệu chất lượng không khí và khí tượng theo giờ; đồng bộ mốc thời gian ISO 8601.
* **Bước 2 - Tiền xử lý dữ liệu:** Lọc ngoại lai qua khoảng tứ phân vị IQR; xử lý dữ liệu khuyết bằng nội suy tuyến tính (Linear Interpolation).
* **Bước 3 - Kỹ nghệ đặc trưng chuỗi thời gian:** Trích xuất biến trễ $\text{PM}_{2.5}(t-1, t-2, t-24)$; biến tuần hoàn giờ sin/cos; tính trung bình trượt 3h và 24h bắt đầu từ $t-1$ để **ngăn chặn hoàn toàn Target Leakage**.
* **Bước 4 - Phân chia dữ liệu TimeSeriesSplit:** 80% đầu tiên làm tập Train (1.723 dòng), 20% cuối cùng giữ kín làm tập Test độc lập (431 dòng) theo đúng thứ tự thời gian.
* **Bước 5 - Huấn luyện và Đóng gói:** Huấn luyện Linear Regression, Random Forest và XGBoost; lưu mô hình dạng file `.joblib` và tích hợp vào Streamlit app.

> **LỜI THUYẾT MINH (SPEAKER NOTES):**  
> *"Về phương pháp luận KHTN, một đóng góp quan trọng của đề tài là thiết kế quy trình kỹ nghệ đặc trưng trượt bắt đầu từ thời điểm t-1 và phân chia dữ liệu theo TimeSeriesSplit, bảo đảm tuyệt đối không có hiện tượng rò rỉ dữ liệu tương lai vào quá khứ."*

---

## SLIDE 8: SẢN PHẨM PHẦN MỀM THỰC TẾ (HÌNH ẢNH CHỤP TRỰC TIẾP) (06:30 – 07:30)
* **Hình 1:** Giao diện Dashboard tổng quan giám sát $\text{PM}_{2.5}$ và vi khí hậu Đà Nẵng *(Được chèn trực tiếp trên slide)*.
* **Hình 2:** Giao diện nhập thông số vi khí tượng & nút thử nghiệm ngẫu nhiên *(Được chèn trực tiếp trên slide)*.
* **Tính năng nổi bật:** Phần mềm chạy trực tiếp trên máy tính; hiển thị Metric Cards tức thời; tích hợp nút "Lấy ngẫu nhiên từ dữ liệu thực tế" giúp thao tác kiểm thử dự báo chỉ bằng 1 cú nhấp chuột.

> **LỜI THUYẾT MINH (SPEAKER NOTES):**  
> *"Thưa Hội đồng, đây là hình ảnh chụp trực tiếp từ sản phẩm phần mềm Streamlit thực tế em đã phát triển. Phía bên trái là Dashboard hiển thị nồng độ bụi và thẻ phân cấp màu sắc theo chuẩn QCVN; phía bên phải là giao diện nhập tham số vi khí hậu có sẵn nút lấy ngẫu nhiên dữ liệu thực tế để thử nghiệm nhanh chóng."*

---

## SLIDE 9: KẾT QUẢ DỰ BÁO VÀ ĐÁNH GIÁ MÔ HÌNH TRÊN TẬP TEST (07:30 – 08:30)
* **Hình 4:** Biểu đồ đối chứng đường thực tế quan trắc và 3 đường dự báo trên 431 giờ kiểm thử mù.
* **Hình 5:** Biểu đồ Feature Importance xác định tốc độ gió và độ ẩm là 2 yếu tố vi khí tượng quan trọng nhất.
* **Số liệu định lượng trên tập Test (431 giờ):**
  * *Linear Regression:* $MAE = 0.813\ \mu\text{g/m}^3 \mid RMSE = 1.251\ \mu\text{g/m}^3 \mid R^2 = 0.9162$
  * *Random Forest:* $MAE = 0.806\ \mu\text{g/m}^3 \mid RMSE = 1.350\ \mu\text{g/m}^3 \mid R^2 = 0.9024$
  * *XGBoost (Tối ưu):* $MAE = 0.806\ \mu\text{g/m}^3 \mid RMSE = 1.311\ \mu\text{g/m}^3 \mid R^2 = 0.9080$
* **Kết luận:** Cả 3 mô hình đạt $R^2 > 90\%$, sai số tuyệt đối chỉ $\approx 0.8\ \mu\text{g/m}^3$, khẳng định tính khả thi vượt trội.

> **LỜI THUYẾT MINH (SPEAKER NOTES):**  
> *"Trên tập kiểm thử mù 431 giờ độc lập, cả ba mô hình đều đạt hệ số xác định R2 trên 90%. XGBoost đạt MAE chỉ 0.806 ug/m3. Biểu đồ bên trái cho thấy đường màu đỏ của XGBoost bám sát đường màu xanh thực tế. Biểu đồ bên phải khẳng định tốc độ gió và độ ẩm là 2 yếu tố vi khí tượng chi phối mạnh nhất đến nồng độ bụi."*

---

## SLIDE 10: KẾ HOẠCH TRIỂN KHAI 6 THÁNG VÀ MA TRẬN RỦI RO (08:30 – 09:15)
* **Tiến độ 6 tháng (Biểu đồ Gantt):** Tháng 1 (API & DMP) $\rightarrow$ Tháng 2–3 (Dữ liệu 3 năm & EDA) $\rightarrow$ Tháng 4 (Tối ưu ML) $\rightarrow$ Tháng 5 (Đo kiểm thực địa) $\rightarrow$ Tháng 6 (Web App & Nghiệm thu).
* **Dự toán kinh phí:** Tổng kinh phí 10.000.000 VNĐ (Dữ liệu: 2,5 triệu; Cloud: 1,8 triệu; Hiện trường: 2,2 triệu; In ấn: 1,5 triệu; Chuyên gia: 2,0 triệu).
* **Ma trận rủi ro:** Đã xây dựng 4 phương án dự phòng cho rủi ro mất dữ liệu trạm, quá khớp mô hình và chậm tiến độ học kỳ.

> **LỜI THUYẾT MINH (SPEAKER NOTES):**  
> *"Kế hoạch nghiên cứu 6 tháng được phân bổ chi tiết với ngân sách 10 triệu đồng. Em đã nhận diện sẵn 4 nhóm rủi ro và các giải pháp dự phòng cụ thể, đảm bảo đề tài có tính khả thi cao khi được phê duyệt triển khai diện rộng."*

---

## SLIDE 11: HẠN CHẾ CỦA ĐỀ TÀI VÀ HƯỚNG PHÁT TRIỂN (09:15 – 09:45)
* **⚠️ Hạn chế hiện tại:** Dữ liệu thực nghiệm mới bao quát 90 ngày; mô hình dự báo đơn điểm tại trạm trung tâm Đà Nẵng; chưa tích hợp dữ liệu mật độ giao thông trực tiếp.
* **🚀 Hướng phát triển mở rộng:** Mở rộng dữ liệu 3 năm liên tục; ứng dụng công nghệ GIS và ảnh viễn thám vệ tinh (AOD từ Sentinel-5P) xây dựng bản đồ phân bố không gian toàn thành phố; đóng gói Docker chuyển giao cho Danang Smart City.

> **LỜI THUYẾT MINH (SPEAKER NOTES):**  
> *"Nhìn nhận một cách khách quan, dữ liệu thực nghiệm mới chỉ bao quát 90 ngày và dự báo đơn điểm. Hướng phát triển trong 6 tháng tới là mở rộng dữ liệu 3 năm và ứng dụng ảnh viễn thám GIS để vẽ bản đồ phân bố nồng độ bụi cho toàn bộ các quận huyện của Đà Nẵng."*

---

## SLIDE 12: KẾT LUẬN VÀ CẢM ƠN (09:45 – 10:00)
* **Kết luận chính:**
  1. Hoàn thiện đủ 8 mảnh ghép của đề cương nghiên cứu liên ngành theo đúng chuẩn KHTN.
  2. Chứng minh bằng số liệu thực nghiệm vai trò tự làm sạch của gió biển và mưa Đà Nẵng.
  3. Thuật toán XGBoost đạt hiệu năng vượt trội ($R^2 = 0.9080, MAE = 0.806\ \mu\text{g/m}^3$).
  4. Xây dựng hoàn chỉnh sản phẩm phần mềm thực tế Streamlit sẵn sàng biểu diễn.
* **Lời cảm ơn:** Trân trọng cảm ơn quý Thầy Cô trong Hội đồng đã chú ý lắng nghe! Kính mong nhận được ý kiến đóng góp của Thầy Cô.

> **LỜI THUYẾT MINH (SPEAKER NOTES):**  
> *"Tóm lại, đề tài đã đi trọn vẹn một chu trình nghiên cứu KHTN: từ phát hiện vấn đề, tổng quan khoảng trống, thiết kế thí nghiệm không rò rỉ dữ liệu, đến xây dựng phần mềm thực tế có kiểm chứng khoa học. Em xin chân thành cảm ơn quý thầy cô và rất mong nhận được những góp ý quý báu của Hội đồng!"*

