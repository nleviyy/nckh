# HỆ THỐNG DỰ BÁO NỒNG ĐỘ BỤI MỊN PM2.5 BẰNG MACHINE LEARNING TẠI ĐÀ NẴNG
## SẢN PHẨM PHẦN MỀM THỰC NGHIỆM (PILOT SOFTWARE APPLICATION)
### Học phần: Phương pháp nghiên cứu khoa học trong Khoa học tự nhiên
**Sinh viên thực hiện:** Khoa Công nghệ thông tin – Trường Đại học Sư phạm, Đại học Đà Nẵng  
**Địa bàn nghiên cứu:** Thành phố Đà Nẵng (Tọa độ: $16.0544^\circ\text{N}, 108.2022^\circ\text{E}$)

---

## 1. GIỚI THIỆU SẢN PHẨM PHẦN MỀM
Đây là sản phẩm phần mềm thực tế hoàn chỉnh được phát triển bằng ngôn ngữ **Python** và khung giao diện **Streamlit**, ứng dụng các thuật toán Học máy (Machine Learning) tiên tiến nhằm giải quyết bài toán cấp bách về dự báo nồng độ bụi mịn $\text{PM}_{2.5}$ theo chuỗi thời gian tại thành phố Đà Nẵng.

Hệ thống kết hợp dữ liệu chất lượng không khí với các yếu tố vi khí tượng ven biển (nhiệt độ, độ ẩm, tốc độ gió, áp suất khí quyển, lượng mưa), cho phép người dùng quan sát dashboard thời gian thực, nhập tham số vi khí hậu để dự báo và đánh giá nguy cơ ô nhiễm theo quy chuẩn quốc gia **QCVN 05:2023/BTNMT**.

---

## 2. CẤU TRÚC THƯ MỤC SẢN PHẨM (`C:\nckh\san_pham\pilot`)

```
C:\nckh\san_pham\pilot\
│
├── app.py                     <- Ứng dụng Web Dashboard & Công cụ dự báo tương tác (Streamlit)
├── train_model.py             <- Script huấn luyện 3 thuật toán ML, xuất metrics và model (.joblib)
├── requirements.txt           <- Danh mục thư viện Python yêu cầu
├── README.md                  <- Tài liệu hướng dẫn cài đặt, vận hành và kiểm thử (File này)
│
├── data\                      <- DỮ LIỆU NGHIÊN CỨU THỰC TẾ
│   ├── danang_real_air_quality.csv          <- 2.178 giờ quan trắc thực tế tại Đà Nẵng (CAMS/ERA5)
│   ├── danang_air_quality_pilot_dataset.csv  <- Dữ liệu chuỗi thời gian 720 giờ phục vụ bài tiểu luận
│   ├── fetch_danang_real_data.py            <- Kịch bản tải dữ liệu tự động từ Open-Meteo API
│   ├── DATA_SOURCE.md                       <- Mô tả minh bạch nguồn gốc và đặc tả dữ liệu
│   └── metadata.json                        <- Siêu dữ liệu chuẩn FAIR
│
├── models\                    <- MÔ HÌNH HỌC MÁY ĐÃ HUẤN LUYỆN SẴN
│   ├── linear_regression.joblib <- Mô hình hồi quy tuyến tính
│   ├── random_forest.joblib     <- Mô hình Random Forest (R² = 0.9024)
│   ├── xgboost.joblib           <- Mô hình XGBoost (R² = 0.9080)
│   ├── metrics.json             <- Kết quả đánh giá sai số định lượng (MAE, RMSE, R²)
│   └── features_config.json     <- Cấu hình các đặc trưng phục vụ suy luận
│
├── outputs\                   <- BIỂU ĐỒ VÀ KẾT QUẢ ĐÁNH GIÁ ĐỊNH LƯỢNG
│   ├── model_comparison.csv     <- Bảng tổng hợp so sánh các chỉ số của 3 mô hình
│   ├── test_predictions.csv     <- Toàn bộ giá trị Thực tế và Dự báo trên 431 giờ kiểm thử
│   ├── prediction_comparison.png<- Đồ thị đối chứng thực tế vs dự báo (Độ phân giải cao 300 DPI)
│   └── feature_importance.png   <- Biểu đồ xếp hạng mức độ quan trọng của đặc trưng
│
└── src\                       <- Kịch bản kiểm chứng bổ trợ phục vụ tiểu luận
    ├── pilot_air_quality_prediction.py
    └── pilot_air_quality_prediction.ipynb
```

---

## 3. CÁC THUẬT TOÁN HỌC MÁY ĐƯỢC TRIỂN KHAI VÀ KẾT QUẢ ĐÁNH GIÁ

Dữ liệu được huấn luyện trên 1.723 giờ và kiểm định trên **431 giờ kiểm thử độc lập (Test Set)** theo phương pháp chia chuỗi thời gian tuyến tính (không rò rỉ dữ liệu). Kết quả thực nghiệm:

| Thuật toán | MAE ($\mu\text{g/m}^3$) | RMSE ($\mu\text{g/m}^3$) | Hệ số xác định $R^2$ | Đánh giá năng lực |
| :--- | :---: | :---: | :---: | :--- |
| **Linear Regression** | 0.813 | 1.251 | 0.9162 | Mô hình cơ sở, giải thích tuyến tính tốt nhưng không bắt được đỉnh phi tuyến cực đoan. |
| **Random Forest Regressor** | 0.806 | 1.350 | 0.9024 | Mô hình cây tổ hợp Bagging, rất bền vững với nhiễu môi trường, chống quá khớp tốt. |
| **XGBoost Regressor** | **0.806** | **1.311** | **0.9080** | **Mô hình tối ưu:** Sai số tuyệt đối trung bình chỉ 0.806 $\mu\text{g/m}^3$, giải thích 90.8% phương sai thực tế. |

---

## 4. HƯỚNG DẪN CÀI ĐẶT VÀ CHẠY ỨNG DỤNG TRÊN WINDOWS

### Bước 1: Mở Terminal (PowerShell hoặc Command Prompt)
Nhấn phím `Windows`, gõ `PowerShell` và nhấn `Enter`.

### Bước 2: Di chuyển vào thư mục dự án
```powershell
cd C:\nckh\san_pham\pilot
```

### Bước 3: Cài đặt các thư viện phụ thuộc (nếu chưa có)
```powershell
python -m pip install -r requirements.txt
```

### Bước 4 (Tùy chọn): Chạy lại quy trình huấn luyện mô hình
Nếu muốn cập nhật dữ liệu mới hoặc huấn luyện lại toàn bộ mô hình:
```powershell
python train_model.py
```

### Bước 5: KHỞI CHẠY ỨNG DỤNG WEB STREAMLIT
```powershell
python -m streamlit run app.py
```
Ngay sau khi lệnh chạy, trình duyệt web mặc định của bạn sẽ tự động mở trang web tại địa chỉ:
👉 **`http://localhost:8501`**

---

## 5. CÁC TÍNH NĂNG NỔI BẬT CỦA ỨNG DỤNG
1. **Dashboard thời gian thực:** Hiển thị thẻ chỉ số (Metrics), phân loại mức độ ô nhiễm theo màu sắc chuẩn QCVN 05:2023, đồ thị diễn biến $\text{PM}_{2.5}$ chuỗi thời gian tương tác (Plotly) và ma trận tương quan nhiệt.
2. **Công cụ dự báo trực quan:** Cho phép lựa chọn thuật toán (XGBoost, Random Forest, Linear Regression); nhập các thông số khí tượng (nhiệt độ, độ ẩm, gió, mưa, áp suất); cung cấp nút "Lấy mẫu ngẫu nhiên từ dữ liệu thực tế" để thử nhanh; đưa ra kết quả dự báo định lượng và khuyến nghị y tế dự phòng.
3. **Đối chứng và kiểm định:** Bảng số liệu MAE, RMSE, $R^2$; biểu đồ tương tác so sánh đường thực tế và 3 đường dự báo; cho phép tải dữ liệu dự báo chi tiết về máy tính dưới dạng CSV.
4. **Luận cứ khoa học liên ngành:** Trình bày rõ ràng mối quan hệ tương hỗ giữa Khoa học Môi trường và Công nghệ thông tin.

