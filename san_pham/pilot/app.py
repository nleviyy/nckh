"""
========================================================================================
HỆ THỐNG DỰ BÁO NỒNG ĐỘ BỤI MỊN PM2.5 BẰNG MACHINE LEARNING TẠI THÀNH PHỐ ĐÀ NẴNG
TRƯỜNG ĐẠI HỌC SƯ PHẠM – ĐẠI HỌC ĐÀ NẴNG | KHOA CÔNG NGHỆ THÔNG TIN
HỌC PHẦN: PHƯƠNG PHÁP NGHIÊN CỨU KHOA HỌC TRONG KHOA HỌC TỰ NHIÊN
========================================================================================
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# Thiết lập cấu hình trang Streamlit
st.set_page_config(
    page_title="Dự Báo PM2.5 Đà Nẵng - Machine Learning",
    page_icon="🌫️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Đường dẫn thư mục
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODELS_DIR = os.path.join(BASE_DIR, "models")
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")

# ==============================================================================
# HÀM HỖ TRỢ NẠP DỮ LIỆU VÀ MÔ HÌNH (CACHE ĐỂ TĂNG TỐC ĐỘ ỨNG DỤNG)
# ==============================================================================
@st.cache_data
def load_data():
    real_csv = os.path.join(DATA_DIR, "danang_real_air_quality.csv")
    if os.path.exists(real_csv):
        df = pd.read_csv(real_csv)
    else:
        df = pd.read_csv(os.path.join(DATA_DIR, "danang_air_quality_pilot_dataset.csv"))
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

@st.cache_data
def load_predictions():
    pred_path = os.path.join(OUTPUTS_DIR, "test_predictions.csv")
    if os.path.exists(pred_path):
        df_pred = pd.read_csv(pred_path)
        df_pred['timestamp'] = pd.to_datetime(df_pred['timestamp'])
        return df_pred
    return None

@st.cache_data
def load_metrics():
    metrics_path = os.path.join(MODELS_DIR, "metrics.json")
    if os.path.exists(metrics_path):
        with open(metrics_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def load_model(model_name):
    filename = model_name.lower().replace(" ", "_") + ".joblib"
    path = os.path.join(MODELS_DIR, filename)
    if os.path.exists(path):
        return joblib.load(path)
    return None

def classify_qcvn(pm25_value):
    """
    Phân loại mức độ ô nhiễm theo QCVN 05:2023/BTNMT và khuyến nghị sức khỏe
    """
    if pm25_value <= 15.0:
        return "Tốt (Mức 1)", "#28a745", "Chất lượng không khí trong lành, rất tốt cho sức khỏe mọi người."
    elif pm25_value <= 25.0:
        return "Trung bình (Đạt chuẩn 24h)", "#17a2b8", "Chất lượng không khí chấp nhận được, đạt chuẩn QCVN 05:2023 trung bình 24h."
    elif pm25_value <= 50.0:
        return "Kém (Tiệm cận giới hạn 1h)", "#ffc107", "Nhóm người nhạy cảm (trẻ em, người già, người mắc bệnh hô hấp) nên hạn chế hoạt động ngoài trời kéo dài."
    elif pm25_value <= 75.0:
        return "Xấu (Vượt ngưỡng an toàn)", "#fd7e14", "Những người nhạy cảm nên tránh ra ngoài; người bình thường nên đeo khẩu trang chống bụi mịn."
    else:
        return "Nguy hại (Rất nguy hiểm)", "#dc3545", "Báo động đỏ: Toàn bộ người dân nên hạn chế tối đa ra ngoài đường."

# ==============================================================================
# GIAO DIỆN CHÍNH
# ==============================================================================
df = load_data()
metrics = load_metrics()
predictions_df = load_predictions()

# SIDEBAR: Điều hướng và thông tin hệ thống
st.sidebar.image("https://img.icons8.com/color/96/air-quality.png", width=70)
st.sidebar.title("ĐIỀU HƯỚNG HỆ THỐNG")
st.sidebar.markdown("**Đề tài:** Dự báo nồng độ bụi mịn PM2.5 tại Đà Nẵng")
st.sidebar.markdown("**Đơn vị:** ĐH Sư phạm – ĐH Đà Nẵng")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "CHỌN CHỨC NĂNG:",
    [
        "📊 1. Tổng quan chất lượng không khí",
        "🎯 2. Nhập tham số & Dự báo PM2.5",
        "📈 3. Đánh giá & So sánh mô hình ML",
        "ℹ️ 4. Giới thiệu đề tài & Tính liên ngành"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "**Thông tin dữ liệu:**\n"
    f"- Tọa độ: Đà Nẵng (16.0544°N, 108.2022°E)\n"
    f"- Số giờ quan trắc: {len(df):,} giờ\n"
    "- Nguồn: Copernicus CAMS & ERA5 (Open-Meteo API)"
)

# ------------------------------------------------------------------------------
# 1. TAB TỔNG QUAN CHẤT LƯỢNG KHÔNG KHÍ (DASHBOARD)
# ------------------------------------------------------------------------------
if menu == "📊 1. Tổng quan chất lượng không khí":
    st.title("🌫️ DASHBOARD GIÁM SÁT CHẤT LƯỢNG KHÔNG KHÍ TẠI ĐÀ NẴNG")
    st.markdown("*Hệ thống phân tích chuỗi thời gian nồng độ bụi mịn PM2.5 và vi khí hậu ven biển.*")

    # Lấy thông số bản ghi gần nhất
    latest = df.iloc[-1]
    pm_val = latest['PM25']
    status_label, status_color, status_desc = classify_qcvn(pm_val)

    # Hiển thị Metric Cards
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Nồng độ PM2.5", f"{pm_val:.1f} µg/m³", delta=f"{pm_val - 25.0:+.1f} so với QCVN")
    with col2:
        st.metric("Nhiệt độ (2m)", f"{latest['temp']:.1f} °C")
    with col3:
        st.metric("Độ ẩm tương đối", f"{latest['humidity']:.1f} %")
    with col4:
        st.metric("Tốc độ gió", f"{latest['wind_speed']:.1f} m/s")
    with col5:
        st.metric("Áp suất khí quyển", f"{latest['pressure']:.1f} hPa")

    # Thẻ cảnh báo phân cấp QCVN
    st.markdown(
        f"""
        <div style="background-color: {status_color}22; border-left: 6px solid {status_color}; padding: 12px 18px; border-radius: 6px; margin: 15px 0;">
            <h4 style="margin: 0; color: {status_color};">Mức đánh giá hiện tại: {status_label}</h4>
            <p style="margin: 5px 0 0 0; color: #333;">{status_desc}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Biểu đồ chuỗi thời gian tương tác Plotly
    st.subheader("📈 Diễn biến nồng độ PM2.5 và các yếu tố khí tượng theo thời gian")
    view_option = st.selectbox("Chọn khoảng thời gian hiển thị:", ["7 ngày gần nhất", "30 ngày gần nhất", "Toàn bộ dữ liệu (90 ngày)"])
    if view_option == "7 ngày gần nhất":
        plot_df = df.iloc[-168:]
    elif view_option == "30 ngày gần nhất":
        plot_df = df.iloc[-720:]
    else:
        plot_df = df

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=plot_df['timestamp'], y=plot_df['PM25'], name='PM2.5 (µg/m³)', line=dict(color='#1f77b4', width=2)))
    fig.add_hline(y=25, line_dash="dash", line_color="orange", annotation_text="QCVN 05:2023 TB 24h (25 µg/m³)", annotation_position="top left")
    fig.add_hline(y=50, line_dash="dash", line_color="red", annotation_text="QCVN 05:2023 TB 1h (50 µg/m³)", annotation_position="bottom left")
    fig.update_layout(title="Biến thiên nồng độ PM2.5 tại Đà Nẵng", xaxis_title="Thời gian quan trắc", yaxis_title="Nồng độ PM2.5 (µg/m³)", height=420)
    st.plotly_chart(fig, use_container_width=True)

    # Ma trận tương quan giữa khí tượng và ô nhiễm
    st.subheader("🔍 Mối tương quan giữa các yếu tố vi khí hậu ven biển và PM2.5")
    col_corr1, col_corr2 = st.columns([1, 1])
    with col_corr1:
        corr_cols = ['PM25', 'temp', 'humidity', 'wind_speed', 'pressure', 'rain']
        corr_matrix = df[corr_cols].corr().round(3)
        fig_corr = px.imshow(corr_matrix, text_auto=True, color_continuous_scale='RdBu_r', title="Ma trận hệ số tương quan Pearson")
        st.plotly_chart(fig_corr, use_container_width=True)
    with col_corr2:
        st.markdown(
            """
            **Nhận định khoa học về cơ chế vi khí hậu Đà Nẵng:**
            * **Tốc độ gió (`wind_speed`):** Tương quan nghịch có ý nghĩa thống kê cao. Gió biển thổi mạnh thúc đẩy quá trình đối lưu, thổi bay và khuếch tán nhanh chóng các hạt bụi lơ lửng.
            * **Lượng mưa (`rain`):** Tương quan nghịch thể hiện hiệu ứng *lắng đọng ướt* (wet scavenging), rửa trôi bụi mịn xuống mặt đất.
            * **Độ ẩm (`humidity`):** Tương quan thuận khi lặng gió, độ ẩm cao kích thích các hạt nhân hút ẩm phát triển làm tăng kích thước và nồng độ bụi đo được.
            * **Quán tính khí quyển:** Nồng độ giờ liền trước ($t-1$) là đặc trưng dự báo có trọng số cao nhất.
            """
        )

# ------------------------------------------------------------------------------
# 2. TAB NHẬP THAM SỐ VÀ DỰ BÁO PM2.5
# ------------------------------------------------------------------------------
elif menu == "🎯 2. Nhập tham số & Dự báo PM2.5":
    st.title("🎯 CÔNG CỤ DỰ BÁO NỒNG ĐỘ PM2.5 THEO THỜI GIAN THỰC")
    st.markdown("Nhập các tham số khí tượng và nồng độ lịch sử để mô hình Machine Learning đưa ra dự báo chính xác cho giờ tiếp theo ($t+1$).")

    # Chọn mô hình dự báo
    selected_model_name = st.selectbox(
        "Lựa chọn mô hình Machine Learning để suy luận:",
        ["XGBoost", "Random Forest", "Linear Regression"],
        index=0
    )

    model = load_model(selected_model_name)
    if model is None:
        st.error(f"Chưa tìm thấy mô hình đã huấn luyện {selected_model_name}. Vui lòng chạy lệnh `python train_model.py` trước!")
    else:
        st.write("---")
        # Nút lấy mẫu thử nghiệm nhanh từ dữ liệu thực tế
        if st.button("🎲 Lấy ngẫu nhiên thông số từ tập dữ liệu thực tế Đà Nẵng"):
            random_sample = df.sample(1).iloc[0]
            st.session_state['input_pm25_lag1'] = float(random_sample['PM25'])
            st.session_state['input_pm25_lag2'] = float(df.iloc[random_sample.name - 1]['PM25'] if random_sample.name > 0 else random_sample['PM25'])
            st.session_state['input_pm25_lag24'] = float(df.iloc[random_sample.name - 24]['PM25'] if random_sample.name >= 24 else random_sample['PM25'])
            st.session_state['input_temp'] = float(random_sample['temp'])
            st.session_state['input_humid'] = float(random_sample['humidity'])
            st.session_state['input_wind'] = float(random_sample['wind_speed'])
            st.session_state['input_pres'] = float(random_sample['pressure'])
            st.session_state['input_rain'] = float(random_sample['rain'])
            st.session_state['input_hour'] = int(random_sample['timestamp'].hour)

        # Form nhập liệu 2 cột
        col_in1, col_in2 = st.columns(2)
        with col_in1:
            st.markdown("#### 1. Thông số nồng độ quá khứ (Lag Features)")
            pm25_lag1 = st.number_input("Nồng độ PM2.5 giờ trước (t-1) [µg/m³]:", min_value=0.0, max_value=300.0, value=st.session_state.get('input_pm25_lag1', 14.5), step=0.5)
            pm25_lag2 = st.number_input("Nồng độ PM2.5 cách 2 giờ (t-2) [µg/m³]:", min_value=0.0, max_value=300.0, value=st.session_state.get('input_pm25_lag2', 15.0), step=0.5)
            pm25_lag24 = st.number_input("Nồng độ PM2.5 cùng giờ hôm qua (t-24) [µg/m³]:", min_value=0.0, max_value=300.0, value=st.session_state.get('input_pm25_lag24', 16.2), step=0.5)
            hour_val = st.slider("Giờ quan trắc trong ngày (0 - 23h):", min_value=0, max_value=23, value=st.session_state.get('input_hour', 8))

        with col_in2:
            st.markdown("#### 2. Thông số vi khí tượng mặt đất")
            temp = st.number_input("Nhiệt độ không khí (°C):", min_value=10.0, max_value=45.0, value=st.session_state.get('input_temp', 27.5), step=0.1)
            humidity = st.number_input("Độ ẩm tương đối (%):", min_value=20.0, max_value=100.0, value=st.session_state.get('input_humid', 80.0), step=1.0)
            wind_speed = st.number_input("Tốc độ gió (m/s):", min_value=0.0, max_value=30.0, value=st.session_state.get('input_wind', 3.5), step=0.1)
            pressure = st.number_input("Áp suất khí quyển (hPa):", min_value=980.0, max_value=1030.0, value=st.session_state.get('input_pres', 1010.5), step=0.5)
            rain = st.number_input("Lượng mưa tích lũy (mm):", min_value=0.0, max_value=150.0, value=st.session_state.get('input_rain', 0.0), step=0.5)

        # Tính toán các đặc trưng kỹ nghệ tự động
        pm25_roll3 = (pm25_lag1 + pm25_lag2 + pm25_lag1) / 3.0  # ước lượng xấp xỉ
        pm25_roll24 = (pm25_lag1 + pm25_lag24) / 2.0
        hour_sin = np.sin(2 * np.pi * hour_val / 24.0)
        hour_cos = np.cos(2 * np.pi * hour_val / 24.0)

        # Vector đặc trưng đầu vào đúng thứ tự huấn luyện
        input_vector = pd.DataFrame([{
            'PM25_lag1': pm25_lag1,
            'PM25_lag2': pm25_lag2,
            'PM25_lag24': pm25_lag24,
            'PM25_roll3': pm25_roll3,
            'PM25_roll24': pm25_roll24,
            'temp': temp,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'pressure': pressure,
            'rain': rain,
            'hour_sin': hour_sin,
            'hour_cos': hour_cos
        }])

        st.write("")
        if st.button("🚀 TIẾN HÀNH DỰ BÁO NGAY", type="primary", use_container_width=True):
            pred_value = float(model.predict(input_vector)[0])
            pred_value = max(0.0, pred_value)
            pred_status, pred_color, pred_rec = classify_qcvn(pred_value)

            st.write("---")
            st.subheader("📋 KẾT QUẢ DỰ BÁO NỒNG ĐỘ PM2.5 (GIỜ TIẾP THEO)")
            res_c1, res_c2 = st.columns([1, 2])
            with res_c1:
                st.markdown(
                    f"""
                    <div style="background-color: #f8f9fa; border: 2px solid {pred_color}; border-radius: 10px; padding: 20px; text-align: center;">
                        <span style="font-size: 14px; color: #666; font-weight: bold;">KẾT QUẢ DỰ BÁO BỞI {selected_model_name.upper()}</span>
                        <h1 style="color: {pred_color}; font-size: 48px; margin: 10px 0;">{pred_value:.2f}</h1>
                        <span style="font-size: 16px; color: #444; font-weight: bold;">µg/m³</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with res_c2:
                st.markdown(
                    f"""
                    <div style="background-color: {pred_color}18; border-left: 6px solid {pred_color}; border-radius: 6px; padding: 16px 20px;">
                        <h3 style="color: {pred_color}; margin-top: 0;">Đánh giá cấp độ: {pred_status}</h3>
                        <p style="font-size: 15px; line-height: 1.5; color: #222;"><b>Khuyến nghị sức khỏe:</b> {pred_rec}</p>
                        <hr style="margin: 10px 0; border: none; border-top: 1px solid #ddd;">
                        <p style="font-size: 13px; color: #555; margin: 0;"><b>Tiêu chuẩn đối chiếu:</b> QCVN 05:2023/BTNMT - Quy chuẩn kỹ thuật quốc gia về chất lượng không khí xung quanh.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# ------------------------------------------------------------------------------
# 3. TAB ĐÁNH GIÁ VÀ SO SÁNH CÁC MÔ HÌNH HỌC MÁY
# ------------------------------------------------------------------------------
elif menu == "📈 3. Đánh giá & So sánh mô hình ML":
    st.title("📈 ĐÁNH GIÁ HIỆU NĂNG VÀ ĐỐI CHỨNG CÁC MÔ HÌNH HỌC MÁY")
    st.markdown("So sánh định lượng 3 thuật toán (Linear Regression, Random Forest, XGBoost) trên tập dữ liệu kiểm thử độc lập gồm **431 giờ quan trắc thực tế** tại Đà Nẵng.")

    # 1. Bảng số liệu chỉ số MAE, RMSE, R2
    st.subheader("1. Bảng chỉ số đánh giá sai số chuẩn hóa (Evaluation Metrics)")
    if metrics:
        metrics_df = pd.DataFrame(metrics).T
        metrics_df.columns = ["MAE (µg/m³)", "RMSE (µg/m³)", "R² Score"]
        st.dataframe(metrics_df.style.highlight_min(subset=["MAE (µg/m³)", "RMSE (µg/m³)"], color='#d4edda')
                                      .highlight_max(subset=["R² Score"], color='#cce5ff'), use_container_width=True)

        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1:
            st.metric("Linear Regression R²", f"{metrics.get('Linear Regression', {}).get('R2', 0):.4f}", f"MAE: {metrics.get('Linear Regression', {}).get('MAE', 0):.3f}")
        with m_col2:
            st.metric("Random Forest R²", f"{metrics.get('Random Forest', {}).get('R2', 0):.4f}", f"MAE: {metrics.get('Random Forest', {}).get('MAE', 0):.3f}")
        with m_col3:
            st.metric("XGBoost R² (Tối ưu)", f"{metrics.get('XGBoost', {}).get('R2', 0):.4f}", f"MAE: {metrics.get('XGBoost', {}).get('MAE', 0):.3f}")

    # 2. Đồ thị so sánh thực tế vs dự báo
    st.subheader("2. Biểu đồ tương tác đối chứng Thực tế và Dự báo trên tập Test")
    if predictions_df is not None:
        fig_comp = go.Figure()
        fig_comp.add_trace(go.Scatter(x=predictions_df['timestamp'], y=predictions_df['Actual_PM25'], name='Thực tế (Quan trắc)', line=dict(color='#1f77b4', width=2.5)))
        fig_comp.add_trace(go.Scatter(x=predictions_df['timestamp'], y=predictions_df['Linear Regression'], name='Linear Regression', line=dict(color='#7f7f7f', width=1, dash='dot')))
        fig_comp.add_trace(go.Scatter(x=predictions_df['timestamp'], y=predictions_df['Random Forest'], name='Random Forest', line=dict(color='#2ca02c', width=1.5, dash='dash')))
        fig_comp.add_trace(go.Scatter(x=predictions_df['timestamp'], y=predictions_df['XGBoost'], name='XGBoost Regressor', line=dict(color='#d62728', width=2)))

        fig_comp.add_hline(y=25, line_dash="dash", line_color="orange", annotation_text="QCVN 05:2023 TB 24h (25 µg/m³)")
        fig_comp.update_layout(title="Đối chứng kết quả dự báo trên 431 giờ kiểm thử độc lập", xaxis_title="Thời gian", yaxis_title="PM2.5 (µg/m³)", height=450)
        st.plotly_chart(fig_comp, use_container_width=True)

        # Cho phép tải dữ liệu dự báo CSV
        csv_data = predictions_df.to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            label="📥 Tải xuống tệp CSV kết quả dự báo chi tiết",
            data=csv_data,
            file_name="danang_pm25_model_predictions.csv",
            mime="text/csv"
        )

    # 3. Mức độ quan trọng đặc trưng (Feature Importance)
    st.subheader("3. Mức độ quan trọng của các đặc trưng môi trường (Feature Importance)")
    feat_img = os.path.join(OUTPUTS_DIR, "feature_importance.png")
    if os.path.exists(feat_img):
        st.image(feat_img, caption="Trọng số đóng góp của các đặc trưng vào mô hình học máy", use_container_width=True)

# ------------------------------------------------------------------------------
# 4. TAB GIỚI THIỆU ĐỀ TÀI VÀ TÍNH LIÊN NGÀNH
# ------------------------------------------------------------------------------
elif menu == "ℹ️ 4. Giới thiệu đề tài & Tính liên ngành":
    st.title("ℹ️ THÔNG TIN ĐỀ TÀI VÀ LUẬN CỨ LIÊN NGÀNH")
    st.markdown("### Học phần: Phương pháp nghiên cứu khoa học trong Khoa học tự nhiên")
    st.markdown("**Đề tài lựa chọn:** Đề số 5 – Xây dựng đề cương nghiên cứu liên ngành cho một vấn đề thực tiễn của địa phương.")

    col_info1, col_info2 = st.columns(2)
    with col_info1:
        st.markdown(
            """
            #### 🌿 Vai trò của Khoa học Môi trường:
            * Cung cấp cơ sở lý luận về bản chất phân tán bụi mịn $\text{PM}_{2.5}$ trong tầng đối lưu.
            * Luận giải sự tương tác của gió biển, độ ẩm và mưa đặc thù vùng ven biển Đà Nẵng.
            * Xác lập ngưỡng tiêu chuẩn đối chứng theo **QCVN 05:2023/BTNMT**.
            """
        )
    with col_info2:
        st.markdown(
            """
            #### 💻 Vai trò của Công nghệ thông tin:
            * Thu thập, chuẩn hóa chuỗi dữ liệu lớn thời gian thực từ API mở theo chuẩn FAIR.
            * Kỹ nghệ đặc trưng trễ và chu kỳ không làm rò rỉ dữ liệu (`TimeSeriesSplit`).
            * Xây dựng, huấn luyện mô hình học máy (XGBoost, Random Forest) và phát triển ứng dụng Streamlit phục vụ cộng đồng.
            """
        )

    st.write("---")
    st.markdown(
        """
        ### 👨‍🎓 Tác giả thực hiện:
        * **Sinh viên:** Khoa Công nghệ thông tin – Trường Đại học Sư phạm, Đại học Đà Nẵng.
        * **Địa chỉ triển khai:** Thành phố Đà Nẵng, Việt Nam.
        * **Cam kết liêm chính:** Dữ liệu hoàn toàn thực tế, nguồn mở công khai, mã nguồn có thể tái lập 100%.
        """
    )

