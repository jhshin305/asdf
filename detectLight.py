from smbus2 import SMBus
import time

bus = SMBus(0)  # Jetson의 I2C-0 버스

MUX_ADDR = 0x70
CHANNEL_7 = 0x80
SENSOR_ADDR = 0x10

notFullLux = 3000  # 조도 기준값 (1000 lux)

def detect_light(channel):
	bus.write_byte(MUX_ADDR, channel)
	# time.sleep(0.1)

	bus.write_word_data(SENSOR_ADDR, 0x00, 0x0000)  # VEML7700 초기화 (ALS enable)
	# time.sleep(0.5)

	data = bus.read_word_data(SENSOR_ADDR, 0x04)  # ALS 결과 (16비트)
	als_raw = ((data & 0xFF) << 8) | (data >> 8)  # 리틀엔디안 → 빅엔디안 변환
	lux = als_raw * 0.0576  # 변환 계수 (기본 설정 기준)

	print(f"조도: {lux:.2f} lux")
	return lux

def detect_full(channel):
	bus.write_byte(MUX_ADDR, channel)
	# time.sleep(0.1)

	bus.write_word_data(SENSOR_ADDR, 0x00, 0x0000)  # VEML7700 초기화 (ALS enable)
	# time.sleep(0.5)

	data = bus.read_word_data(SENSOR_ADDR, 0x04)  # ALS 결과 (16비트)
	als_raw = ((data & 0xFF) << 8) | (data >> 8)  # 리틀엔디안 → 빅엔디안 변환
	lux = als_raw * 0.0576  # 변환 계수 (기본 설정 기준)

	if(lux > notFullLux):
		print(f"조도: {lux:.2f} lux - 쓰레기통이 가득 차지 않았습니다.")
		return False
	else:
		print(f"조도: {lux:.2f} lux - 쓰레기통이 가득 찼습니다.")
		return True

def wait_pass(channel):
	bus.write_byte(MUX_ADDR, channel)
	# time.sleep(0.1)

	bus.write_word_data(SENSOR_ADDR, 0x00, 0x0000)  # VEML7700 초기화 (ALS enable)
	# time.sleep(0.5)

	data = bus.read_word_data(SENSOR_ADDR, 0x04)  # ALS 결과 (16비트)
	als_raw = ((data & 0xFF) << 8) | (data >> 8)  # 리틀엔디안 → 빅엔디안 변환
	lux = als_raw * 0.0576  # 변환 계수 (기본 설정 기준)

	print(f"쓰레기통 {channel} 통과 대기 중")

	while(lux > notFullLux):
		data = bus.read_word_data(SENSOR_ADDR, 0x04)
		als_raw = ((data & 0xFF) << 8) | (data >> 8)
		lux = als_raw * 0.0576  # 변환 계수 (기본 설정 기준)
		# time.sleep(0.1)
	
	print(f"쓰레기통 {channel} 통과 완료")
	return

# TCA9548A 채널 7 선택
# bus.write_byte(MUX_ADDR, CHANNEL_7)
# time.sleep(0.1)

# # VEML7700 초기화 (ALS enable)
# bus.write_word_data(SENSOR_ADDR, 0x00, 0x0000)  # Power on
# time.sleep(0.5)

# # 조도 데이터 읽기
# data = bus.read_word_data(SENSOR_ADDR, 0x04)  # ALS 결과 (16비트)

# # 데이터 정리 (리틀엔디안 → 빅엔디안 변환)
# als_raw = ((data & 0xFF) << 8) | (data >> 8)

# # 변환 계수 (기본 설정 기준)
# lux = als_raw * 0.0576

# print(f"조도: {lux:.2f} lux")