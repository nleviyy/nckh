"""
Script tải và hợp nhất dữ liệu thực tế chất lượng không khí (PM2.5) và vi khí tượng tại Đà Nẵng.
Nguồn dữ liệu: Open-Meteo Air Quality & Weather API (Dữ liệu quan trắc vệ tinh CAMS/ECMWF và trạm mặt đất).
Tọa độ Đà Nẵng: 16.0544° N, 108.2022° E.
"""

import os
import json
import urllib.request
import pandas as pd
import numpy as np

def fetch_real_data():
    lat = 16.0544
    lon = 108.2022
    past_days = 90  # Lấy 90 ngày quan trắc gần nhất (~2.160 giờ thực tế)

    print(f"[*] Đang tải dữ liệu thực tế cho Đà Nẵng (Lat: {lat}, Lon: {lon}) trong {past_days} ngày qua...")

    # 1. Tải dữ liệu chất lượng không khí (PM2.5, PM10, CO, NO2)
    aq_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&hourly=pm2_5,pm10,carbon_monoxide,nitrogen_dioxide&timezone=Asia%2FBangkok&past_days={past_days}"
    req_aq = urllib.request.urlopen(aq_url, timeout=20)
    aq_json = json.loads(req_aq.read().decode('utf-8'))
    df_aq = pd.DataFrame(aq_json['hourly'])
    df_aq['time'] = pd.to_datetime(df_aq['time'])
    df_aq = df_aq.rename(columns={'time': 'timestamp', 'pm2_5': 'PM25'})

    # 2. Tải dữ liệu khí tượng bề mặt (Nhiệt độ, Độ ẩm, Tốc độ gió, Hướng gió, Áp suất, Mưa)
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,relative_humidity_2m,surface_pressure,wind_speed_10m,wind_direction_10m,precipitation&timezone=Asia%2FBangkok&past_days={past_days}"
    req_weather = urllib.request.urlopen(weather_url, timeout=20)
    weather_json = json.loads(req_weather.read().decode('utf-8'))
    df_weather = pd.DataFrame(weather_json['hourly'])
    df_weather['time'] = pd.to_datetime(df_weather['time'])
    df_weather = df_weather.rename(columns={
        'time': 'timestamp',
        'temperature_2m': 'temp',
        'relative_humidity_2m': 'humidity',
        'surface_pressure': 'pressure',
        'wind_speed_10m': 'wind_speed',
        'wind_direction_10m': 'wind_dir',
        'precipitation': 'rain'
    })

    # 3. Hợp nhất hai nguồn dữ liệu theo mốc thời gian timestamp
    merged = pd.merge(df_aq, df_weather, on='timestamp', how='inner')
    
    # Loại bỏ các thời điểm tương lai (nếu API trả về dự báo)
    now = pd.Timestamp.now(tz='Asia/Bangkok').tz_localize(None)
    merged = merged[merged['timestamp'] <= now]

    # Xử lý các giá trị khuyết (nếu có) bằng nội suy tuyến tính
    merged['PM25'] = merged['PM25'].interpolate(method='linear').ffill().bfill()
    merged['temp'] = merged['temp'].interpolate(method='linear').ffill().bfill()
    merged['humidity'] = merged['humidity'].interpolate(method='linear').ffill().bfill()
    merged['wind_speed'] = merged['wind_speed'].interpolate(method='linear').ffill().bfill()
    merged['wind_dir'] = merged['wind_dir'].interpolate(method='linear').ffill().bfill()
    merged['pressure'] = merged['pressure'].interpolate(method='linear').ffill().bfill()
    merged['rain'] = merged['rain'].fillna(0.0)

    # Làm tròn số liệu cho chuẩn quan trắc
    merged['PM25'] = merged['PM25'].round(2)
    merged['temp'] = merged['temp'].round(1)
    merged['humidity'] = merged['humidity'].round(1)
    merged['wind_speed'] = merged['wind_speed'].round(1)
    merged['wind_dir'] = merged['wind_dir'].round(0)
    merged['pressure'] = merged['pressure'].round(1)
    merged['rain'] = merged['rain'].round(1)

    # Lưu tập tin
    data_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(data_dir, "danang_real_air_quality.csv")
    merged.to_csv(output_path, index=False, encoding='utf-8')

    print(f"[+] Đã tải và lưu thành công {len(merged)} dòng dữ liệu thực tế tại: {output_path}")
    print(merged.head())
    print("\nThống kê mô tả dữ liệu PM2.5 thực tế:")
    print(merged['PM25'].describe())

if __name__ == "__main__":
    fetch_real_data()

