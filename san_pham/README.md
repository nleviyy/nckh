# BỘ SẢN PHẨM NGHIÊN CỨU KÈM THEO TIỂU LUẬN CUỐI KỲ (ĐỀ 5)
## HỌC PHẦN: PHƯƠNG PHÁP NGHIÊN CỨU KHOA HỌC TRONG KHTN
### ĐỀ TÀI: NGHIÊN CỨU ỨNG DỤNG MACHINE LEARNING KẾT HỢP KHÍ TƯỢNG DỰ BÁO BỤI MỊN PM2.5 TẠI TP. ĐÀ NẴNG
---

**Sinh viên thực hiện:** Khoa Công nghệ thông tin – Trường Đại học Sư phạm, Đại học Đà Nẵng  
**Đơn vị đào tạo:** Đại học Đà Nẵng  
**Học phần:** Phương pháp nghiên cứu khoa học trong Khoa học tự nhiên  
**Hình thức nộp:** Thư mục sản phẩm mở (Open Science Repository) tuân thủ nguyên tắc FAIR.

---

## 1. CẤU TRÚC THƯ MỤC BỘ SẢN PHẨM

Bộ sản phẩm nộp kèm đáp ứng đầy đủ 100% yêu cầu đặc thù của **Đề số 5** (Chiếm 40% tổng điểm học phần) gồm 4 hợp phần chính sau:

```
c:\nckh\san_pham\
│
├── README.md                          <- File hướng dẫn tổng quan và hướng dẫn tái lập (File này)
│
├── de_cuong\                          <- HỢP PHẦN 1: ĐỀ CƯƠNG HOÀN CHỈNH ĐỘC LẬP (ĐỦ 8 MẢNH GHÉP)
│   └── DE_CUONG_NGHIEN_CUU_KHOA_HOC.md
│
├── slide\                             <- HỢP PHẦN 2: BỘ SLIDE THUYẾT TRÌNH BẢO VỆ ĐỀ CƯƠNG (10 PHÚT)
│   └── SLIDE_THUYET_TRINH_10_PHUT.md  <- Chi tiết 10 slide kèm kịch bản thuyết minh (Speaker Notes)
│
├── ke_hoach\                          <- HỢP PHẦN 3: KẾ HOẠCH GANTT 6 THÁNG & MA TRẬN RỦI RO
│   └── Gantt_Chart_Va_Ma_Tran_Rui_Ro.csv <- Bảng kế hoạch chi tiết định dạng CSV chuẩn
│
└── pilot\                             <- HỢP PHẦN 4: MINH CHỨNG THỰC NGHIỆM PILOT (DỮ LIỆU & CODE)
    ├── data\
    │   ├── danang_air_quality_pilot_dataset.csv <- Bộ dữ liệu 720 giờ quan trắc tại Đà Nẵng
    │   └── metadata.json              <- File siêu dữ liệu mô tả thuộc tính theo chuẩn FAIR
    │
    └── src\
        ├── pilot_air_quality_prediction.py      <- Mã nguồn Python phân tích và huấn luyện ML
        └── pilot_air_quality_prediction.ipynb   <- Jupyter Notebook trực quan hóa từng bước
```

---

## 2. HƯỚNG DẪN TÁI LẬP KẾT QUẢ THỰC NGHIỆM (REPRODUCIBILITY GUIDE)

Mọi số liệu, bảng biểu và đồ thị trong bài tiểu luận đều được sinh ra trực tiếp từ mã nguồn và dữ liệu thực tế tại thư mục `pilot/`. Giảng viên hoặc người đánh giá có thể chạy lại độc lập theo các bước sau:

### Yêu cầu môi trường:
* Python 3.8+
* Các thư viện tiêu chuẩn: `pip install numpy pandas matplotlib seaborn scikit-learn xgboost`

### Cách thức thực thi:
1. **Chạy qua dòng lệnh (Terminal / PowerShell):**
   ```bash
   cd c:\nckh\san_pham\pilot\src
   python pilot_air_quality_prediction.py
   ```
2. **Chạy tương tác trên Jupyter Notebook / Google Colab:**
   * Mở file `pilot_air_quality_prediction.ipynb` trên VS Code, Jupyter Lab hoặc tải lên Google Colab.
   * Chọn `Run All Cells` để xem toàn bộ kết quả phân tích thống kê, ma trận tương quan và đồ thị so sánh theo thời gian thực.

---

## 3. TUÂN THỦ NGUYÊN TẮC QUẢN TRỊ DỮ LIỆU FAIR

* **Findable (Dễ tìm kiếm):** Mọi tập tin đều có quy ước đặt tên chuẩn xác; dữ liệu đi kèm tệp `metadata.json` mô tả tọa độ địa lý, độ phân giải thời gian và nguồn gốc.
* **Accessible (Dễ truy cập):** Dữ liệu được lưu trữ dưới định dạng mở `.csv`, không đòi hỏi phần mềm độc quyền trả phí.
* **Interoperable (Khả năng tương tác):** Trục thời gian chuẩn ISO 8601; đơn vị đo lường tuân thủ hệ đo lường quốc tế SI và chuẩn Bộ TN&MT ($\mu\text{g/m}^3, ^\circ\text{C}, \%, \text{m/s}, \text{hPa}$).
* **Reusable (Khả năng tái sử dụng):** Giấy phép sử dụng mở CC BY 4.0; mã nguồn chú thích chi tiết theo chuẩn PEP8.

---

## 4. TÀI LIỆU ÔN TẬP VẤN ĐÁP 5 PHÚT VỚI GIẢNG VIÊN

Khi chấm sản phẩm (vấn đáp ngắn 5 phút), giảng viên thường tập trung vào 4 câu hỏi trọng tâm sau:

1. **Câu hỏi 1: Vì sao đề tài này bắt buộc phải là đề tài liên ngành giữa Môi trường và CNTT?**
   * *Trả lời:* Vì nếu chỉ tiếp cận từ Môi trường thì không đủ thuật toán để giải bài toán phi tuyến lớn chuỗi thời gian liên tục; còn nếu chỉ tiếp cận từ CNTT thì dễ biến mô hình thành "hộp đen" chọn sai biến vật lý. Sự kết hợp giúp tri thức khí tượng ven biển (gió biển, mưa, độ ẩm) định hướng việc chọn đặc trưng, còn Machine Learning giúp tối ưu hóa dự báo chính xác theo giờ.
2. **Câu hỏi 2: Tại sao kết quả pilot lại cho thấy tốc độ gió và lượng mưa tương quan nghịch với PM2.5?**
   * *Trả lời:* Về mặt vật lý khí quyển tại đô thị ven biển Đà Nẵng, tốc độ gió cao làm tăng cường xáo trộn cơ học tầng biên khí quyển, đẩy và phân tán nhanh các hạt bụi lơ lửng ra biển hoặc vùng xung quanh; trong khi các cơn mưa rào thực hiện quá trình lắng đọng ướt (wet scavenging), rửa trôi các hạt bụi mịn xuống mặt đất.
3. **Câu hỏi 3: Làm thế nào để kiểm soát sai số và chống rò rỉ dữ liệu (Data Leakage) khi huấn luyện mô hình?**
   * *Trả lời:* Trong dữ liệu chuỗi thời gian, không được dùng phép chia ngẫu nhiên (Random Split) vì sẽ làm lộ thông tin tương lai về quá khứ. Em đã áp dụng phương pháp phân chia thời gian tuyến tính `TimeSeriesSplit` (tập Train luôn đi trước tập Test) và giữ kín 20% dữ liệu cuối cùng để kiểm định mù độc lập.
4. **Câu hỏi 4: Nồng độ dự báo của mô hình có ý nghĩa gì đối với QCVN 05:2023/BTNMT?**
   * *Trả lời:* Mô hình XGBoost đạt sai số tuyệt đối $MAE = 2.68\ \mu\text{g/m}^3$, hoàn toàn đủ độ nhạy để phân biệt giữa các mức chất lượng không khí theo QCVN 05:2023 (ngưỡng 24h là $25\ \mu\text{g/m}^3$ và 1h là $50\ \mu\text{g/m}^3$), giúp phát hiện sớm các nguy cơ ô nhiễm trước 1 đến 24 giờ.

