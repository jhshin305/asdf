from smbus2 import SMBus
import time

bus = SMBus(0)  # Jetson의 I2C-0 버스

MUX_ADDR = 0x70
CHANNEL_7 = 0x80
SENSOR_ADDR = 0x10

# TCA9548A 채널 7 선택
bus.write_byte(MUX_ADDR, CHANNEL_7)
time.sleep(0.1)

# VEML7700 초기화 (ALS enable)
bus.write_word_data(SENSOR_ADDR, 0x00, 0x0000)  # Power on
time.sleep(0.5)

# 조도 데이터 읽기
data = bus.read_word_data(SENSOR_ADDR, 0x04)  # ALS 결과 (16비트)

# 데이터 정리 (리틀엔디안 → 빅엔디안 변환)
als_raw = ((data & 0xFF) << 8) | (data >> 8)

# 변환 계수 (기본 설정 기준)
lux = als_raw * 0.0576

print(f"조도: {lux:.2f} lux")
