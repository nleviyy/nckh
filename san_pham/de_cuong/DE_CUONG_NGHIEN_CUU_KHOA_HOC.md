# BỘ GIÁO DỤC VÀ ĐÀO TẠO - ĐẠI HỌC ĐÀ NẴNG
## TRƯỜNG ĐẠI HỌC SƯ PHẠM
### HỘI ĐỒNG KHOA HỌC VÀ ĐÀO TẠO
---

<br><br>

# THUYẾT MINH ĐỀ CƯƠNG ĐỀ TÀI NGHIÊN CỨU KHOA HỌC CẤP TRƯỜNG
*(DÀNH CHO NGHIÊN CỨU KHOA HỌC CỦA SINH VIÊN)*

<br>

## TÊN ĐỀ TÀI:
# NGHIÊN CỨU ỨNG DỤNG THUẬT TOÁN HỌC MÁY (MACHINE LEARNING) KẾT HỢP YẾU TỐ KHÍ TƯỢNG NHẰM DỰ BÁO NỒNG ĐỘ BỤI MỊN $\text{PM}_{2.5}$ TẠI THÀNH PHỐ ĐÀ NẴNG

<br>

* **Lĩnh vực nghiên cứu:** Liên ngành Công nghệ thông tin (Khoa học dữ liệu / AI) & Khoa học Môi trường
* **Chủ nhiệm đề tài:** [Họ và tên sinh viên] – Lớp: [Lớp sinh hoạt] – Khoa: Công nghệ thông tin
* **Giảng viên hướng dẫn:** [Họ và hàm học vị GVHD]
* **Thời gian thực hiện dự kiến:** 06 tháng (Từ tháng 01/2027 đến tháng 06/2027)
* **Địa điểm triển khai:** Thành phố Đà Nẵng

<br><br>
---
**Đà Nẵng, Năm 2026**

\newpage

# THÔNG TIN CHUNG VỀ ĐỀ TÀI

| Mục | Nội dung chi tiết |
| :--- | :--- |
| **1. Tên đề tài** | Nghiên cứu ứng dụng thuật toán học máy (Machine Learning) kết hợp yếu tố khí tượng nhằm dự báo nồng độ bụi mịn $\text{PM}_{2.5}$ tại thành phố Đà Nẵng |
| **2. Mã số đề tài** | [Phòng KH&HTQT cấp] |
| **3. Lĩnh vực KH&CN** | Liên ngành: Khoa học tự nhiên (Khoa học môi trường) & Kỹ thuật - Công nghệ (Công nghệ thông tin) |
| **4. Loại hình nghiên cứu** | Nghiên cứu ứng dụng (Applied Research) & Triển khai thực nghiệm (Experimental Development) |
| **5. Thời gian thực hiện** | 06 tháng |
| **6. Cơ quan chủ trì** | Trường Đại học Sư phạm – Đại học Đà Nẵng |
| **7. Đơn vị phối hợp** | Trung tâm Quan trắc Môi trường miền Trung / Trạm quan trắc địa phương |
| **8. Tổng kinh phí** | 10.000.000 VNĐ *(Mười triệu đồng chẵn)* |

---

# NỘI DUNG THUYẾT MINH ĐỀ CƯƠNG CHI TIẾT (8 MẢNH GHÉP)

## MẢNH GHÉP 1: TÍNH CẤP THIẾT CỦA ĐỀ TÀI VÀ LUẬN GIẢI TÍNH LIÊN NGÀNH
### 1.1. Tính cấp thiết
Bụi mịn $\text{PM}_{2.5}$ là tác nhân ô nhiễm không khí nguy hại hàng đầu tới sức khỏe con người do khả năng thâm nhập sâu vào phế nang và máu. Đà Nẵng đang hướng đến mục tiêu "Thành phố môi trường", song áp lực từ tốc độ gia tăng phương tiện giao thông cá nhân và hoạt động công nghiệp đang đe dọa chất lượng không khí đô thị. Hệ thống quan trắc tự động hiện tại chỉ phản ánh nồng độ hiện thời mà thiếu năng lực dự báo trước 1 đến 24 giờ. Dự báo sớm là chìa khóa để cơ quan quản lý điều tiết giao thông và người dân chủ động phòng ngừa rủi ro sức khỏe.

### 1.2. Luận giải tính liên ngành bắt buộc
* **Khoa học Môi trường (Cơ sở tự nhiên):** Cung cấp hiểu biết về cơ chế hóa khí quyển, bản chất nguồn phát thải và quy luật ảnh hưởng của các yếu tố khí tượng ven biển (gió biển, gió đất, độ ẩm, lượng mưa, hiện tượng nghịch nhiệt). Xác lập quy chuẩn đánh giá đối chứng theo QCVN 05:2023/BTNMT.
* **Công nghệ thông tin (Phương pháp và công cụ tính toán):** Cung cấp các thuật toán học máy giám sát (Random Forest, XGBoost), kỹ thuật xử lý dữ liệu lớn chuỗi thời gian, bù khuyết dữ liệu thông minh, trích xuất đặc trưng trễ tự động và tối ưu hóa siêu tham số.
* **Kết luận:** Nếu thiếu Khoa học Môi trường, mô hình CNTT sẽ biến thành "hộp đen" vô nghĩa về mặt vật lý. Nếu thiếu CNTT, Khoa học Môi trường không thể xử lý dữ liệu phi tuyến lớn theo thời gian thực với độ chính xác cao. Sự giao thoa là điều kiện tiên quyết để giải quyết bài toán.

---

## MẢNH GHÉP 2: TỔNG QUAN TÌNH HÌNH NGHIÊN CỨU VÀ KHOẢNG TRỐNG TRI THỨC
### 2.1. Tổng quan tình hình nghiên cứu
* **Trên thế giới:** Các công trình của Zheng et al. (2015), Huang & Kuo (2018), Gu et al. (2020) đã chứng minh các thuật toán học máy dạng cây (Tree-based Ensemble) và mạng nơ-ron hồi quy có khả năng dự báo ô nhiễm không khí vượt trội so với các mô hình phân tán số trị WRF-Chem truyền thống do không đòi hỏi đầu vào kiểm kê phát thải phức tạp.
* **Tại Việt Nam:** Các nghiên cứu của Pham et al. (2021) tại Hà Nội, Nguyen et al. (2022) tại TP. Hồ Chí Minh đã bắt đầu ứng dụng Deep Learning và Random Forest dự báo $\text{PM}_{2.5}$.
* **Khoảng trống tri thức (Knowledge Gap):**
  1. Chưa có công trình nào nghiên cứu bài bản mô hình học máy chuỗi thời gian thích ứng với **vi khí hậu ven biển nhiệt đới gió mùa tại Đà Nẵng**.
  2. Chưa có khung quy trình mở, mã nguồn mở có khả năng điền khuyết tự động dữ liệu cảm biến đo gián đoạn phục vụ các địa phương miền Trung.

---

## MẢNH GHÉP 3: CÂY MỤC TIÊU, CÂU HỎI VÀ GIẢ THUYẾT KHOA HỌC
### 3.1. Mục tiêu nghiên cứu
* **Mục tiêu chung:** Xây dựng khung mô hình học máy tích hợp tham số khí tượng dự báo chính xác nồng độ bụi $\text{PM}_{2.5}$ theo giờ tại thành phố Đà Nẵng.
* **Mục tiêu cụ thể 1:** Thu thập, chuẩn hóa chuỗi dữ liệu $\text{PM}_{2.5}$ và khí tượng; phân tích tương quan và kiểm định tác động của gió biển, lượng mưa.
* **Mục tiêu cụ thể 2:** Xây dựng, huấn luyện và tối ưu hóa thuật toán Random Forest và XGBoost; đánh giá sai số định lượng qua $RMSE, MAE, R^2$.
* **Mục tiêu cụ thể 3:** Thực hiện kiểm chứng pilot, đánh giá theo ngưỡng QCVN 05:2023/BTNMT và đề xuất giải pháp ứng dụng cảnh báo sớm cho Đà Nẵng.

### 3.2. Câu hỏi và giả thuyết khoa học
* **Câu hỏi 1:** Yếu tố vi khí tượng ven biển nào chi phối mạnh nhất đến nồng độ $\text{PM}_{2.5}$ tại Đà Nẵng?
  * *Giả thuyết 1:* Tốc độ gió và lượng mưa tương quan nghịch mạnh ($p < 0.05$) với $\text{PM}_{2.5}$ do quá trình xáo trộn cơ học và lắng đọng ướt.
* **Câu hỏi 2:** Thuật toán học máy nào phù hợp và đạt độ chính xác cao nhất cho dữ liệu chuỗi thời gian tại Đà Nẵng?
  * *Giả thuyết 2:* Thuật toán XGBoost đạt hiệu năng vượt trội ($R^2 > 0.80$, $RMSE$ thấp hơn 10% so với Random Forest) nhờ cơ chế kiểm soát điều chuẩn và tối ưu hóa hàm mất mát.

---

## MẢNH GHÉP 4: ĐỐI TƯỢNG, KHÁCH THỂ VÀ PHẠM VI NGHIÊN CỨU
* **Đối tượng:** Chuỗi thời gian nồng độ bụi mịn $\text{PM}_{2.5}$ ($\mu\text{g/m}^3$) và các thông số khí tượng bề mặt (nhiệt độ, độ ẩm, tốc độ gió, hướng gió, lượng mưa, áp suất khí quyển); các thuật toán học máy (RF, XGBoost).
* **Khách thể:** Chất lượng môi trường không khí xung quanh tại Đà Nẵng.
* **Phạm vi không gian:** Khu vực đô thị trung tâm thành phố Đà Nẵng.
* **Phạm vi thời gian:** Dữ liệu lịch sử 1–3 năm liên tục theo giờ; kế hoạch triển khai đề tài trong 06 tháng.

---

## MẢNH GHÉP 5: THIẾT KẾ VÀ PHƯƠNG PHÁP NGHIÊN CỨU LIÊN NGÀNH
### 5.1. Thiết kế nghiên cứu
Thiết kế nghiên cứu thực nghiệm số (Quantitative Experimental Design) trên chuỗi thời gian:
$$\text{Data Ingestion} \rightarrow \text{FAIR Preprocessing} \rightarrow \text{Feature Engineering} \rightarrow \text{ML Training (TimeSeriesSplit)} \rightarrow \text{Validation}$$

### 5.2. Phương pháp nghiên cứu cụ thể
1. **Phương pháp phân tích môi trường:** Phân tích tương quan Pearson/Spearman; phân loại chất lượng không khí theo thang đo chỉ số AQI và quy chuẩn QCVN 05:2023/BTNMT.
2. **Phương pháp tiền xử lý dữ liệu:** Lọc ngoại lai theo ngưỡng vật lý và $IQR$; nội suy tuyến tính điền khuyết chuỗi ngắn ($\le 3$h); điền trung bình trượt chuỗi dài; chuẩn hóa dữ liệu.
3. **Kỹ nghệ đặc trưng:** Tạo biến trễ ($t-1, t-2, t-24$), biến cửa sổ trượt (Rolling Mean 3h, 24h), biến tuần hoàn thời gian qua hàm $\sin/\cos$.
4. **Phương pháp mô hình hóa học máy:** Huấn luyện mô hình Random Forest Regressor và XGBoost Regressor; tối ưu hóa siêu tham số bằng tìm kiếm lưới (`GridSearchCV`) kết hợp kiểm định chéo chuỗi thời gian (`TimeSeriesSplit`).
5. **Đánh giá sai số:** Định lượng thông qua 3 chỉ số $MAE, RMSE, R^2$; phân tích độ không đảm bảo đo mở rộng $U_{95\%}$.

---

## MẢNH GHÉP 6: KẾ HOẠCH TRIỂN KHAI (GANTT 6 THÁNG) VÀ DỰ TRÙ KINH PHÍ
* **Tiến độ triển khai 6 tháng:**
  * Tháng 1: Khảo sát thực địa, thiết lập quy trình API thu thập dữ liệu.
  * Tháng 2 – 3: Thu thập dữ liệu lịch sử, làm sạch, tiền xử lý và phân tích tương quan EDA.
  * Tháng 4: Kỹ nghệ đặc trưng, huấn luyện mô hình RF và XGBoost, tối ưu siêu tham số.
  * Tháng 5: Đánh giá mô hình trên tập kiểm thử độc lập, kiểm chứng chéo, phân tích sai số.
  * Tháng 6: Viết báo cáo tổng kết, xây dựng giao diện demo trực quan và nghiệm thu đề tài.
* **Tổng dự toán kinh phí:** 10.000.000 VNĐ (Gồm: Thu thập dữ liệu & API: 2,5 triệu; Điện toán đám mây: 1,8 triệu; Khảo sát thực địa đối chứng: 2,2 triệu; In ấn & văn phòng phẩm: 1,5 triệu; Hội thảo & chuyên gia: 2,0 triệu).

---

## MẢNH GHÉP 7: PHÂN TÍCH RỦI RO, ĐẠO ĐỨC KHOA HỌC VÀ QUẢN TRỊ DỮ LIỆU FAIR
* **Ma trận rủi ro:**
  * *Rủi ro mất dữ liệu trạm:* Khắc phục bằng cơ chế thu thập đa nguồn mở (OpenAQ, trạm địa phương) và thuật toán điền khuyết thông minh.
  * *Rủi ro quá khớp (Overfitting):* Khắc phục bằng kỹ thuật điều chuẩn $\text{L}_1/\text{L}_2$ và kiểm định chéo `TimeSeriesSplit`.
* **Đạo đức nghiên cứu & Liêm chính:** Tuyệt đối không ngụy tạo dữ liệu; minh bạch mã nguồn mở (Open Source Code); cam đoan tuân thủ nguyên tắc FAIR (Dữ liệu Dễ tìm kiếm – Dễ truy cập – Tương thích – Tái sử dụng).

---

## MẢNH GHÉP 8: KẾT QUẢ THỬ NGHIỆM SƠ BỘ (PILOT STUDY) VÀ SẢN PHẨM DỰ KIẾN
### 8.1. Kết quả thực nghiệm sơ bộ (Pilot Study)
* Triển khai thử nghiệm trên tập dữ liệu 720 giờ liên tục tại Đà Nẵng.
* Đã chứng minh tương quan nghịch chặt chẽ giữa tốc độ gió ($r = -0.482$) và lượng mưa ($r = -0.345$) với nồng độ $\text{PM}_{2.5}$.
* Mô hình XGBoost đạt hiệu năng dự báo xuất sắc trên tập kiểm thử độc lập:
  $$R^2 = 0.834, \quad RMSE = 3.88\ \mu\text{g/m}^3, \quad MAE = 2.68\ \mu\text{g/m}^3$$
  Cải thiện 43.4% sai số so với mô hình cơ sở Baseline, khẳng định tính khả thi tuyệt đối của đề tài khi triển khai diện rộng.

### 8.2. Sản phẩm dự kiến bàn giao của đề tài
1. 01 Báo cáo tổng kết toàn văn đề tài nghiên cứu khoa học cấp trường.
2. 01 Bộ cơ sở dữ liệu chất lượng không khí và khí tượng Đà Nẵng đã chuẩn hóa theo chuẩn FAIR.
3. 01 Bộ mã nguồn hoàn chỉnh (Python Script & Jupyter Notebook) huấn luyện và dự báo $\text{PM}_{2.5}$.
4. 01 Ứng dụng web thử nghiệm (Dashboard) trực quan hóa kết quả dự báo thời gian thực.
5. 01 Bài báo khoa học đăng trên Tạp chí Khoa học & Giáo dục (ĐH Sư phạm - ĐH Đà Nẵng) hoặc kỷ yếu hội nghị chuyên ngành.

---

**XÁC NHẬN CỦA GIẢNG VIÊN HƯỚNG DẪN**  
*(Ký và ghi rõ họ tên)*

<br><br><br>

**CHỦ NHIỆM ĐỀ TÀI**  
*(Ký và ghi rõ họ tên)*

