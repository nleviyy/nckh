"""
========================================================================================
HỆ THỐNG DỰ BÁO NỒNG ĐỘ BỤI MỊN PM2.5 BẰNG MACHINE LEARNING TẠI TP. ĐÀ NẴNG
FILE: train_model.py - HUẤN LUYỆN, ĐÁNH GIÁ VÀ LƯU TRỮ CÁC MÔ HÌNH HỌC MÁY
========================================================================================
Thuật toán triển khai:
1. Linear Regression (Mô hình hồi quy tuyến tính)
2. Random Forest Regressor (Rừng ngẫu nhiên - Bagging Ensemble)
3. XGBoost Regressor (Tăng cường độ dốc cực đại - Gradient Boosting)
========================================================================================
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Kiểm tra XGBoost
try:
    from xgboost import XGBRegressor
    HAS_XGB = True
except ImportError:
    from sklearn.ensemble import GradientBoostingRegressor
    HAS_XGB = False

def create_features(df):
    """
    Kỹ nghệ đặc trưng cho chuỗi thời gian khí tượng và chất lượng không khí:
    - Biến trễ (Lag features): PM25 trễ 1 giờ, 2 giờ, 24 giờ (t-1, t-2, t-24)
    - Biến cửa sổ trượt (Rolling statistics): Trung bình trượt của các giờ QUÁ KHỨ (shift 1 để tránh rò rỉ target)
    - Biến chu kỳ thời gian (Diurnal cycle): sin/cos của giờ trong ngày
    """
    df = df.copy()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp').reset_index(drop=True)

    # Đặc trưng thời gian tuần hoàn
    df['hour'] = df['timestamp'].dt.hour
    df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24.0)
    df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24.0)

    # Đặc trưng trễ thời gian (Lag Features)
    df['PM25_lag1'] = df['PM25'].shift(1)
    df['PM25_lag2'] = df['PM25'].shift(2)
    df['PM25_lag24'] = df['PM25'].shift(24)

    # Đặc trưng trung bình trượt của QUÁ KHỨ (bắt đầu từ t-1)
    df['PM25_roll3'] = df['PM25'].shift(1).rolling(window=3).mean()
    df['PM25_roll24'] = df['PM25'].shift(1).rolling(window=24).mean()

    # Loại bỏ các hàng bị khuyết do tạo lag
    df_clean = df.dropna().reset_index(drop=True)
    return df_clean

def train_and_evaluate():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    models_dir = os.path.join(base_dir, "models")
    outputs_dir = os.path.join(base_dir, "outputs")

    os.makedirs(models_dir, exist_ok=True)
    os.makedirs(outputs_dir, exist_ok=True)

    # 1. NẠP DỮ LIỆU THỰC TẾ
    data_file = os.path.join(data_dir, "danang_real_air_quality.csv")
    if not os.path.exists(data_file):
        data_file = os.path.join(data_dir, "danang_air_quality_pilot_dataset.csv")

    print(f"[*] Đang nạp dữ liệu từ: {data_file}")
    raw_df = pd.read_csv(data_file)
    print(f"-> Tổng số dòng dữ liệu thô: {len(raw_df)}")

    # 2. TIỀN XỬ LÝ VÀ KỸ NGHỆ ĐẶC TRƯNG
    df = create_features(raw_df)
    feature_cols = [
        'PM25_lag1', 'PM25_lag2', 'PM25_lag24', 'PM25_roll3', 'PM25_roll24',
        'temp', 'humidity', 'wind_speed', 'pressure', 'rain', 'hour_sin', 'hour_cos'
    ]
    target_col = 'PM25'

    X = df[feature_cols]
    y = df[target_col]

    # 3. CHIA DỮ LIỆU THEO CHUỖI THỜI GIAN (80% TRAIN, 20% TEST - TUYỆT ĐỐI KHÔNG DATA LEAKAGE)
    split_index = int(len(df) * 0.8)
    X_train, X_test = X.iloc[:split_index], X.iloc[split_index:]
    y_train, y_test = y.iloc[:split_index], y.iloc[split_index:]
    timestamps_test = df['timestamp'].iloc[split_index:]

    print(f"-> Kích thước tập huấn luyện (Train): {len(X_train)} dòng")
    print(f"-> Kích thước tập kiểm thử (Test): {len(X_test)} dòng")

    # 4. KHỞI TẠO VÀ HUẤN LUYỆN 3 MÔ HÌNH HỌC MÁY
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=100, max_depth=10, min_samples_split=4, random_state=42, n_jobs=-1),
        "XGBoost": XGBRegressor(n_estimators=100, max_depth=5, learning_rate=0.08, subsample=0.85, colsample_bytree=0.85, random_state=42) if HAS_XGB else GradientBoostingRegressor(n_estimators=100, max_depth=5, learning_rate=0.08, random_state=42)
    }

    metrics_dict = {}
    predictions_df = pd.DataFrame({"timestamp": timestamps_test, "Actual_PM25": y_test.values})

    print("\n" + "=" * 70)
    print("KẾT QUẢ ĐÁNH GIÁ CÁC MÔ HÌNH TRÊN TẬP KIỂM THỬ ĐỘC LẬP (TEST SET)")
    print("=" * 70)

    for name, model in models.items():
        print(f"\n[*] Đang huấn luyện mô hình: {name}...")
        model.fit(X_train, y_train)

        # Dự báo trên tập kiểm thử
        preds = model.predict(X_test)
        predictions_df[name] = np.round(preds, 2)

        # Đánh giá các chỉ số
        mae = mean_absolute_error(y_test, preds)
        rmse = np.sqrt(mean_squared_error(y_test, preds))
        r2 = r2_score(y_test, preds)

        metrics_dict[name] = {
            "MAE": round(float(mae), 3),
            "RMSE": round(float(rmse), 3),
            "R2": round(float(r2), 4)
        }

        print(f"   + MAE  (Sai số tuyệt đối TB):   {mae:.3f} ug/m3")
        print(f"   + RMSE (Căn bậc hai sai số):   {rmse:.3f} ug/m3")
        print(f"   + R²   (Hệ số xác định):       {r2:.4f}")

        # Lưu model đã huấn luyện vào thư mục models/
        model_filename = name.lower().replace(" ", "_") + ".joblib"
        model_path = os.path.join(models_dir, model_filename)
        joblib.dump(model, model_path)
        print(f"   -> Đã lưu mô hình tại: {model_path}")

    # 5. LƯU THÔNG TIN METRICS VÀ KẾT QUẢ DỰ BÁO
    metrics_path = os.path.join(models_dir, "metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics_dict, f, indent=4, ensure_ascii=False)

    summary_df = pd.DataFrame(metrics_dict).T
    summary_df.to_csv(os.path.join(outputs_dir, "model_comparison.csv"), encoding="utf-8-sig")

    predictions_df.to_csv(os.path.join(outputs_dir, "test_predictions.csv"), index=False, encoding="utf-8-sig")

    # 6. LƯU DANH SÁCH FEATURES PHỤC VỤ DỰ BÁO TRÊN APP
    best_model_name = "XGBoost" if metrics_dict["XGBoost"]["R2"] >= metrics_dict["Random Forest"]["R2"] else "Random Forest"
    feature_meta = {
        "features": feature_cols,
        "target": target_col,
        "best_model": best_model_name,
        "last_trained_timestamp": str(df['timestamp'].max())
    }
    with open(os.path.join(models_dir, "features_config.json"), "w", encoding="utf-8") as f:
        json.dump(feature_meta, f, indent=4)

    # 7. VẼ ĐỒ THỊ SO SÁNH VÀ XUẤT ẢNH BÁO CÁO
    print("\n[*] Đang kết xuất biểu đồ đánh giá vào thư mục outputs/...")
    plt.style.use('default')

    # Đồ thị 1: So sánh giá trị Thực tế vs Dự báo (Test Set)
    plt.figure(figsize=(14, 6))
    plt.plot(predictions_df['timestamp'], predictions_df['Actual_PM25'], label='Thực tế (Quan trắc Đà Nẵng)', color='#1f77b4', linewidth=2.0)
    plt.plot(predictions_df['timestamp'], predictions_df['Linear Regression'], label=f'Linear Regression (R²={metrics_dict["Linear Regression"]["R2"]:.3f})', color='#7f7f7f', linestyle=':', linewidth=1.2)
    plt.plot(predictions_df['timestamp'], predictions_df['Random Forest'], label=f'Random Forest (R²={metrics_dict["Random Forest"]["R2"]:.3f})', color='#2ca02c', linestyle='--', linewidth=1.5)
    plt.plot(predictions_df['timestamp'], predictions_df['XGBoost'], label=f'XGBoost (R²={metrics_dict["XGBoost"]["R2"]:.3f})', color='#d62728', linestyle='-', linewidth=1.8)

    plt.axhline(y=25, color='orange', linestyle='--', alpha=0.7, label='QCVN 05:2023 TB 24h (25 ug/m3)')
    plt.axhline(y=50, color='red', linestyle='--', alpha=0.7, label='QCVN 05:2023 TB 1h (50 ug/m3)')

    plt.title('ĐỐI CHỨNG DỰ BÁO CỦA CÁC THUẬT TOÁN HỌC MÁY TRÊN TẬP KIỂM THỬ ĐÀ NẴNG', fontsize=12, fontweight='bold')
    plt.xlabel('Thời gian quan trắc (Giờ)', fontsize=10)
    plt.ylabel('Nồng độ PM2.5 (ug/m3)', fontsize=10)
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(outputs_dir, "prediction_comparison.png"), dpi=300)
    plt.close()

    # Đồ thị 2: Mức độ quan trọng đặc trưng (Feature Importance)
    best_tree_model = models["XGBoost"] if HAS_XGB else models["Random Forest"]
    importances = best_tree_model.feature_importances_
    indices = np.argsort(importances)

    plt.figure(figsize=(10, 6))
    plt.barh(range(len(indices)), importances[indices], color='#2b5c8f', align='center')
    plt.yticks(range(len(indices)), [feature_cols[i] for i in indices])
    plt.xlabel('Trọng số quan trọng tương đối', fontsize=10)
    plt.title('MỨC ĐỘ ĐÓNG GÓP CỦA CÁC ĐẶC TRƯNG MÔI TRƯỜNG & KHÍ TƯỢNG (XGBOOST)', fontsize=12, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(outputs_dir, "feature_importance.png"), dpi=300)
    plt.close()

    print("[+] Hoàn tất huấn luyện mô hình và lưu sản phẩm thành công!")

if __name__ == "__main__":
    train_and_evaluate()
