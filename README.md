# Nghiên cứu dự báo PM2.5 tại TP. Đà Nẵng

**Đề tài:** Ứng dụng Machine Learning kết hợp dữ liệu khí tượng để dự báo bụi mịn PM2.5 tại TP. Đà Nẵng  
**Học phần:** Phương pháp nghiên cứu khoa học trong Khoa học tự nhiên  
**Đơn vị:** Khoa Công nghệ thông tin – Trường Đại học Sư phạm, Đại học Đà Nẵng

Đây là bộ sản phẩm nghiên cứu kèm theo tiểu luận cuối kỳ (Đề 5), gồm đề cương, slide thuyết trình, kế hoạch nghiên cứu và minh chứng thực nghiệm pilot.

## Tài liệu và sản phẩm

- [Hướng dẫn tổng quan và tái lập kết quả](san_pham/README.md)
- [Đề cương nghiên cứu](san_pham/de_cuong/DE_CUONG_NGHIEN_CUU_KHOA_HOC.md)
- [Slide thuyết trình 10 phút](san_pham/slide/SLIDE_THUYET_TRINH_10_PHUT.md)
- [Kế hoạch Gantt và ma trận rủi ro](san_pham/ke_hoach/Gantt_Chart_Va_Ma_Tran_Rui_Ro.csv)
- [Dữ liệu pilot](san_pham/pilot/data/danang_air_quality_pilot_dataset.csv)
- [Mã nguồn phân tích và dự báo](san_pham/pilot/src/pilot_air_quality_prediction.py)
- [Notebook thực nghiệm](san_pham/pilot/src/pilot_air_quality_prediction.ipynb)

## Chạy thử pilot

Yêu cầu Python 3.8 trở lên. Cài các thư viện được liệt kê trong [requirements.txt](san_pham/pilot/requirements.txt), sau đó chạy:

```powershell
cd san_pham/pilot
python src/pilot_air_quality_prediction.py
```

Xem [hướng dẫn chi tiết](san_pham/README.md) để biết thêm về dữ liệu, quy trình thực nghiệm và cách tái lập kết quả.
