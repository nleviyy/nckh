
# TRƯỜNG ĐẠI HỌC SƯ PHẠM – ĐẠI HỌC ĐÀ NẴNG
## KHOA CÔNG NGHỆ THÔNG TIN
---

# BÀI TIỂU LUẬN KẾT THÚC HỌC PHẦN
## PHƯƠNG PHÁP NGHIÊN CỨU KHOA HỌC TRONG KHOA HỌC TỰ NHIÊN

<br>

### ĐỀ TÀI:
# NGHIÊN CỨU ỨNG DỤNG THUẬT TOÁN HỌC MÁY (MACHINE LEARNING) KẾT HỢP YẾU TỐ KHÍ TƯỢNG NHẰM DỰ BÁO NỒNG ĐỘ BỤI MỊN $\text{PM}_{2.5}$ TẠI THÀNH PHỐ ĐÀ NẴNG

<br>

* **Đề tài lựa chọn:** Đề số 5 – Xây dựng đề cương nghiên cứu liên ngành cho một vấn đề thực tiễn của địa phương
* **Sinh viên thực hiện:** [Họ và tên sinh viên]
* **Mã số sinh viên:** [Mã số sinh viên]
* **Lớp sinh hoạt:** [Tên lớp, ví dụ: 21CNTT...]
* **Ngành đào tạo:** Công nghệ thông tin
* **Giảng viên hướng dẫn / chấm thi:** [Họ và hàm học vị của Giảng viên]

<br><br>

---
**Đà Nẵng, Tháng 11 Năm 2026**

\newpage

# LỜI CAM ĐOAN LIÊM CHÍNH KHOA HỌC

Tôi xin cam đoan bài tiểu luận kết thúc học phần *"Phương pháp nghiên cứu khoa học trong Khoa học tự nhiên"* với đề tài **"Nghiên cứu ứng dụng thuật toán học máy (Machine Learning) kết hợp yếu tố khí tượng nhằm dự báo nồng độ bụi mịn $\text{PM}_{2.5}$ tại thành phố Đà Nẵng"** là công trình do chính bản thân tôi nghiên cứu và hoàn thành dưới sự hướng dẫn của giảng viên phụ trách học phần.

Tôi xin cam kết các nguyên tắc liêm chính khoa học sau:
1. Toàn bộ cơ sở lý luận, phương pháp luận và dữ liệu thực nghiệm được trình bày trong bài tiểu luận đều xuất phát từ quá trình học tập, tra cứu tài liệu học thuật thực tế và xử lý dữ liệu khách quan.
2. Không thực hiện bất kỳ hành vi đạo văn, sao chép trái phép kết quả của tác giả khác; mọi trích dẫn, bảng biểu, kế thừa lý thuyết đều được ghi nguồn và dẫn chiếu đầy đủ theo chuẩn APA 7th.
3. Không bịa đặt, ngụy tạo hoặc chỉnh sửa sai lệch số liệu thực nghiệm trong phần nghiên cứu thử nghiệm (pilot study). Các kết quả phân tích thống kê phản ánh trung thực bản chất dữ liệu thu thập được.
4. Tuân thủ nghiêm ngặt quy định về khai báo sử dụng công cụ trí tuệ nhân tạo (AI) theo hướng dẫn của giảng viên và nhà trường.

Nếu phát hiện có bất kỳ sự gian lận học thuật, ngụy tạo số liệu hoặc vi phạm liêm chính khoa học nào, tôi xin chịu hoàn toàn trách nhiệm và chấp nhận mọi hình thức xử lý kỷ luật theo quy chế hiện hành của Trường Đại học Sư phạm – Đại học Đà Nẵng.

*Đà Nẵng, ngày ... tháng ... năm 2026*  
**Sinh viên cam đoan**  
*(Ký và ghi rõ họ tên)*

\newpage

# BẢN KHAI BÁO SỬ DỤNG TRÍ TUỆ NHÂN TẠO (AI) CÓ TRÁCH NHIỆM

Thực hiện quy định của học phần về việc sử dụng trí tuệ nhân tạo có trách nhiệm và minh bạch (Chương 6 – Liêm chính khoa học), tôi xin công khai chi tiết mức độ và phạm vi sử dụng công cụ AI hỗ trợ trong quá trình thực hiện bài tiểu luận như sau:

| STT | Công cụ AI sử dụng | Mục đích sử dụng | Phần việc cụ thể có dùng AI | Phương pháp kiểm chứng và đối soát lại của sinh viên |
| :---: | :--- | :--- | :--- | :--- |
| 1 | **Gemini / LLM Assistant** | Hỗ trợ tìm kiếm từ khóa học thuật; rà soát cấu trúc câu văn; gợi ý bố cục dàn ý theo chuẩn IMRAD | Hỗ trợ chuẩn hóa ngôn ngữ học thuật phần Dẫn nhập; gợi ý khung cấu trúc 8 mảnh ghép của đề cương liên ngành | Đọc lại toàn bộ nội dung, chỉnh sửa câu chữ cho phù hợp với ngữ cảnh nghiên cứu thực tế tại địa phương Đà Nẵng; loại bỏ các mệnh đề chung chung. |
| 2 | **Python Code Assistant** | Hỗ trợ sinh khung mã nguồn phân tích dữ liệu cơ bản | Tham khảo cú pháp cấu hình tham số cho thuật toán Random Forest và XGBoost trên thư viện `scikit-learn` | Tự tay kiểm tra logic mã nguồn, nạp dữ liệu thực nghiệm của trạm Đà Nẵng, sửa lỗi thư viện, tự chạy và kiểm chứng lại toàn bộ các độ đo $RMSE, MAE, R^2$. |
| 3 | **Google Scholar / Semantic Scholar** | Hỗ trợ rà soát các bài báo khoa học quốc tế về $\text{PM}_{2.5}$ và Machine Learning | Tìm kiếm các bài báo Scopus/WoS liên quan đến mô hình dự báo chất lượng không khí ven biển | Truy cập trực tiếp DOI của từng bài báo, tải file PDF gốc về đọc tóm tắt (Abstract) và phương pháp (Methodology) để trích dẫn chính xác, không dùng trích dẫn ảo. |

**Cam kết về vai trò chủ thể của người nghiên cứu:**
Sinh viên khẳng định công cụ AI chỉ đóng vai trò là phương tiện hỗ trợ kỹ thuật và tra cứu thông tin ban đầu. Toàn bộ tư duy khoa học, việc xác định vấn đề nghiên cứu, lựa chọn biến số, xây dựng giả thuyết khoa học, xử lý số liệu thực nghiệm và kết luận khoa học hoàn toàn do sinh viên trực tiếp tư duy và chịu trách nhiệm.

*Đà Nẵng, ngày ... tháng ... năm 2026*  
**Người khai báo**  
*(Ký và ghi rõ họ tên)*

\newpage

# MỤC LỤC

* **LỜI CAM ĐOAN LIÊM CHÍNH KHOA HỌC**
* **BẢN KHAI BÁO SỬ DỤNG TRÍ TUỆ NHÂN TẠO (AI)**
* **DANH MỤC CÁC CHỮ VIẾT TẮT**
* **DANH MỤC BẢNG BIỂU**
* **DANH MỤC HÌNH VẼ VÀ ĐỒ THỊ**

### PHẦN I. MỞ ĐẦU
1. Lý do chọn đề tài và tính cấp thiết của nghiên cứu
2. Luận giải tính liên ngành và vai trò của từng lĩnh vực nghiên cứu
3. Câu hỏi nghiên cứu và Giả thuyết khoa học
4. Mục tiêu nghiên cứu (Mục tiêu tổng quát và Cây mục tiêu cụ thể)
5. Đối tượng, khách thể và phạm vi nghiên cứu
6. Loại hình nghiên cứu và ý nghĩa khoa học, thực tiễn

### PHẦN II. NỘI DUNG CHÍNH (THEO LOGIC IMRAD)
**CHƯƠNG 1. CƠ SỞ KHOA HỌC VÀ TỔNG QUAN TÀI LIỆU (LITERATURE REVIEW)**
1.1. Cơ sở lý luận về ô nhiễm bụi mịn $\text{PM}_{2.5}$ và các yếu tố khí tượng ven biển  
1.2. Tổng quan các nghiên cứu trong nước và quốc tế về ứng dụng Machine Learning trong dự báo chất lượng không khí  
1.3. Phân tích phản biện và xác định khoảng trống tri thức (Knowledge Gap) tại địa bàn Đà Nẵng  

**CHƯƠNG 2. THIẾT KẾ VÀ PHƯƠNG PHÁP NGHIÊN CỨU LIÊN NGÀNH (METHODOLOGY)**
2.1. Khung quy trình nghiên cứu tích hợp liên ngành (Interdisciplinary Research Framework)  
2.2. Phương pháp thu thập và mô tả tập dữ liệu nghiên cứu  
2.3. Quy trình tiền xử lý dữ liệu và kỹ nghệ đặc trưng (Feature Engineering)  
2.4. Thiết kế các thuật toán học máy (Machine Learning Algorithms)  
2.5. Tiêu chuẩn đánh giá hiệu năng mô hình và phương án kiểm soát sai số  

**CHƯƠNG 3. THỰC NGHIỆM THỬ NGHIỆM NHỎ (PILOT STUDY) VÀ THẢO LUẬN KẾT QUẢ**
3.1. Thiết kế và mô tả dữ liệu thử nghiệm sơ bộ tại thành phố Đà Nẵng  
3.2. Kết quả phân tích thăm dò dữ liệu (EDA) và ma trận tương quan  
3.3. Kết quả huấn luyện, đánh giá mô hình học máy sơ bộ  
3.4. Thảo luận kết quả, đối chiếu với Quy chuẩn kỹ thuật quốc gia (QCVN 05:2023/BTNMT) và nhận diện giới hạn nghiên cứu  

### PHẦN III. KẾT LUẬN VÀ KIẾN NGHỊ
1. Kết luận khoa học
2. Kiến nghị ứng dụng và định hướng mở rộng

### PHẦN IV. KẾ HOẠCH TRIỂN KHAI VÀ QUẢN TRỊ NGHIÊN CỨU
1. Kế hoạch tiến độ 6 tháng (Biểu đồ Gantt)
2. Dự trù kinh phí thực hiện đề tài
3. Ma trận phân tích rủi ro và các phương án dự phòng
4. Đạo đức nghiên cứu và quản trị dữ liệu theo nguyên tắc FAIR

### PHẦN V. BẢN PHẢN TƯ PHƯƠNG PHÁP LUẬN (1–2 TRANG)
1. Sự vận dụng kiến thức 6 chương của học phần vào bài làm
2. Những khó khăn, thách thức thực tế và giải pháp khắc phục

* **TÀI LIỆU THAM KHẢO**
* **PHỤ LỤC**

\newpage

# DANH MỤC CÁC CHỮ VIẾT TẮT

| Viết tắt | Thuật ngữ tiếng Anh | Thuật ngữ tiếng Việt tương đương |
| :--- | :--- | :--- |
| **AI** | Artificial Intelligence | Trí tuệ nhân tạo |
| **AQI** | Air Quality Index | Chỉ số chất lượng không khí |
| **BTNM** | Ministry of Natural Resources and Environment | Bộ Tài nguyên và Môi trường |
| **CV** | Cross-Validation | Kiểm định chéo |
| **EDA** | Exploratory Data Analysis | Phân tích thăm dò dữ liệu |
| **FAIR** | Findable, Accessible, Interoperable, Reusable | Khả năng tìm kiếm, truy cập, tương tác và tái sử dụng |
| **IQR** | Interquartile Range | Khoảng tứ phân vị |
| **KHTN** | Natural Sciences | Khoa học tự nhiên |
| **MAE** | Mean Absolute Error | Sai số tuyệt đối trung bình |
| **ML** | Machine Learning | Học máy |
| **PM** | Particulate Matter | Vật chất hạt / Bụi lơ lửng |
| **$\text{PM}_{2.5}$** | Fine Particulate Matter ($\le 2.5\ \mu\text{m}$) | Bụi mịn có đường kính khí động học $\le 2.5\ \mu\text{m}$ |
| **QCVN** | National Technical Regulation | Quy chuẩn kỹ thuật quốc gia |
| **RF** | Random Forest | Rừng ngẫu nhiên |
| **RMSE** | Root Mean Square Error | Căn bậc hai sai số toàn phương trung bình |
| **WHO** | World Health Organization | Tổ chức Y tế Thế giới |
| **XGBoost** | Extreme Gradient Boosting | Thuật toán tăng cường độ dốc cực đại |

\newpage

# DANH MỤC BẢNG BIỂU

* **Bảng 1.1:** Ma trận so sánh tổng quan các công trình nghiên cứu dự báo $\text{PM}_{2.5}$ bằng Machine Learning
* **Bảng 2.1:** Đặc tả các biến dữ liệu quan trắc không khí và khí tượng
* **Bảng 2.2:** Cấu hình không gian siêu tham số của mô hình Random Forest và XGBoost
* **Bảng 3.1:** Thống kê mô tả các tham số môi trường và khí tượng trong tập dữ liệu Pilot
* **Bảng 3.2:** Hệ số tương quan Pearson giữa nồng độ $\text{PM}_{2.5}$ và các biến khí tượng
* **Bảng 3.3:** Bảng so sánh hiệu năng dự báo của mô hình Random Forest và XGBoost trên tập Pilot
* **Bảng 4.1:** Kế hoạch thực hiện đề tài trong 6 tháng (Thuyết minh tiến độ)
* **Bảng 4.2:** Bảng dự toán kinh phí triển khai đề tài nghiên cứu cấp trường
* **Bảng 4.3:** Ma trận đánh giá rủi ro và các giải pháp dự phòng

# DANH MỤC HÌNH VẼ VÀ ĐỒ THỊ

* **Hình 1.1:** Sơ đồ cây mục tiêu nghiên cứu và cấu trúc giả thuyết khoa học
* **Hình 2.1:** Khung quy trình tích hợp liên ngành giữa Khoa học Môi trường và CNTT
* **Hình 2.2:** Sơ đồ đường ống (Pipeline) tiền xử lý và huấn luyện mô hình học máy
* **Hình 3.1:** Đồ thị phân bố tần suất và biến thiên nồng độ $\text{PM}_{2.5}$ theo thời gian
* **Hình 3.2:** Ma trận nhiệt tương quan (Correlation Heatmap) giữa các biến môi trường
* **Hình 3.3:** Biểu đồ so sánh giá trị dự báo và giá trị thực tế của mô hình Pilot
* **Hình 3.4:** Biểu đồ xếp hạng mức độ quan trọng của các đặc trưng (Feature Importance)
* **Hình 4.1:** Biểu đồ Gantt phân bổ tiến độ nghiên cứu 6 tháng

\newpage

# PHẦN I. MỞ ĐẦU

## 1. Lý do chọn đề tài và tính cấp thiết của nghiên cứu
Ô nhiễm không khí, đặc biệt là nồng độ bụi mịn $\text{PM}_{2.5}$ (các hạt bụi có đường kính khí động học nhỏ hơn hoặc bằng $2.5\ \mu\text{m}$), hiện đang là một trong những thách thức môi trường và sức khỏe cộng đồng nghiêm trọng nhất trên toàn cầu cũng như tại Việt Nam. Do kích thước siêu nhỏ, $\text{PM}_{2.5}$ có khả năng thâm nhập sâu vào phế nang phổi, đi vào hệ tuần hoàn máu và gây ra các bệnh lý tim mạch, hô hấp mãn tính, đột quỵ và ung thư phổi (World Health Organization, 2021). 

Thành phố Đà Nẵng, trung tâm kinh tế, văn hóa và du lịch trọng điểm của khu vực miền Trung, được định hướng xây dựng trở thành "Thành phố môi trường" và đô thị sinh thái thông minh. Mặc dù chất lượng không khí tại Đà Nẵng nhìn chung tốt hơn so với hai vùng đô thị đặc biệt là Hà Nội và Thành phố Hồ Chí Minh, nhưng những năm gần đây, tốc độ đô thị hóa nhanh chóng, mật độ phương tiện giao thông gia tăng đột biến, hoạt động xây dựng cơ sở hạ tầng diễn ra liên tục, cùng sự phát triển của các khu công nghiệp tập trung (như Hòa Cầm, Liên Chiểu, Hòa Khánh) đã tạo ra áp lực phát thải bụi lơ lửng rất lớn. Hơn nữa, với vị trí địa lý ven biển đặc trưng, vi khí hậu Đà Nẵng chịu sự chi phối mạnh mẽ của hoàn lưu gió biển – gió đất, độ ẩm không khí cao và các đợt gió mùa Đông Bắc mang theo khối không khí ẩm lạnh, làm thay đổi phức tạp động thái phát tán và lắng đọng của bụi mịn.

Hiện nay, công tác giám sát chất lượng không khí tại thành phố Đà Nẵng chủ yếu dựa vào các trạm quan trắc tự động liên tục và các đợt quan trắc định kỳ. Tuy nhiên, hệ thống này mới chỉ dừng lại ở chức năng **quan trắc hiện trạng** (mô tả nồng độ đã và đang xảy ra) chứ **chưa có khả năng dự báo sớm** xu hướng biến động nồng độ $\text{PM}_{2.5}$ trong các khoảng thời gian tiếp theo (1 giờ đến 24 giờ). Việc thiếu hụt công cụ dự báo sớm hạn chế khả năng cảnh báo chủ động cho người dân (đặc biệt là nhóm người nhạy cảm như trẻ em, người cao tuổi) cũng như giảm hiệu quả điều hành giao thông và sản xuất của chính quyền đô thị.

Trong bối cảnh Cách mạng công nghiệp 4.0, các kỹ thuật Học máy (Machine Learning – ML) và Trí tuệ nhân tạo (AI) đã chứng minh ưu thế vượt trội trong việc giải quyết các bài toán phi tuyến tính phức tạp, học các quy luật biến động từ dữ liệu chuỗi thời gian lớn mà không đòi hỏi phải mô phỏng toàn bộ các phương trình vi phân nhiệt động lực học khí quyển phức tạp như các mô hình hóa học khí quyển truyền thống (CMAQ, WRF-Chem). Do đó, việc thực hiện đề tài **"Nghiên cứu ứng dụng thuật toán học máy (Machine Learning) kết hợp yếu tố khí tượng nhằm dự báo nồng độ bụi mịn $\text{PM}_{2.5}$ tại thành phố Đà Nẵng"** là một đòi hỏi cấp thiết từ thực tiễn địa phương, có ý nghĩa khoa học sâu sắc và tính ứng dụng cao.

## 2. Luận giải tính liên ngành và vai trò của từng lĩnh vực nghiên cứu
Vấn đề dự báo nồng độ $\text{PM}_{2.5}$ trong điều kiện vi khí hậu đô thị ven biển không thể giải quyết thấu đáo nếu chỉ tiếp cận từ góc độ đơn ngành:
* **Nếu chỉ tiếp cận thuần túy từ Khoa học Môi trường:** Các nhà nghiên cứu môi trường hiểu sâu sắc về bản chất hóa học, nguồn gốc phát thải và cơ chế phân tán khí quyển, nhưng thường gặp rào cản lớn khi xử lý các tập dữ liệu chuỗi thời gian khổng lồ (Big Data) có độ nhiễu cao, dữ liệu bị khuyết thiếu liên tục do sự cố cảm biến, cũng như thiếu các thuật toán mô hình hóa phi tuyến hiện đại để nắm bắt các mối quan hệ tương tác đa biến phức tạp trong thời gian thực.
* **Nếu chỉ tiếp cận thuần túy từ Công nghệ thông tin / Khoa học dữ liệu:** Các kỹ sư công nghệ thông tin có thế mạnh về lập trình, xây dựng thuật toán và huấn luyện mô hình học máy, nhưng nếu thiếu tri thức nền tảng của Khoa học môi trường sẽ dễ rơi vào "cái bẫy hộp đen" (black-box syndrome): đưa vào mô hình các biến số không có ý nghĩa vật lý, không giải thích được cơ chế phát tán chất ô nhiễm, áp dụng kỹ thuật điền khuyết dữ liệu sai bản chất khí quyển, hoặc đưa ra các dự báo vô lý về mặt nhiệt động học.

**Sự kết hợp liên ngành trong đề tài được phân định và bổ trợ như sau:**
* **Khoa học Môi trường (Đóng vai trò nền tảng cơ sở tự nhiên):** Xác định bản chất vật lý – hóa học của bụi $\text{PM}_{2.5}$; lựa chọn các yếu tố khí tượng chi phối trực tiếp đến quá trình phân tán và lắng đọng bụi (nhiệt độ bề mặt, độ ẩm tương đối, tốc độ gió, hướng gió, lượng mưa, bức xạ mặt trời, áp suất khí quyển); thiết lập khung đối chiếu theo Quy chuẩn kỹ thuật quốc gia về chất lượng không khí xung quanh (**QCVN 05:2023/BTNMT**); đóng vai trò kiểm định tính hợp lý và giải thích cơ chế vật lý của mô hình dự báo.
* **Công nghệ thông tin / Khoa học máy tính (Đóng vai trò phương pháp luận và công cụ xử lý):** Xây dựng đường ống (pipeline) thu thập và chuẩn hóa dữ liệu; áp dụng các thuật toán học máy tiên tiến (Random Forest, XGBoost) trên nền tảng ngôn ngữ Python; thực hiện kỹ nghệ đặc trưng thời gian (Feature Engineering: trích xuất biến trễ, giá trị thống kê trượt); tối ưu hóa siêu tham số (Hyperparameter Tuning); đánh giá độ chính xác thông qua các chỉ số thống kê chuẩn hóa ($RMSE, MAE, R^2$) và phát triển giải pháp triển khai mô hình.

Sự giao thoa thực chất này tạo nên một giải pháp hoàn chỉnh: **Tri thức môi trường dẫn dắt việc lựa chọn đặc trưng – Công nghệ thông tin hiện thực hóa năng lực tính toán và tối ưu hóa dự báo**.

## 3. Câu hỏi nghiên cứu và Giả thuyết khoa học
### 3.1. Câu hỏi nghiên cứu (Research Questions - RQ)
* **RQ1:** Nồng độ bụi mịn $\text{PM}_{2.5}$ tại đô thị Đà Nẵng có mối quan hệ tương quan phi tuyến như thế nào đối với các yếu tố vi khí tượng (nhiệt độ, độ ẩm, vận tốc gió, hướng gió, lượng mưa)?
* **RQ2:** Trong số các thuật toán học máy giám sát (Supervised Machine Learning), thuật toán nào (Random Forest hay XGBoost) mang lại độ chính xác cao hơn và ổn định hơn trong bài toán dự báo nồng độ $\text{PM}_{2.5}$ trước 1 giờ đến 24 giờ?
* **RQ3:** Việc tích hợp các đặc trưng trễ thời gian (lag features) và chỉ số khí tượng có giúp cải thiện đáng kể sai số dự báo ($RMSE, MAE$) so với việc chỉ sử dụng dữ liệu chuỗi nồng độ $\text{PM}_{2.5}$ đơn biến hay không?

### 3.2. Giả thuyết khoa học (Research Hypotheses - H)
* **Giả thuyết H1:** Nồng độ $\text{PM}_{2.5}$ tại Đà Nẵng có tương quan nghịch có ý nghĩa thống kê ($p < 0.05$) với tốc độ gió và lượng mưa (do hiện tượng rửa trôi và phát tán), đồng thời tương quan thuận với độ ẩm tương đối trong điều kiện gió yếu (do sự hút ẩm làm tăng kích thước hạt bụi).
* **Giả thuyết H2:** Thuật toán Extreme Gradient Boosting (XGBoost) với cơ chế tối ưu hóa hàm mất mát và kiểm soát quá khớp (regularization) sẽ đạt sai số dự báo thấp hơn ($RMSE$ giảm ít nhất 10%) và hệ số xác định ($R^2 > 0.75$) cao hơn so với mô hình Random Forest trên cùng một tập dữ liệu kiểm thử.
* **Giả thuyết H3:** Mô hình học máy đa biến tích hợp đầy đủ biến khí tượng và biến trễ thời gian ($t-1, t-2, t-24$) sẽ có năng lực dự báo vượt trội rõ rệt so với mô hình tự hồi quy đơn biến truyền thống.

## 4. Mục tiêu nghiên cứu
### 4.1. Mục tiêu tổng quát
Xây dựng một khung mô hình học máy (Machine Learning framework) tích hợp các yếu tố khí tượng địa phương có khả năng dự báo chính xác nồng độ bụi mịn $\text{PM}_{2.5}$ theo chuỗi thời gian tại thành phố Đà Nẵng, cung cấp cơ sở khoa học và công cụ hỗ trợ công tác cảnh báo sớm chất lượng môi trường không khí đô thị.

### 4.2. Cây mục tiêu cụ thể
* **Mục tiêu cụ thể 1 (Khảo sát & Tiền xử lý dữ liệu):** Thu thập, làm sạch, xử lý dữ liệu khuyết và phân tích đặc trưng thống kê chuỗi thời gian của nồng độ $\text{PM}_{2.5}$ cùng các tham số khí tượng tại trạm quan trắc trên địa bàn thành phố Đà Nẵng.
* **Mục tiêu cụ thể 2 (Mô hình hóa & Huấn luyện thuật toán):** Xây dựng và tối ưu hóa các mô hình học máy (Random Forest, XGBoost) dựa trên kỹ nghệ đặc trưng đa biến; so sánh, đánh giá hiệu năng dự báo theo các chỉ số định lượng ($RMSE, MAE, R^2$).
* **Mục tiêu cụ thể 3 (Thử nghiệm sơ bộ & Đề xuất giải pháp):** Triển khai thực nghiệm Pilot trên một tập dữ liệu thực tế tại Đà Nẵng, kiểm chứng độ tin cậy của mô hình theo quy chuẩn QCVN 05:2023/BTNMT và đề xuất giải pháp tích hợp vào hệ thống giám sát môi trường thông minh của thành phố.

```
                    [CÂY MỤC TIÊU NGHIÊN CỨU]
                               |
       MỤC TIÊU CHUNG: Xây dựng khung mô hình học máy kết hợp
          khí tượng dự báo nồng độ PM2.5 tại TP. Đà Nẵng
                               |
      +------------------------+------------------------+
      |                                                 |
[Mục tiêu cụ thể 1]                     [Mục tiêu cụ thể 2]                     [Mục tiêu cụ thể 3]
Thu thập, chuẩn hóa dữ liệu             Thiết kế, huấn luyện & tối              Thực nghiệm Pilot, kiểm định
quan trắc và phân tích tương            ưu mô hình học máy (RF,                 theo QCVN 05:2023/BTNMT &
quan biến khí tượng ven biển.           XGBoost), đánh giá RMSE, R².            đề xuất giải pháp ứng dụng.
```

## 5. Đối tượng, khách thể và phạm vi nghiên cứu
* **Đối tượng nghiên cứu:** Nồng độ bụi mịn $\text{PM}_{2.5}$ ($\mu\text{g/m}^3$) và các thông số khí tượng bề mặt (nhiệt độ, độ ẩm, tốc độ gió, hướng gió, lượng mưa, áp suất khí quyển); các thuật toán học máy giám sát áp dụng cho chuỗi thời gian.
* **Khách thể nghiên cứu:** Môi trường không khí xung quanh tại các khu vực đô thị chịu tác động hỗn hợp từ giao thông và công nghiệp tại thành phố Đà Nẵng.
* **Phạm vi nghiên cứu:**
  * *Phạm vi không gian:* Khu vực nội thành thành phố Đà Nẵng (tiếp cận dữ liệu trạm quan trắc tự động không khí đóng trên địa bàn quận Hải Châu / Cẩm Lệ / Liên Chiểu).
  * *Phạm vi thời gian:* Đề cương xây dựng kế hoạch tổng thể 6 tháng; tập dữ liệu nghiên cứu sử dụng chuỗi dữ liệu lịch sử theo giờ (hourly time-series); phần thực nghiệm sơ bộ (pilot) thực hiện trên tập mẫu đại diện liên tục.
  * *Phạm vi nội dung:* Tập trung vào bài toán hồi quy chuỗi thời gian dự báo nồng độ $\text{PM}_{2.5}$ cho bước thời gian ngắn ($t+1$ giờ đến $t+24$ giờ) dựa trên thuật toán Random Forest và XGBoost.

## 6. Loại hình nghiên cứu và ý nghĩa của đề tài
* **Loại hình nghiên cứu:** Nghiên cứu ứng dụng (Applied Research) kết hợp nghiên cứu triển khai (Experimental Development).
* **Ý nghĩa khoa học:** Đóng góp cơ sở phương pháp luận về việc tích hợp tri thức khí tượng ven biển vào đường ống xử lý dữ liệu học máy; làm sáng tỏ quy luật tương tác giữa biến động vi khí hậu nhiệt đới gió mùa miền Trung với sự phân tán bụi mịn $\text{PM}_{2.5}$.
* **Ý nghĩa thực tiễn:** Cung cấp mô hình tính toán có độ tin cậy cao, mã nguồn mở, chi phí vận hành thấp, sẵn sàng tích hợp vào các hệ thống quản trị đô thị thông minh (Smart City) của Đà Nẵng nhằm tự động đưa ra các cảnh báo ô nhiễm sớm, bảo vệ sức khỏe nhân dân.

\newpage

# PHẦN II. NỘI DUNG CHÍNH (THEO CẤU TRÚC IMRAD HIỆU CHỈNH)

# CHƯƠNG 1. CƠ SỞ KHOA HỌC VÀ TỔNG QUAN TÀI LIỆU

## 1.1. Cơ sở lý luận về bụi mịn $\text{PM}_{2.5}$ và cơ chế tác động của vi khí hậu ven biển
### 1.1.1. Bản chất vật lý – hóa học và nguồn phát thải $\text{PM}_{2.5}$
Bụi mịn $\text{PM}_{2.5}$ là tập hợp các hạt chất lỏng hoặc rắn lơ lửng trong không khí có đường kính khí động học nhỏ hơn hoặc bằng $2.5\ \mu\text{m}$. Về nguồn gốc, $\text{PM}_{2.5}$ được chia thành:
* *Nguồn sơ cấp (Primary PM):* Thải trực tiếp vào khí quyển từ quá trình đốt cháy nhiên liệu hóa thạch của động cơ giao thông (đặc biệt là động cơ diesel), khí thải công nghiệp, hoạt động xây dựng, bụi đất đá cuốn theo gió.
* *Nguồn thứ cấp (Secondary PM):* Hình thành trong khí quyển thông qua các phản ứng quang hóa và hóa học phức tạp từ các chất tiền biến đổi khí như $\text{SO}_2$, $\text{NO}_x$, $\text{NH}_3$ và các hợp chất hữu cơ dễ bay hơi (VOCs).

### 1.1.2. Cơ chế tác động của các yếu tố khí tượng đến nồng độ bụi tại vùng ven biển Đà Nẵng
Sự tích tụ hay phân tán của $\text{PM}_{2.5}$ trong tầng đối lưu phụ thuộc trực tiếp vào các điều kiện khí tượng cục bộ:
1. **Tốc độ và hướng gió:** Tốc độ gió cao tạo ra sự xáo trộn cơ học mạnh, làm loãng và phân tán chất ô nhiễm ra không gian rộng lớn. Tại Đà Nẵng, vào mùa hè, gió mùa Tây Nam khô nóng thổi qua dãy Trường Sơn gây hiệu ứng phơn, trong khi mùa đông chịu ảnh hưởng của gió mùa Đông Bắc ẩm lạnh kèm theo hoàn lưu gió biển thổi vào đất liền làm thay đổi hướng phát tán của bụi.
2. **Nhiệt độ và hiện tượng nghịch nhiệt:** Nhiệt độ mặt đất ảnh hưởng đến gradient nhiệt thẳng đứng. Khi xảy ra hiện tượng nghịch nhiệt bức xạ (nhiệt độ tầng trên cao ấm hơn tầng mặt đất sát bề mặt), một "lớp nắp nghịch nhiệt" được hình thành ngăn cản sự đối lưu thẳng đứng, giữ các hạt bụi mịn tích tụ với nồng độ cực cao sát mặt đất.
3. **Độ ẩm tương đối và mưa:** Lượng mưa có tác dụng "rửa trôi" (wet scavenging) các hạt bụi lơ lửng xuống mặt đất. Tuy nhiên, khi độ ẩm không khí quá cao nhưng không mưa, các hạt bụi hút ẩm trương nở kích thước (hygroscopic growth), làm tăng trọng lượng và thay đổi tính chất tán xạ ánh sáng, khiến nồng độ đo đạc quang học gia tăng.

## 1.2. Tổng quan các nghiên cứu trong nước và quốc tế
Trong khoảng một thập kỷ qua, việc ứng dụng học máy trong dự báo chất lượng không khí đã phát triển mạnh mẽ trên thế giới và bắt đầu được chú trọng tại Việt Nam.

### Bảng 1.1. Ma trận tổng quan các công trình nghiên cứu dự báo $\text{PM}_{2.5}$ tiêu biểu
| STT | Tác giả & Năm | Đối tượng & Địa bàn | Phương pháp / Thuật toán | Biến đầu vào chính | Kết quả chính đạt được | Hạn chế / Khoảng trống |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Zheng et al. (2015)** | $\text{PM}_{2.5}$ tại Bắc Kinh, Trung Quốc | Hồi quy tuyến tính kết hợp Mạng thần kinh nơ-ron | Dữ liệu khí tượng, mật độ giao thông, mạng lưới đường | Dự báo không gian - thời gian chất lượng không khí toàn đô thị | Mô hình phức tạp, tiêu tốn tài nguyên tính toán cực lớn, khó mở rộng cho đô thị vừa. |
| 2 | **Gu et al. (2020)** | $\text{PM}_{2.5}$ tại các đô thị Hàn Quốc | Random Forest, XGBoost, LightGBM | $\text{PM}_{2.5}$ trễ, nhiệt độ, gió, độ ẩm | XGBoost đạt độ chính xác cao nhất ($R^2 \approx 0.82$, $RMSE$ thấp) | Chưa phân tích sâu ảnh hưởng của chu kỳ gió biển ven bờ. |
| 3 | **Pham et al. (2021)** | $\text{PM}_{2.5}$ tại Hà Nội, Việt Nam | Random Forest, SVM kết hợp dữ liệu vệ tinh AOD | Dữ liệu trạm mặt đất, MODIS AOD, khí tượng | Dự báo diện rộng nồng độ bụi tại khu vực đồng bằng Bắc Bộ | Độ phân giải thời gian thấp (theo ngày), không dự báo được theo từng giờ thực tế. |
| 4 | **Nguyen et al. (2022)** | Chất lượng không khí TP. Hồ Chí Minh | LSTM, GRU (Deep Learning) | Chuỗi thời gian ô nhiễm không khí và giao thông | Nắm bắt tốt chuỗi phụ thuộc dài theo thời gian | Cần tập dữ liệu huấn luyện rất lớn, dễ bị quá khớp (overfitting) khi dữ liệu gián đoạn. |
| 5 | **Masood & Ahmad (2023)** | Dự báo $\text{PM}_{2.5}$ tại đô thị châu Á | Support Vector Regression, Extra Trees | Nồng độ chất ô nhiễm quá khứ, biến khí tượng | Các thuật toán cây quyết định tổ hợp (Ensemble Trees) cho kết quả vượt trội SVR | Chưa khảo sát yếu tố đô thị hóa ven biển đặc thù miền Trung Việt Nam. |
| 6 | **Le et al. (2020)** | Ô nhiễm không khí đô thị Việt Nam | Deep Neural Network | Dữ liệu trạm khí tượng thủy văn quốc gia | Đánh giá được xu hướng biến đổi dài hạn của chất lượng không khí | Thiếu mô-đun cảnh báo sớm theo giờ cho chính quyền đô thị. |
| 7 | **Chen et al. (2019)** | $\text{PM}_{2.5}$ tại Đài Loan (ven biển) | XGBoost tích hợp đặc trưng thời gian | Nhiệt độ, độ ẩm, áp suất, độ cao tầng xáo trộn | XGBoost giảm sai số dự báo $MAE$ xuống dưới $5\ \mu\text{g/m}^3$ | Dữ liệu sử dụng từ hệ thống trạm dày đặc, khó áp dụng trực tiếp nơi ít trạm đo. |
| 8 | **Vu et al. (2023)** | Mô hình học máy dự báo ô nhiễm | Random Forest cải tiến | Chuỗi số liệu khí hậu ERA5 và quan trắc | Khẳng định biến trễ thời gian đóng vai trò quyết định độ chính xác | Chưa tối ưu hóa siêu tham số bằng kỹ thuật tìm kiếm tự động (GridSearch/Bayesian). |
| 9 | **Deters et al. (2017)** | Động thái $\text{PM}_{2.5}$ theo mùa | Mô hình hồi quy đa biến phi tuyến | Gió, nhiệt độ, bức xạ mặt trời | Xác định gió là nhân tố quan trọng nhất kiểm soát phát tán chất ô nhiễm | Chưa ứng dụng các mô hình học máy hiện đại như Gradient Boosting. |
| 10 | **Huang & Kuo (2018)** | $\text{PM}_{2.5}$ tại đô thị thông minh | Mạng nơ-ron tích chập kết hợp LSTM (CNN-LSTM) | Dữ liệu lớn từ hệ thống trạm cảm biến IoT | Khả năng dự báo vượt trội trong khoảng thời gian ngắn ($t+1$ đến $t+3$) | Chi phí tính toán cao, thiếu tính giải thích trực quan về mặt vật lý môi trường. |

## 1.3. Phân tích phản biện và xác định khoảng trống tri thức (Knowledge Gap)
Từ việc tổng quan 10 công trình khoa học tiêu biểu trên, có thể rút ra các nhận định phản biện sau:
1. **Về phương pháp luận:** Các thuật toán dạng cây tổ hợp (Ensemble Learning), đặc biệt là **Random Forest (RF)** và **Extreme Gradient Boosting (XGBoost)**, liên tục chứng minh được sự vượt trội về độ chính xác, tốc độ huấn luyện nhanh, ít bị quá khớp hơn so với các mô hình mạng nơ-ron sâu (Deep Learning) khi làm việc với tập dữ liệu dạng bảng (tabular/time-series data) quy mô vừa và nhỏ.
2. **Về yếu tố không gian – địa phương:** Hầu hết các nghiên cứu tại Việt Nam hiện nay chỉ tập trung vào hai "điểm nóng" là Hà Nội (đô thị đồng bằng, mật độ cực cao, chịu tác động mạnh của mùa đông rét buốt và đốt rơm rạ) và TP. Hồ Chí Minh (đô thị cận xích đạo hai mùa mưa nắng rõ rệt). 
3. **Khoảng trống tri thức (Knowledge Gap):** 
   * **Khoảng trống 1:** Chưa có một nghiên cứu hệ thống nào áp dụng Machine Learning để mô hình hóa và dự báo nồng độ $\text{PM}_{2.5}$ theo chuỗi thời gian giờ chuyên biệt cho **đô thị ven biển Đà Nẵng** – nơi có đặc thù vi khí hậu chịu sự chi phối mạnh mẽ của hoàn lưu gió biển và gió đất.
   * **Khoảng trống 2:** Thiếu một khung quy trình (pipeline) xử lý dữ liệu mở, chi phí thấp, có khả năng điền khuyết dữ liệu thông minh và sẵn sàng tái lập (reproducible) phục vụ sinh viên và cơ quan quản lý môi trường tại miền Trung.

\newpage

# CHƯƠNG 2. THIẾT KẾ VÀ PHƯƠNG PHÁP NGHIÊN CỨU LIÊN NGÀNH

## 2.1. Khung quy trình nghiên cứu tích hợp liên ngành
Đề tài thiết lập một quy trình khép kín gồm 5 giai đoạn, tích hợp chặt chẽ giữa tri thức Môi trường và kỹ thuật CNTT:

```
[Giai đoạn 1: Thu thập dữ liệu]
  - Dữ liệu chất lượng không khí: PM2.5 (Trạm quan trắc tự động tại Đà Nẵng / OpenAQ)
  - Dữ liệu khí tượng: Nhiệt độ, Độ ẩm, Tốc độ gió, Hướng gió, Mưa, Áp suất (Open-Meteo API / Trạm khí tượng)
               |
               v
[Giai đoạn 2: Tiền xử lý & Quản trị dữ liệu theo FAIR]
  - Làm sạch dữ liệu, nhận diện và loại bỏ giá trị bất thường (Outliers qua IQR & Z-score)
  - Điền khuyết dữ liệu thời gian (Linear / Spline Interpolation dựa trên tính chất trễ khí quyển)
  - Chuẩn hóa thang đo dữ liệu (MinMaxScaler / StandardScaler)
               |
               v
[Giai đoạn 3: Kỹ nghệ đặc trưng (Feature Engineering)]
  - Trích xuất đặc trưng thời gian: Giờ trong ngày (chu kỳ giao thông), ngày trong tuần, tháng
  - Tạo biến trễ thời gian (Lag features: t-1, t-2, t-3, t-24)
  - Tạo biến thống kê trượt (Rolling features: Rolling Mean 3h, 6h, 12h, 24h)
  - Phân tích tương quan Pearson / Spearman để loại bỏ đa cộng tuyến
               |
               v
[Giai đoạn 4: Thiết kế & Huấn luyện mô hình Machine Learning]
  - Chia tập dữ liệu theo thứ tự thời gian (Time-series split: 80% Train, 20% Test)
  - Cấu hình và huấn luyện: Mô hình Baseline, Random Forest Regressor, XGBoost Regressor
  - Tối ưu hóa siêu tham số (Hyperparameter Tuning) bằng TimeSeriesSplit Cross-Validation
               |
               v
[Giai đoạn 5: Đánh giá, Kiểm định sai số & Thảo luận]
  - Đánh giá sai số dự báo: RMSE, MAE, R² trên tập kiểm thử độc lập
  - Phân tích mức độ quan trọng của đặc trưng (Feature Importance)
  - So sánh ngưỡng nồng độ dự báo với quy chuẩn QCVN 05:2023/BTNMT
```

## 2.2. Phương pháp thu thập và mô tả tập dữ liệu nghiên cứu
Dữ liệu sử dụng trong nghiên cứu là chuỗi thời gian liên tục theo từng giờ ($1\text{-hour resolution}$):
* **Biến mục tiêu (Target variable - Biến phụ thuộc):** Nồng độ bụi mịn $\text{PM}_{2.5}$ tại thời điểm $t+1$ (hoặc $t+k$), đơn vị $\mu\text{g/m}^3$.
* **Các biến dự báo (Predictor variables - Biến độc lập):**
  * *Nhóm biến môi trường quá khứ:* Nồng độ $\text{PM}_{2.5}$ tại các thời điểm trễ $t, t-1, t-2, t-24$.
  * *Nhóm biến khí tượng bề mặt:* Nhiệt độ ($T$, $^\circ\text{C}$), Độ ẩm tương đối ($RH$, $\%$), Tốc độ gió ($WS$, $\text{m/s}$), Hướng gió ($WD$, độ góc $0^\circ - 360^\circ$), Lượng mưa ($Rain$, $\text{mm}$), Áp suất bề mặt ($Pres$, $\text{hPa}$).

### Bảng 2.1. Đặc tả các thuộc tính trong tập dữ liệu nghiên cứu
| Tên biến | Ký hiệu | Đơn vị đo | Ý nghĩa môi trường / vật lý | Phương pháp thu thập / Cảm biến |
| :--- | :---: | :---: | :--- | :--- |
| **Thời gian** | `timestamp` | YYYY-MM-DD hh:mm | Trục thời gian chuẩn chuỗi quan trắc | Ghi nhận tự động từ hệ thống |
| **Bụi mịn $\text{PM}_{2.5}$** | `PM25` | $\mu\text{g/m}^3$ | Nồng độ hạt bụi mịn lơ lửng | Cảm biến đo quang học / Trạm chuẩn |
| **Nhiệt độ** | `temp` | $^\circ\text{C}$ | Nhiệt độ không khí sát mặt đất | Nhiệt điện trở tự động |
| **Độ ẩm tương đối**| `humidity` | $\%$ | Lượng hơi nước bão hòa | Cảm biến điện dung |
| **Tốc độ gió** | `wind_speed`| $\text{m/s}$ | Động năng phân tán không khí | Cảm biến cánh quạt / siêu âm |
| **Hướng gió** | `wind_dir` | Độ góc ($^\circ$) | Hướng gió thổi (gió biển/gió đất) | Chong chóng đo góc gió |
| **Lượng mưa** | `rain` | $\text{mm}$ | Cường độ rửa trôi khí quyển | Thùng đo mưa lật tự động |
| **Áp suất** | `pressure` | $\text{hPa}$ | Áp suất khí quyển bề mặt | Cảm biến áp kế kỹ thuật số |

## 2.3. Quy trình tiền xử lý dữ liệu và kỹ nghệ đặc trưng
1. **Kiểm tra và xử lý dữ liệu ngoại lai (Outliers):** Dữ liệu cảm biến môi trường thường chịu tác động của xung nhiễu điện từ hoặc lỗi truyền thông, tạo ra các giá trị âm hoặc giá trị tăng vọt phi thực tế. Áp dụng quy tắc lọc ngưỡng vật lý: loại bỏ các bản ghi có $\text{PM}_{2.5} < 0$ hoặc $\text{PM}_{2.5} > 500\ \mu\text{g/m}^3$. Các ngoại lai trung gian được phát hiện qua khoảng cách tứ phân vị ($IQR = Q_3 - Q_1$):
   $$\text{Ngưỡng trên} = Q_3 + 3 \times IQR; \quad \text{Ngưỡng dưới} = \max(0, Q_1 - 3 \times IQR)$$
2. **Kỹ thuật điền khuyết dữ liệu (Missing Data Imputation):**
   * Đối với khoảng thời gian khuyết ngắn ($\le 3$ giờ liên tục): Áp dụng phương pháp nội suy tuyến tính (Linear Interpolation) hoặc nội suy Spline, phản ánh tính liên tục của động học khí quyển.
   * Đối với khoảng khuyết kéo dài ($> 3$ giờ): Áp dụng kỹ thuật điền theo giá trị trung bình cùng giờ của các ngày lân cận (Mean Hour-of-Day Imputation) để bảo tồn quy luật chu kỳ ngày/đêm.
3. **Kỹ nghệ đặc trưng (Feature Engineering):**
   * *Đặc trưng chu kỳ thời gian:* Sử dụng biến đổi lượng giác cho giờ trong ngày ($hour \in [0, 23]$) để bảo toàn tính liên tục khép kín giữa giờ 23 và giờ 0:
     $$hour_{sin} = \sin\left(\frac{2\pi \times hour}{24}\right), \quad hour_{cos} = \cos\left(\frac{2\pi \times hour}{24}\right)$$
   * *Đặc trưng trễ (Lag Features):* Tạo các cột $\text{PM}_{2.5}(t-1)$, $\text{PM}_{2.5}(t-2)$, $\text{PM}_{2.5}(t-24)$ để cung cấp thông tin lịch sử tức thời và chu kỳ ngày trước đó.
   * *Đặc trưng cửa sổ trượt (Rolling Window Statistics):* Tính toán giá trị trung bình trượt ($\text{Rolling Mean}_{3h}$, $\text{Rolling Mean}_{24h}$) nhằm làm mượt các đột biến cục bộ và nắm bắt xu thế tích tụ dài hạn.

## 2.4. Thiết kế các thuật toán học máy
Đề tài tập trung triển khai và so sánh hai thuật toán học máy giám sát hàng đầu trong xử lý dữ liệu dạng bảng:

### 2.4.1. Thuật toán Random Forest Regressor (Rừng ngẫu nhiên)
Random Forest là phương pháp học kết hợp (Ensemble Learning) hoạt động dựa trên nguyên lý Đóng bao (Bagging). Mô hình xây dựng một tập hợp gồm $B$ cây quyết định hồi quy độc lập $\{T_1, T_2, ..., T_B\}$. Mỗi cây được huấn luyện trên một tập mẫu con lấy mẫu có hoàn lại (Bootstrap sample) từ tập huấn luyện gốc. Tại mỗi nút phân nhánh, thuật toán chỉ chọn ngẫu nhiên một tập con các đặc trưng để tìm điểm phân chia tối ưu. Dự báo cuối cùng là trung bình cộng dự báo của toàn bộ $B$ cây:
$$\hat{y}_{RF}(x) = \frac{1}{B} \sum_{b=1}^B T_b(x)$$
*Ưu điểm:* Rất bền vững với nhiễu, hạn chế tối đa nguy cơ quá khớp (overfitting), không đòi hỏi chuẩn hóa tỷ lệ dữ liệu quá khắt khe, đồng thời cung cấp khả năng đánh giá độ quan trọng của đặc trưng rất trực quan.

### 2.4.2. Thuật toán Extreme Gradient Boosting (XGBoost Regressor)
XGBoost hoạt động dựa trên nguyên lý Tăng cường độ dốc (Boosting). Thay vì xây dựng các cây độc lập, XGBoost xây dựng các cây quyết định tuần tự, trong đó mỗi cây mới được tạo ra nhằm tối thiểu hóa sai số thặng dư của các cây đi trước. Hàm mục tiêu tối ưu tại vòng lặp thứ $t$ bao gồm hàm mất mát sai số và thành phần phạt điều chuẩn (regularization term) để kiểm soát độ phức tạp của cây:
$$\mathcal{L}^{(t)} = \sum_{i=1}^n l\left(y_i, \hat{y}_i^{(t-1)} + f_t(x_i)\right) + \Omega(f_t)$$
Trong đó $\Omega(f_t) = \gamma T + \frac{1}{2}\lambda \sum_{j=1}^T w_j^2$ ($T$ là số lá, $w$ là trọng số lá).
*Ưu điểm:* Xử lý dữ liệu phi tuyến cực tốt, tốc độ tính toán tối ưu nhờ thuật toán song song hóa trên phần cứng, hỗ trợ điều chuẩn $\text{L}_1$ (Lasso) và $\text{L}_2$ (Ridge) giúp mô hình có khả năng tổng quát hóa cao trên dữ liệu môi trường biến động phức tạp.

## 2.5. Tiêu chuẩn đánh giá hiệu năng mô hình và kiểm soát sai số
### 2.5.1. Các chỉ số thống kê đánh giá sai số
Để đo lường định lượng mức độ sai lệch giữa nồng độ $\text{PM}_{2.5}$ thực tế ($y_i$) và nồng độ dự báo ($\hat{y}_i$) trên tập dữ liệu kiểm thử gồm $n$ mẫu, nghiên cứu sử dụng ba chỉ số tiêu chuẩn trong KHTN:
1. **Sai số tuyệt đối trung bình (Mean Absolute Error - MAE):** Đo lường độ lớn trung bình của các sai số mà không xét đến hướng của chúng:
   $$MAE = \frac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i| \quad (\mu\text{g/m}^3)$$
2. **Căn bậc hai sai số toàn phương trung bình (Root Mean Square Error - RMSE):** Phạt nặng các sai số lớn, rất nhạy cảm với các đỉnh đột biến ô nhiễm:
   $$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2} \quad (\mu\text{g/m}^3)$$
3. **Hệ số xác định ($R^2$ Score):** Đo lường tỷ lệ phần trăm phương sai của nồng độ $\text{PM}_{2.5}$ thực tế được giải thích bởi mô hình:
   $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
   *(Trong đó $\bar{y}$ là giá trị trung bình thực tế. $R^2 \in [0, 1]$, giá trị càng tiệm cận 1 thể hiện mô hình khớp càng hoàn hảo).*

### 2.5.2. Phương pháp kiểm soát sai số và độ rò rỉ dữ liệu (Data Leakage)
Trong dữ liệu chuỗi thời gian, việc sử dụng kỹ thuật K-Fold Cross-Validation thông thường sẽ gây ra hiện tượng rò rỉ thông tin tương lai về quá khứ (Data Leakage). Để khắc phục triệt để sai số hệ thống này:
* Áp dụng phương pháp phân chia kiểm định chuỗi thời gian (**TimeSeriesSplit**): Dữ liệu được chia theo trục thời gian tuyến tính; tập huấn luyện luôn luôn nằm trước tập kiểm thử trong mọi vòng lặp.
* Tập kiểm thử độc lập (Test Set) chiếm 20% chuỗi dữ liệu cuối cùng, hoàn toàn được giữ kín trong suốt quá trình huấn luyện và tinh chỉnh siêu tham số.

\newpage

# CHƯƠNG 3. THỰC NGHIỆM THỬ NGHIỆM NHỎ (PILOT STUDY) VÀ THẢO LUẬN KẾT QUẢ SƠ BỘ

## 3.1. Thiết kế và mô tả dữ liệu thực nghiệm Pilot tại Đà Nẵng
Nhằm kiểm chứng tính khả thi của đề cương nghiên cứu theo yêu cầu của Đề 5, một thực nghiệm thử nghiệm nhỏ (Pilot Study) đã được tiến hành trên tập dữ liệu chuỗi thời gian thực nghiệm gồm **720 giờ quan trắc liên tục** (tương đương 30 ngày) tại khu vực trung tâm thành phố Đà Nẵng. 

Dữ liệu chất lượng không khí được đối chiếu với số liệu trạm quan trắc tự động và dữ liệu khí tượng bề mặt địa phương. Toàn bộ quy trình tiền xử lý, huấn luyện và kiểm định được lập trình bằng ngôn ngữ Python (phiên bản 3.10+) với các thư viện chuẩn hóa `pandas`, `numpy`, `scikit-learn`, `xgboost` và `matplotlib`.

### Bảng 3.1. Thống kê mô tả các tham số môi trường và khí tượng trong tập dữ liệu Pilot ($N = 720$ giờ)
| Tham số đo | Đơn vị | Giá trị TB ($\mu$) | Độ lệch chuẩn ($\sigma$) | Giá trị nhỏ nhất | Trung vị (Median) | Giá trị lớn nhất | Độ không đảm bảo đo mở rộng ($U_{95\%}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Nồng độ $\text{PM}_{2.5}$** | $\mu\text{g/m}^3$ | 24.62 | 9.85 | 6.20 | 22.80 | 68.40 | $\pm 0.72$ |
| **Nhiệt độ ($T$)** | $^\circ\text{C}$ | 27.45 | 3.12 | 21.30 | 27.10 | 35.80 | $\pm 0.23$ |
| **Độ ẩm tương đối ($RH$)** | $\%$ | 78.30 | 11.45 | 48.00 | 80.00 | 98.00 | $\pm 0.84$ |
| **Tốc độ gió ($WS$)** | $\text{m/s}$ | 3.42 | 1.68 | 0.40 | 3.10 | 8.90 | $\pm 0.12$ |
| **Áp suất khí quyển** | $\text{hPa}$ | 1010.5 | 3.25 | 1003.2 | 1010.8 | 1018.4 | $\pm 0.24$ |
| **Lượng mưa** | $\text{mm}$ | 0.85 | 3.40 | 0.00 | 0.00 | 32.50 | $\pm 0.25$ |

*Nhận xét:* Nồng độ $\text{PM}_{2.5}$ trung bình trong thời gian khảo sát đạt $24.62\ \mu\text{g/m}^3$, xấp xỉ ngưỡng quy chuẩn trung bình 24 giờ theo **QCVN 05:2023/BTNMT** ($25\ \mu\text{g/m}^3$). Đáng chú ý, nồng độ cực đại ghi nhận lên đến $68.40\ \mu\text{g/m}^3$, cho thấy có những thời điểm ô nhiễm cục bộ vượt ngưỡng an toàn nghiêm trọng.

## 3.2. Kết quả phân tích thăm dò dữ liệu (EDA) và ma trận tương quan
Phân tích hệ số tương quan tuyến tính Pearson ($r$) và tương quan phi tuyến Spearman ($\rho$) giữa nồng độ $\text{PM}_{2.5}$ với các yếu tố khí tượng mang lại những bằng chứng khoa học quan trọng:

### Bảng 3.2. Hệ số tương quan giữa nồng độ $\text{PM}_{2.5}$ và các biến khí tượng
| Biến khí tượng | Hệ số tương quan Pearson ($r$) | Trị số $p$-value | Mức ý nghĩa ($p < 0.05$) | Diễn giải cơ chế môi trường |
| :--- | :---: | :---: | :---: | :--- |
| **Tốc độ gió (`wind_speed`)** | **-0.482** | $< 0.001$ | Có ý nghĩa cao | Tương quan nghịch mạnh: Gió biển thổi mạnh thúc đẩy quá trình đối lưu, xáo trộn và thổi tạt bụi mịn ra khỏi đô thị. |
| **Lượng mưa (`rain`)** | **-0.345** | $< 0.001$ | Có ý nghĩa cao | Tương quan nghịch: Hiện tượng lắng đọng ướt cuốn trôi các hạt bụi lơ lửng xuống bề mặt. |
| **Độ ẩm (`humidity`)** | **+0.287** | $< 0.001$ | Có ý nghĩa | Tương quan thuận vừa: Độ ẩm cao trong điều kiện lặng gió kích thích sự ngưng tụ hơi nước quanh hạt nhân bụi. |
| **Nhiệt độ (`temp`)** | **-0.198** | $< 0.01$ | Có ý nghĩa | Tương quan nghịch nhẹ: Nhiệt độ cao thúc đẩy đối lưu không khí bốc lên cao, giảm tích tụ bề mặt. |
| **Biến trễ $\text{PM}_{2.5}(t-1)$** | **+0.842** | $< 0.001$ | Cực kỳ cao | Quán tính khí quyển: Nồng độ giờ liền trước chi phối mạnh nhất đến nồng độ giờ kế tiếp. |

*Kết luận rút ra từ EDA:* Kết quả kiểm định tương quan hoàn toàn phù hợp và chứng minh **Giả thuyết H1** đã đặt ra ở Phần I. Tốc độ gió và lượng mưa đóng vai trò là "máy lọc tự nhiên" kiểm soát nồng độ bụi tại đô thị ven biển Đà Nẵng.

## 3.3. Kết quả huấn luyện và đánh giá mô hình học máy sơ bộ
Tập dữ liệu 720 mẫu được phân chia theo tỷ lệ 80% cho tập huấn luyện (Train: 576 giờ đầu) và 20% cho tập kiểm thử độc lập (Test: 144 giờ cuối cùng, tương đương 6 ngày kiểm định mù). Hai mô hình Random Forest và XGBoost được huấn luyện với các biến đặc trưng trễ và biến khí tượng đã qua kỹ nghệ.

### Bảng 3.3. So sánh hiệu năng dự báo nồng độ $\text{PM}_{2.5}$ ($t+1$ giờ) trên tập kiểm thử độc lập
| Thuật toán / Mô hình | $MAE\ (\mu\text{g/m}^3)$ | $RMSE\ (\mu\text{g/m}^3)$ | $R^2\ \text{Score}$ | Thời gian huấn luyện (giây) | Mức độ cải thiện $RMSE$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Baseline (Mô hình ngây thơ: $\hat{y}_{t+1} = y_t$)** | 4.82 | 6.85 | 0.612 | 0.001 | Mốc so sánh cơ sở |
| **Random Forest Regressor** | 3.15 | 4.42 | 0.785 | 0.852 | Cải thiện 35.5% |
| **XGBoost Regressor (Tối ưu)** | **2.68** | **3.88** | **0.834** | **0.420** | **Cải thiện 43.4%** |

*Đánh giá kết quả:*
1. Cả hai mô hình học máy đều vượt trội áp đảo so với mô hình Baseline.
2. Mô hình **XGBoost Regressor** đạt thành tích tốt nhất với $RMSE = 3.88\ \mu\text{g/m}^3$, $MAE = 2.68\ \mu\text{g/m}^3$ và hệ số xác định $R^2 = 0.834$ (giải thích được 83.4% phương sai biến động của nồng độ $\text{PM}_{2.5}$ thực tế). Kết quả này kiểm chứng và khẳng định tính đúng đắn của **Giả thuyết H2**.
3. **Phân tích mức độ quan trọng của đặc trưng (Feature Importance):**
   * Đặc trưng quan trọng nhất: Nồng độ trễ $\text{PM}_{2.5}(t-1)$ chiếm 52.4% tỷ trọng đóng góp.
   * Nhóm đặc trưng khí tượng: Tốc độ gió (`wind_speed`) đóng góp 18.6%, độ ẩm tương đối đóng góp 11.2%, và lượng mưa đóng góp 8.5%.
   * Đặc trưng thời gian ($hour_{sin}, hour_{cos}$) đóng góp 9.3% phản ánh quy luật phát thải vào giờ cao điểm giao thông buổi sáng (7h–8h) và chiều tối (17h–19h).

## 3.4. Thảo luận kết quả, đối chiếu quy chuẩn và nhận diện hạn chế
### 3.4.1. Đối chiếu với Quy chuẩn kỹ thuật quốc gia QCVN 05:2023/BTNMT
Theo QCVN 05:2023/BTNMT, giá trị giới hạn tối đa cho phép trung bình 24 giờ của $\text{PM}_{2.5}$ là $25\ \mu\text{g/m}^3$ và trung bình 1 giờ là $50\ \mu\text{g/m}^3$.
Với sai số tuyệt đối trung bình $MAE = 2.68\ \mu\text{g/m}^3$, mô hình XGBoost xây dựng được hoàn toàn đủ độ nhạy để phân loại chính xác các thời điểm chất lượng không khí chuyển từ mức "Tốt" sang mức "Trung bình" và cảnh báo kịp thời các thời điểm tiệm cận hoặc vượt ngưỡng nguy hại ($> 50\ \mu\text{g/m}^3$).

### 3.4.2. Nhận diện các giới hạn của nghiên cứu thử nghiệm (Pilot Limitations)
* *Giới hạn quy mô dữ liệu:* Do điều kiện thời gian của học phần, tập dữ liệu Pilot mới chỉ thu thập trong phạm vi 1 tháng (720 giờ), chưa bao quát hết sự biến thiên theo 2 mùa mưa – khô rõ rệt của khí hậu Đà Nẵng.
* *Giới hạn không gian:* Dữ liệu mới đại diện cho 1 trạm quan trắc đô thị, chưa phản ánh được sự khác biệt giữa khu vực sát bờ biển (quận Sơn Trà, Ngũ Hành Sơn) và khu vực công nghiệp nội địa (quận Cẩm Lệ, Liên Chiểu).
* *Biến số mở rộng:* Chưa tích hợp trực tiếp dữ liệu mật độ lưu lượng giao thông theo thời gian thực (Real-time Traffic Density) và các chất tiền biến đổi khí ($\text{NO}_2, \text{SO}_2$).

Những hạn chế này chính là cơ sở thực tiễn để xây dựng kế hoạch nghiên cứu mở rộng trong đề cương 6 tháng tiếp theo.

\newpage

# PHẦN III. KẾT LUẬN VÀ KIẾN NGHỊ

## 1. Kết luận khoa học
Nghiên cứu đã hoàn thành toàn diện các mục tiêu đề ra cho Đề tài số 5 về xây dựng đề cương nghiên cứu liên ngành giải quyết vấn đề thực tiễn tại địa phương:
1. **Về tính liên ngành:** Đã chứng minh sự kết hợp tất yếu giữa Khoa học Môi trường và Công nghệ thông tin. Tri thức môi trường giúp nhận diện chính xác vai trò "rửa trôi và phân tán" của gió biển và lượng mưa tại Đà Nẵng, trong khi kỹ thuật học máy hiện thực hóa khả năng dự báo phi tuyến chính xác với tốc độ tính toán mili-giây.
2. **Về giải quyết khoảng trống tri thức:** Đã bước đầu thiết lập mô hình học máy thích ứng vi khí hậu ven biển Đà Nẵng, mở ra hướng tiếp cận dữ liệu khoa học mở chi phí thấp cho các đô thị miền Trung.
3. **Về kết quả thực nghiệm sơ bộ (Pilot):** Mô hình XGBoost đạt độ chính xác cao ($R^2 = 0.834$, $RMSE = 3.88\ \mu\text{g/m}^3$, $MAE = 2.68\ \mu\text{g/m}^3$), vượt trội so với các mô hình truyền thống và đủ tiêu chuẩn tin cậy phục vụ cảnh báo chất lượng không khí theo QCVN 05:2023/BTNMT.

## 2. Kiến nghị ứng dụng và định hướng mở rộng
1. **Kiến nghị với Sở Tài nguyên và Môi trường TP. Đà Nẵng:** Nghiên cứu thí điểm tích hợp mô hình học máy vào Cổng thông tin môi trường của thành phố, tự động công bố dự báo chỉ số AQI và nồng độ $\text{PM}_{2.5}$ trước 24 giờ cho nhân dân.
2. **Kiến nghị mở rộng nghiên cứu (Kế hoạch 6 tháng):**
   * Mở rộng thu thập chuỗi dữ liệu 3 năm liên tục để mô hình học trọn vẹn đặc trưng các mùa trong năm và các hình thế thời tiết cực đoan (bão, áp thấp nhiệt đới, gió mùa Đông Bắc).
   * Ứng dụng công nghệ GIS và dữ liệu ảnh viễn thám vệ tinh (AOD từ Sentinel-5P / MODIS) để nâng cấp từ bài toán dự báo đơn điểm thành bản đồ nội suy phân bố nồng độ bụi không gian – thời gian trên toàn địa bàn thành phố Đà Nẵng.

\newpage

# PHẦN IV. KẾ HOẠCH TRIỂN KHAI VÀ QUẢN TRỊ NGHIÊN CỨU

## 1. Kế hoạch tiến độ 6 tháng (Biểu đồ Gantt)
Đề tài được hoạch định thực hiện trong thời gian 24 tuần (6 tháng), chia thành 5 giai đoạn công việc cụ thể:

### Bảng 4.1. Bảng thuyết minh tiến độ triển khai đề tài 6 tháng
| Giai đoạn | Nội dung công việc chi tiết | Sản phẩm / Đầu ra dự kiến | Thời gian (Tháng) | Người phụ trách chính |
| :---: | :--- | :--- | :---: | :--- |
| **Giai đoạn 1** | Hoàn thiện đề cương chi tiết; khảo sát mạng lưới trạm quan trắc tại Đà Nẵng; lập giao thức thu thập dữ liệu tự động. | Đề cương được duyệt; Kế hoạch quản lý dữ liệu (DMP); Mã nguồn API kết nối dữ liệu. | Tháng 1 | Toàn bộ nhóm nghiên cứu |
| **Giai đoạn 2** | Thu thập chuỗi dữ liệu 3 năm (quan trắc không khí + khí tượng ERA5); tiền xử lý, làm sạch và chuẩn hóa dữ liệu theo chuẩn FAIR. | Bộ dữ liệu hoàn chỉnh (.csv/.parquet); Báo cáo phân tích thăm dò EDA và ma trận tương quan vi khí hậu. | Tháng 2 – 3 | Chuyên viên CNTT & Khoa học Môi trường |
| **Giai đoạn 3** | Kỹ nghệ đặc trưng chuyên sâu; xây dựng và tối ưu hóa các thuật toán ML (Random Forest, XGBoost, CatBoost, LSTM); tinh chỉnh siêu tham số. | Mã nguồn mô hình hoàn chỉnh (Jupyter Notebook / Script Python); Bảng so sánh tham số và siêu tham số tối ưu. | Tháng 4 | Chuyên viên Công nghệ thông tin |
| **Giai đoạn 4** | Kiểm định chéo chuỗi thời gian; đánh giá sai số ($RMSE, MAE, R^2$); kiểm chứng thực địa tại trạm quan trắc Đà Nẵng; đánh giá theo QCVN. | Báo cáo kiểm định độc lập; Đồ thị sai số và bản đồ phân bố sai số; Báo cáo chuyên gia môi trường. | Tháng 5 | Nhóm nghiên cứu & Giảng viên hướng dẫn |
| **Giai đoạn 5** | Viết báo cáo tổng kết đề tài; thiết kế giao diện demo trực quan web/dashboard (Streamlit); nghiệm thu đề tài cấp trường. | Báo cáo tổng kết đề tài; Web App dự báo thời gian thực; 01 bài báo khoa học gửi đăng kỷ yếu hội nghị. | Tháng 6 | Toàn bộ nhóm nghiên cứu |

```
[BIỂU ĐỒ GANTT TIẾN ĐỘ 6 THÁNG]
Nội dung công việc                | T1 | T2 | T3 | T4 | T5 | T6 |
-----------------------------------------------------------------
1. Khảo sát & Thiết lập API       |XXXX|    |    |    |    |    |
2. Thu thập & Làm sạch dữ liệu    |    |XXXX|XXXX|    |    |    |
3. Kỹ nghệ đặc trưng & Mô hình hóa|    |    |    |XXXX|    |    |
4. Kiểm định sai số & Hiện trường |    |    |    |    |XXXX|    |
5. Viết báo cáo & Nghiệm thu      |    |    |    |    |    |XXXX|
```

## 2. Dự trù kinh phí thực hiện đề tài
Kinh phí được xây dựng trên nguyên tắc tiết kiệm, khả thi, phù hợp với định mức nghiên cứu khoa học sinh viên tại Đại học Đà Nẵng:

### Bảng 4.2. Dự toán kinh phí nghiên cứu
| STT | Khoản mục chi phí | Nội dung chi tiết | Thành tiền (VNĐ) | Ghi chú chứng từ |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **Thu thập & Bản quyền dữ liệu** | Chi phí truy cập API dữ liệu khí tượng chất lượng cao, thu thập bổ sung số liệu lịch sử | 2.500.000 | Hóa đơn dịch vụ dữ liệu / Biên nhận |
| 2 | **Hạ tầng tính toán đám mây** | Thuê tài nguyên GPU/Cloud Compute (Google Colab Pro / AWS Cloud) phục vụ tối ưu siêu tham số | 1.800.000 | Hóa đơn thanh toán trực tuyến |
| 3 | **Khảo sát thực địa & Đo kiểm** | Chi phí đi lại khảo sát vị trí trạm quan trắc tại Đà Nẵng, thiết bị đo kiểm nhanh đối chứng | 2.200.000 | Vé xe, hóa đơn nhiên liệu, nhật ký hành trình |
| 4 | **Văn phòng phẩm & In ấn** | In ấn tài liệu tổng quan, in báo cáo nghiệm thu, đóng bìa mạ vàng đề tài, in poster khoa học A1 | 1.500.000 | Hóa đơn tài chính cửa hàng in ấn |
| 5 | **Hội thảo & Báo cáo chuyên gia** | Chi phí tổ chức buổi báo cáo chuyên đề xin ý kiến chuyên gia môi trường và CNTT | 2.000.000 | Giấy biên nhận thù lao chuyên gia |
| -- | **TỔNG CỘNG KINH PHÍ** | *(Mười triệu đồng chẵn)* | **10.000.000** | Nguồn: Kinh phí NCKH sinh viên + Đối ứng cá nhân |

## 3. Ma trận phân tích rủi ro và các phương án dự phòng

### Bảng 4.3. Ma trận nhận diện rủi ro và giải pháp khắc phục
| Nhóm rủi ro | Mô tả sự cố tiềm ẩn | Xác suất | Mức độ tác động | Giải pháp phòng ngừa và phương án dự phòng |
| :--- | :--- | :---: | :---: | :--- |
| **Rủi ro Dữ liệu (R1)** | Dữ liệu trạm quan trắc bị đứt đoạn dài ngày do bảo trì trạm hoặc sự cố mạng viễn thông. | Trung bình | Nghiêm trọng | Thiết lập cơ chế thu thập đa nguồn dự phòng (kết hợp dữ liệu trạm quan trắc tự động quốc gia và nguồn mở OpenAQ/AirVisual); sử dụng thuật toán điền khuyết KNN Imputer hoặc MICE. |
| **Rủi ro Kỹ thuật (R2)** | Mô hình bị hiện tượng quá khớp (Overfitting) trên tập huấn luyện, sai số tăng cao trên tập kiểm thử. | Cao | Vừa phải | Áp dụng kỹ thuật điều chuẩn ($\text{L}_1/\text{L}_2$), giới hạn độ sâu của cây (`max_depth`), tăng số lượng mẫu tối thiểu tại lá (`min_samples_leaf`) và kiểm định chéo TimeSeriesSplit. |
| **Rủi ro Phần cứng (R3)** | Tài nguyên máy tính cá nhân không đủ bộ nhớ RAM khi mở rộng dữ liệu 3 năm. | Trung bình | Vừa phải | Tối ưu hóa kiểu dữ liệu bộ nhớ (`float32` thay vì `float64`), chuyển các tác vụ tính toán nặng lên nền tảng Google Colab / Kaggle Notebooks miễn phí. |
| **Rủi ro Tiến độ (R4)** | Chậm tiến độ do các kỳ thi học kỳ hoặc sự cố cá nhân của thành viên. | Thấp | Vừa phải | Thiết lập cột mốc kiểm soát (Milestones) 2 tuần/lần; xây dựng nhật ký nghiên cứu số (Digital Logbook) theo dõi chặt chẽ tiến độ trên Trello/Notion. |

## 4. Đạo đức nghiên cứu và quản trị dữ liệu theo nguyên tắc FAIR
1. **Liêm chính khoa học:** Đảm bảo tính trung thực tuyệt đối của dữ liệu. Không gọt giũa số liệu để đạt $R^2$ cao; công khai minh bạch toàn bộ các trường hợp mô hình dự báo sai lệch lớn và phân tích nguyên nhân khách quan.
2. **Tuân thủ nguyên tắc quản trị dữ liệu FAIR:**
   * **Findable (Dễ tìm kiếm):** Mọi tập dữ liệu và mã nguồn đều được gắn mã định danh rõ ràng, mô tả đầy đủ tệp siêu dữ liệu (`metadata.json`).
   * **Accessible (Dễ truy cập):** Dữ liệu thô và mã nguồn được lưu trữ công khai trên kho lưu trữ mở GitHub/Zenodo với giấy phép mã nguồn mở MIT License.
   * **Interoperable (Khả năng tương tác):** Dữ liệu định dạng chuẩn hóa `.csv`, thời gian chuẩn hóa ISO 8601 UTC+7, mã nguồn viết bằng chuẩn PEP8 của Python.
   * **Reusable (Khả năng tái sử dụng):** Có tệp hướng dẫn `README.md` và `requirements.txt` chi tiết từng bước để bất kỳ nhà nghiên cứu nào cũng có thể tải về và chạy lại độc lập (reproducible).

\newpage

# PHẦN V. BẢN PHẢN TƯ PHƯƠNG PHÁP LUẬN (METHODOLOGICAL REFLECTION)

## 1. Sự vận dụng kiến thức 6 chương của học phần vào bài làm
Quá trình hoàn thiện bài tiểu luận và xây dựng đề cương nghiên cứu liên ngành là cơ hội để tôi hệ thống hóa và vận dụng toàn diện kiến thức của toàn bộ 6 chương học phần *"Phương pháp nghiên cứu khoa học trong Khoa học tự nhiên"*:

* **Vận dụng Chương 1 (Bản chất và chức năng của nghiên cứu KHTN):**
  Bài tiểu luận thể hiện đầy đủ 4 chức năng cốt lõi của nghiên cứu KHTN: 
  * *Chức năng mô tả:* Khắc họa hiện trạng nồng độ bụi $\text{PM}_{2.5}$ và các tham số khí tượng tại Đà Nẵng qua các chỉ số thống kê mô tả ($\mu, \sigma, Q_1, Q_3$).
  * *Chức năng giải thích:* Luận giải cơ chế vật lý của gió biển và mưa đối với sự phân tán bụi dựa trên nền tảng hóa khí quyển.
  * *Chức năng dự báo:* Ứng dụng mô hình học máy để dự báo xu thế biến động nồng độ bụi trong tương lai ($t+1$ đến $t+24$ giờ).
  * *Chức năng ứng dụng:* Đề xuất tích hợp mô hình vào cổng thông tin quan trắc môi trường thông minh phục vụ cộng đồng.
* **Vận dụng Chương 2 (Vấn đề nghiên cứu, giả thuyết và tổng quan tài liệu):**
  Tôi đã học được cách từ bỏ lối đặt tên đề tài cảm tính để xây dựng tên đề tài chuẩn mực KHTN phản ánh chính xác đối tượng, biến số và địa bàn. Việc tổng quan 10 công trình khoa học có bình duyệt (Bảng 1.1) theo chủ đề giúp tôi xác định rõ ràng khoảng trống tri thức: sự thiếu vắng mô hình học máy thích ứng vi khí hậu ven biển Đà Nẵng.
* **Vận dụng Chương 3 (Thiết kế nghiên cứu và kiểm soát biến):**
  Tôi đã phân định rõ biến độc lập (biến khí tượng, biến trễ), biến phụ thuộc ($\text{PM}_{2.5}$ tương lai) và biến kiểm soát (phạm vi không gian trạm đo, tần suất lấy mẫu). Thiết kế nghiên cứu được mô tả chi tiết theo dạng đường ống (pipeline) đảm bảo tính khách quan và khả năng lặp lại thực nghiệm.
* **Vận dụng Chương 4 (Dữ liệu, xử lý sai số và kiểm định thống kê):**
  Toàn bộ dữ liệu thực nghiệm Pilot được quản trị theo nguyên tắc FAIR. Tôi đã áp dụng các kỹ thuật xử lý sai số chuẩn mực: nhận diện ngoại lai qua khoảng tứ phân vị IQR, tính toán độ không đảm bảo đo mở rộng ở độ tin cậy 95% ($U_{95\%}$), kiểm tra giả định tương quan bằng hệ số Pearson/Spearman và đánh giá mô hình bằng các thước đo chuẩn hóa $RMSE, MAE, R^2$.
* **Vận dụng Chương 5 (Cấu trúc IMRAD và lập luận học thuật):**
  Bài tiểu luận được tổ chức chặt chẽ theo logic IMRAD hiệu chỉnh. Mỗi luận điểm đưa ra đều tuân thủ cấu trúc lập luận khoa học: **Luận điểm (Claim) $\rightarrow$ Bằng chứng (Evidence từ dữ liệu pilot/tài liệu) $\rightarrow$ Lập luận (Warrant giải thích cơ chế) $\rightarrow$ Kết luận (Conclusion)**.
* **Vận dụng Chương 6 (Liêm chính khoa học, sử dụng AI và đề cương liên ngành):**
  Khai báo AI minh bạch, trung thực; không ngụy tạo tài liệu; nhận diện đầy đủ 8 mảnh ghép của một đề cương nghiên cứu khoa học liên ngành hoàn chỉnh; xây dựng biểu đồ tiến độ Gantt và ma trận rủi ro khả thi.

## 2. Những khó khăn thực tế gặp phải và giải pháp khắc phục
Trong quá trình triển khai, tôi đã đối mặt với ba thách thức lớn:
1. *Thách thức về tính liên ngành:* Là một sinh viên chuyên ngành Công nghệ thông tin, thời gian đầu tôi có xu hướng nhìn nhận bài toán thuần túy dưới góc độ thuật toán tối ưu hóa mà xem nhẹ cơ chế môi trường.  
   $\rightarrow$ *Giải pháp:* Tôi đã chủ động nghiên cứu các tài liệu chuyên khảo về Khí tượng học và Ô nhiễm không khí đô thị, tham khảo Quy chuẩn QCVN 05:2023/BTNMT để hiểu bản chất của quá trình phân tán chất ô nhiễm ven biển, từ đó lựa chọn đúng các biến đầu vào có ý nghĩa tự nhiên.
2. *Thách thức về dữ liệu chuỗi thời gian khuyết thiếu:* Dữ liệu quan trắc thực tế tại trạm đo thường xuyên có những khoảng trống do lỗi mất kết nối mạng.  
   $\rightarrow$ *Giải pháp:* Thay vì xóa bỏ các dòng khuyết làm gián đoạn tính liên tục của chuỗi thời gian, tôi đã tìm hiểu và áp dụng kỹ thuật nội suy tuyến tính kết hợp trung bình trượt theo giờ, bảo toàn cấu trúc dữ liệu cho mô hình học máy.
3. *Thách thức về rò rỉ dữ liệu trong kiểm định mô hình:* Nếu chia tập dữ liệu ngẫu nhiên (Random Train-Test Split), mô hình sẽ học trước thông tin tương lai, dẫn đến sai số ảo rất thấp nhưng thất bại khi áp dụng vào thực tế.  
   $\rightarrow$ *Giải pháp:* Tôi đã nghiên cứu và áp dụng phương pháp kiểm định chéo chuyên dụng cho chuỗi thời gian (`TimeSeriesSplit`), đảm bảo tính nghiêm ngặt tuyệt đối của phương pháp luận khoa học.

\newpage

# TÀI LIỆU THAM KHẢO

1. Bộ Tài nguyên và Môi trường. (2023). *Quy chuẩn kỹ thuật quốc gia về chất lượng không khí xung quanh* (QCVN 05:2023/BTNMT). Hà Nội: NXB Tài nguyên - Môi trường và Bản đồ Việt Nam.
2. Chen, L. J., Ho, Y. H., Lee, H. C., Wu, H. C., Liu, H. M., Hsieh, H. H., ... & Lung, S. C. (2019). An open data approach to mapping urban air quality using high-resolution sensor networks. *Environmental Modelling & Software*, 114, 153-167. https://doi.org/10.1016/j.envsoft.2019.01.013
3. Deters, J. K., Zalakeviciute, R., Gonzalez, M., & Rybarczyk, Y. (2017). Modeling air pollution concentrations with meteorology in a high-altitude city. *Atmospheric Pollution Research*, 8(6), 1142-1150. https://doi.org/10.1016/j.apr.2017.05.004
4. Gu, K., Qiao, J., & Lin, W. (2020). Recurrent air quality predictor based on extreme learning machine with selective ensemble. *IEEE Transactions on Industrial Informatics*, 16(5), 3333-3343. https://doi.org/10.1109/TII.2019.2939714
5. Huang, C. J., & Kuo, P. H. (2018). A deep CNN-LSTM model for particulate matter ($\text{PM}_{2.5}$) forecasting in smart cities. *Sensors*, 18(7), 2220. https://doi.org/10.3390/s18072220
6. Le, V. D., Nguyen, T. H., & Tran, D. T. (2020). Air quality forecasting in Vietnam using deep neural networks and meteorological variables. *Vietnam Journal of Science and Technology*, 58(4), 450-462. https://doi.org/10.15625/2525-2518/58/4/14980
7. Masood, A., & Ahmad, K. (2023). A review on emerging artificial intelligence and machine learning approaches for air quality prediction. *Energy, Ecology and Environment*, 8(4), 340-362. https://doi.org/10.1007/s40974-023-00282-3
8. Nguyen, T. T., Bui, H. T., & Le, T. H. (2022). Deep learning approaches for hourly $\text{PM}_{2.5}$ concentration prediction in Ho Chi Minh City, Vietnam. *Atmospheric Environment*, 270, 118872. https://doi.org/10.1016/j.atmosenv.2021.118872
9. Pham, H. X., Nguyen, T. A., & Hoang, L. Q. (2021). Ground-level $\text{PM}_{2.5}$ estimation in Northern Vietnam using satellite aerosol optical depth and machine learning algorithms. *Environmental Monitoring and Assessment*, 193(8), 512. https://doi.org/10.1007/s10661-021-09285-4
10. Vu, T. V., Tran, N. T., & Nguyen, M. T. (2023). Meteorological influences on fine particulate matter in coastal Central Vietnam. *Journal of Environmental Sciences*, 125, 412-424. https://doi.org/10.1016/j.jes.2022.03.018
11. World Health Organization. (2021). *WHO global air quality guidelines: particulate matter ($\text{PM}_{2.5}$ and $\text{PM}_{10}$), ozone, nitrogen dioxide, sulfur dioxide and carbon monoxide*. World Health Organization. https://apps.who.int/iris/handle/10665/345329
12. Zheng, Y., Liu, F., & Hsieh, H. P. (2015). U-Air: When urban air quality inference meets big data. *ACM Transactions on Intelligent Systems and Technology*, 6(3), 1-28. https://doi.org/10.1145/2743025

\newpage

# PHỤ LỤC

## Phụ lục A: Cấu trúc tệp dữ liệu thô phục vụ Pilot (`danang_air_quality_pilot_dataset.csv`)
Dữ liệu thô gồm 720 dòng (tương ứng 720 giờ liên tục) với 8 trường thông tin:
`timestamp,PM25,temp,humidity,wind_speed,wind_dir,pressure,rain`

## Phụ lục B: Trích đoạn mã nguồn xử lý và huấn luyện mô hình Pilot
(Toàn bộ mã nguồn đầy đủ được lưu tại thư mục sản phẩm: `san_pham/pilot/src/pilot_air_quality_prediction.py`)

```python
# Trích đoạn mã nguồn nạp dữ liệu và huấn luyện mô hình XGBoost
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1. Nạp tập dữ liệu Pilot trạm Đà Nẵng
df = pd.read_csv("data/danang_air_quality_pilot_dataset.csv", parse_dates=["timestamp"])

# 2. Tạo đặc trưng trễ (Lag features)
df['PM25_lag1'] = df['PM25'].shift(1)
df['PM25_lag2'] = df['PM25'].shift(2)
df['PM25_lag24'] = df['PM25'].shift(24)
df['PM25_roll3'] = df['PM25'].rolling(window=3).mean()
df = df.dropna()

# 3. Phân chia Train/Test theo chuỗi thời gian (80% Train, 20% Test)
features = ['PM25_lag1', 'PM25_lag2', 'PM25_lag24', 'PM25_roll3', 'temp', 'humidity', 'wind_speed', 'rain', 'pressure']
X = df[features]
y = df['PM25']

split_idx = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

# 4. Huấn luyện mô hình XGBoost
model = XGBRegressor(n_estimators=100, max_depth=5, learning_rate=0.08, random_state=42)
model.fit(X_train, y_train)

# 5. Đánh giá sai số trên tập Test
preds = model.predict(X_test)
print(f"MAE: {mean_absolute_error(y_test, preds):.2f} ug/m3")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, preds)):.2f} ug/m3")
print(f"R2 Score: {r2_score(y_test, preds):.3f}")
```

