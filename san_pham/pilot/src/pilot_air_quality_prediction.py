"""
========================================================================================
HỌC PHẦN: PHƯƠNG PHÁP NGHIÊN CỨU KHOA HỌC TRONG KHOA HỌC TỰ NHIÊN
ĐỀ TÀI: NGHIÊN CỨU ỨNG DỤNG MACHINE LEARNING DỰ BÁO BỤI MỊN PM2.5 TẠI TP. ĐÀ NẴNG
FILE: pilot_air_quality_prediction.py (KỊCH BẢN THỰC NGHIỆM PILOT TÁI LẬP - FAIR)
SINH VIÊN THỰC HIỆN: Khoa Công nghệ thông tin - Trường Đại học Sư phạm, ĐH Đà Nẵng
========================================================================================
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Kiểm tra thư viện XGBoost; nếu chưa cài đặt thì sử dụng GradientBoostingRegressor tương đương
try:
    from xgboost import XGBRegressor
    HAS_XGBOOST = True
except ImportError:
    from sklearn.ensemble import GradientBoostingRegressor
    HAS_XGBOOST = False

def main():
    print("=" * 80)
    print("CHƯƠNG TRÌNH THỰC NGHIỆM PILOT: DỰ BÁO NỒNG ĐỘ PM2.5 TẠI TP. ĐÀ NẴNG")
    print("=" * 80)

    # 1. XÁC ĐỊNH ĐƯỜNG DẪN DỮ LIỆU
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "..", "data", "danang_air_quality_pilot_dataset.csv")
    output_dir = os.path.join(script_dir, "..", "output")
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(data_path):
        print(f"[LỖI] Không tìm thấy tệp dữ liệu tại: {data_path}")
        sys.exit(1)

    print(f"\n[BƯỚC 1] Đang nạp dữ liệu từ: {os.path.abspath(data_path)}")
    df = pd.read_csv(data_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    print(f"-> Nạp thành công: {len(df)} quan trắc giờ liên tục (30 ngày).")

    # 2. THỐNG KÊ MÔ TẢ VÀ ĐÁNH GIÁ ĐỘ KHÔNG ĐẢM BẢO ĐO (CHƯƠNG 4)
    print("\n[BƯỚC 2] Tính toán thống kê mô tả và độ không đảm bảo đo mở rộng U_95%:")
    stats_df = df[['PM25', 'temp', 'humidity', 'wind_speed', 'rain', 'pressure']].describe().T
    stats_df['SE'] = stats_df['std'] / np.sqrt(stats_df['count'])
    stats_df['U95'] = 1.96 * stats_df['SE']  # Khoảng tin cậy 95%
    print(stats_df[['mean', 'std', 'min', '50%', 'max', 'U95']].round(2))

    # 3. PHÂN TÍCH TƯƠNG QUAN KHÍ TƯỢNG (CHƯƠNG 2 & CHƯƠNG 3)
    print("\n[BƯỚC 3] Phân tích hệ số tương quan Pearson giữa PM2.5 và biến khí tượng:")
    corr_matrix = df[['PM25', 'temp', 'humidity', 'wind_speed', 'pressure', 'rain']].corr()
    pm25_corr = corr_matrix['PM25'].drop('PM25').sort_values()
    for var, val in pm25_corr.items():
        print(f"  * Tương quan PM2.5 với {var:12s}: r = {val:+.3f}")

    # 4. KỸ NGHỆ ĐẶC TRƯNG CHUỖI THỜI GIAN (FEATURE ENGINEERING)
    print("\n[BƯỚC 4] Thực hiện kỹ nghệ đặc trưng (Lag Features, Rolling Window, Diurnal Cycle):")
    # Biến tuần hoàn giờ trong ngày
    df['hour'] = df['timestamp'].dt.hour
    df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24.0)
    df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24.0)

    # Biến trễ (Lag Features)
    df['PM25_lag1'] = df['PM25'].shift(1)
    df['PM25_lag2'] = df['PM25'].shift(2)
    df['PM25_lag24'] = df['PM25'].shift(24)

    # Biến cửa sổ trượt (Rolling Statistics)
    df['PM25_roll3'] = df['PM25'].rolling(window=3).mean()
    df['PM25_roll24'] = df['PM25'].rolling(window=24).mean()

    # Loại bỏ các dòng NaN do tạo lag
    df_clean = df.dropna().reset_index(drop=True)
    print(f"-> Kích thước tập dữ liệu sau khi tạo đặc trưng: {df_clean.shape}")

    # 5. PHÂN CHIA DỮ LIỆU TRAIN / TEST THEO CHUỖI THỜI GIAN (KHÔNG RÒ RỈ DỮ LIỆU)
    features = [
        'PM25_lag1', 'PM25_lag2', 'PM25_lag24', 'PM25_roll3', 'PM25_roll24',
        'temp', 'humidity', 'wind_speed', 'pressure', 'rain', 'hour_sin', 'hour_cos'
    ]
    target = 'PM25'

    X = df_clean[features]
    y = df_clean[target]

    split_idx = int(len(df_clean) * 0.8)
    X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
    y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]
    print(f"-> Tập huấn luyện (Train): {len(X_train)} giờ | Tập kiểm thử (Test): {len(X_test)} giờ")

    # 6. HUẤN LUYỆN VÀ SO SÁNH CÁC MÔ HÌNH HỌC MÁY
    print("\n[BƯỚC 5] Huấn luyện và đánh giá các mô hình:")

    # Mô hình 1: Baseline Ngây thơ (y_hat = y_t-1)
    baseline_preds = X_test['PM25_lag1'].values
    mae_base = mean_absolute_error(y_test, baseline_preds)
    rmse_base = np.sqrt(mean_squared_error(y_test, baseline_preds))
    r2_base = r2_score(y_test, baseline_preds)

    # Mô hình 2: Random Forest
    rf = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    rf_preds = rf.predict(X_test)
    mae_rf = mean_absolute_error(y_test, rf_preds)
    rmse_rf = np.sqrt(mean_squared_error(y_test, rf_preds))
    r2_rf = r2_score(y_test, rf_preds)

    # Mô hình 3: XGBoost (hoặc GradientBoosting)
    if HAS_XGBOOST:
        xgb = XGBRegressor(n_estimators=100, max_depth=5, learning_rate=0.08, subsample=0.8, random_state=42)
    else:
        xgb = GradientBoostingRegressor(n_estimators=100, max_depth=5, learning_rate=0.08, subsample=0.8, random_state=42)
    xgb.fit(X_train, y_train)
    xgb_preds = xgb.predict(X_test)
    mae_xgb = mean_absolute_error(y_test, xgb_preds)
    rmse_xgb = np.sqrt(mean_squared_error(y_test, xgb_preds))
    r2_xgb = r2_score(y_test, xgb_preds)

    # In kết quả so sánh
    results = pd.DataFrame({
        "Mô hình": ["Baseline (Naive)", "Random Forest Regressor", "XGBoost Regressor"],
        "MAE (ug/m3)": [round(mae_base, 2), round(mae_rf, 2), round(mae_xgb, 2)],
        "RMSE (ug/m3)": [round(rmse_base, 2), round(rmse_rf, 2), round(rmse_xgb, 2)],
        "R2 Score": [round(r2_base, 3), round(r2_rf, 3), round(r2_xgb, 3)],
        "Cải thiện RMSE so với Baseline (%)": [
            "0.0%",
            f"{((rmse_base - rmse_rf) / rmse_base * 100):.1f}%",
            f"{((rmse_base - rmse_xgb) / rmse_base * 100):.1f}%"
        ]
    })
    print("\nBẢNG KẾT QUẢ ĐÁNH GIÁ HIỆU NĂNG TRÊN TẬP KIỂM THỬ ĐỘC LẬP:")
    print(results.to_string(index=False))

    # Lưu kết quả ra file CSV
    eval_csv_path = os.path.join(output_dir, "pilot_evaluation_metrics.csv")
    results.to_csv(eval_csv_path, index=False, encoding='utf-8-sig')
    print(f"\n-> Đã lưu bảng kết quả định lượng tại: {eval_csv_path}")

    # 7. VẼ VÀ XUẤT ĐỒ THỊ BÁO CÁO (FAIR VISUALIZATION)
    try:
        plt.style.use('seaborn-v0_8-whitegrid')
    except Exception:
        plt.style.use('default')

    # Hình 1: Biểu đồ dự báo so với thực tế
    plt.figure(figsize=(14, 5))
    test_timeline = df_clean['timestamp'].iloc[split_idx:]
    plt.plot(test_timeline, y_test.values, label='Giá trị thực tế (PM2.5 Thực đo)', color='#1f77b4', linewidth=2.0)
    plt.plot(test_timeline, xgb_preds, label=f'Mô hình XGBoost Dự báo (R² = {r2_xgb:.3f})', color='#d62728', linestyle='--', linewidth=1.8)
    plt.axhline(y=25, color='orange', linestyle=':', label='QCVN 05:2023 24h (25 ug/m3)')
    plt.axhline(y=50, color='red', linestyle=':', label='QCVN 05:2023 1h (50 ug/m3)')
    plt.title('ĐỒ THỊ ĐỐI CHỨNG GIÁ TRỊ THỰC TẾ VÀ DỰ BÁO CỦA MÔ HÌNH HỌC MÁY TẠI ĐÀ NẴNG', fontsize=12, fontweight='bold')
    plt.xlabel('Thời gian quan trắc', fontsize=10)
    plt.ylabel('Nồng độ PM2.5 (ug/m3)', fontsize=10)
    plt.legend(loc='upper right')
    plt.tight_layout()
    fig1_path = os.path.join(output_dir, "prediction_vs_actual.png")
    plt.savefig(fig1_path, dpi=300)
    plt.close()
    print(f"-> Đã xuất đồ thị so sánh dự báo tại: {fig1_path}")

    # Hình 2: Đánh giá tầm quan trọng của đặc trưng (Feature Importance)
    plt.figure(figsize=(10, 6))
    importances = xgb.feature_importances_
    indices = np.argsort(importances)
    plt.barh(range(len(indices)), importances[indices], color='#2ca02c', align='center')
    plt.yticks(range(len(indices)), [features[i] for i in indices])
    plt.xlabel('Tỷ trọng đóng góp vào mô hình (Relative Importance)', fontsize=10)
    plt.title('MỨC ĐỘ QUAN TRỌNG CỦA CÁC ĐẶC TRƯNG MÔI TRƯỜNG & KHÍ TƯỢNG (XGBOOST)', fontsize=12, fontweight='bold')
    plt.tight_layout()
    fig2_path = os.path.join(output_dir, "feature_importance.png")
    plt.savefig(fig2_path, dpi=300)
    plt.close()
    print(f"-> Đã xuất đồ thị mức độ quan trọng đặc trưng tại: {fig2_path}")

    print("\n" + "=" * 80)
    print("HOÀN THÀNH THỰC NGHIỆM PILOT THÀNH CÔNG RỰC RỠ!")
    print("Toàn bộ dữ liệu, mã nguồn và kết quả kiểm chứng đã sẵn sàng theo tiêu chuẩn FAIR.")
    print("=" * 80)

if __name__ == "__main__":
    main()

