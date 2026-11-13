# MÔ TẢ NGUỒN GỐC VÀ ĐẶC TẢ DỮ LIỆU THỰC TẾ
## ĐỀ TÀI: DỰ BÁO NỒNG ĐỘ BỤI MỊN PM2.5 TẠI THÀNH PHỐ ĐÀ NẴNG

---

### 1. NGUỒN GỐC DỮ LIỆU (DATA PROVENANCE)
Toàn bộ dữ liệu huấn luyện và kiểm thử của hệ thống phần mềm được thu thập trực tiếp và minh bạch từ:
1. **Dữ liệu chất lượng không khí (PM2.5, PM10, CO, NO2):**
   * **Nhà cung cấp:** Copernicus Atmosphere Monitoring Service (CAMS) / ECMWF thông qua cổng dữ liệu mở **Open-Meteo Air Quality API**.
   * **Tọa độ địa lý thu thập:** Vĩ độ $16.0544^\circ\text{N}$, Kinh độ $108.2022^\circ\text{E}$ (Trung tâm thành phố Đà Nẵng).
   * **Độ phân giải thời gian:** Theo từng giờ liên tục (Hourly time-series).
   * **Thời gian ghi nhận:** 90 ngày quan trắc thực tế liên tục từ tháng 08/2026 đến tháng 11/2026 (Tổng cộng 2.178 bản ghi giờ).
2. **Dữ liệu vi khí tượng bề mặt (Nhiệt độ, Độ ẩm, Gió, Áp suất, Mưa):**
   * **Nhà cung cấp:** Hệ thống tái phân tích khí tượng toàn cầu ERA5 / GFS thông qua **Open-Meteo Weather API**.
   * **Biến số đồng bộ:** Nhiệt độ tại độ cao 2m ($^\circ\text{C}$), Độ ẩm tương đối 2m ($\%$), Tốc độ gió 10m ($\text{m/s}$), Hướng gió ($^\circ$), Áp suất khí quyển bề mặt ($\text{hPa}$), và Lượng mưa tích lũy ($\text{mm}$).

### 2. CAM KẾT VỀ TÍNH CHÂN THỰC CỦA DỮ LIỆU
* Dữ liệu được tải tự động và tái lập được 100% thông qua tệp mã nguồn `fetch_danang_real_data.py`.
* Tuyệt đối không sử dụng số liệu ngụy tạo hay biến đổi làm sai lệch bản chất tự nhiên.
* Tập dữ liệu phản ánh chính xác quy luật chất lượng không khí tại đô thị ven biển Đà Nẵng: Nồng độ $\text{PM}_{2.5}$ trung bình đạt khoảng $12.43\ \mu\text{g/m}^3$ (thuộc mức "Tốt" theo QCVN 05:2023/BTNMT), với các đợt tăng cao cục bộ đạt tới $49.0\ \mu\text{g/m}^3$ trong các thời điểm gió yếu và nghịch nhiệt.

### 3. CÁC TẬP TIN DỮ LIỆU TRONG THƯ MỤC
* `danang_real_air_quality.csv`: Tập dữ liệu 2.178 giờ quan trắc thực tế tại Đà Nẵng (dùng cho huấn luyện mô hình chính thức của phần mềm).
* `danang_air_quality_pilot_dataset.csv`: Tập dữ liệu thực nghiệm 720 giờ phục vụ báo cáo bài tiểu luận lý thuyết.
* `metadata.json`: Bản đặc tả thuộc tính dữ liệu theo chuẩn quản trị dữ liệu mở FAIR.
* `fetch_danang_real_data.py`: Kịch bản Python tải và cập nhật dữ liệu tự động từ API.

