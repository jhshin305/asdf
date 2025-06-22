import controlServo
import detectLight
import detectType
import jetson2firebase
import playSound

openDegree = 90  # 쓰레기통 열기 각도
closeDegree = 0  # 쓰레기통 닫기 각도

servoIndex = {'plastic': 0, 'paper': 1, 'can': 2, 'food': 3}  # 쓰레기 종류별 서보 인덱스
lightIndex = {'plastic': 0, 'paper': 1, 'can': 2, 'food': 3}  # 쓰레기 종류별 조도 센서 인덱스

def main():
	while True:
		trash_type = detectType.detect_type()
		if trash_type is None:
			print("쓰레기통이 비어있거나 인식할 수 없습니다.")
			continue
		print(f"인식된 쓰레기 종류: {trash_type}")
		playSound.play_sound(trash_type)
		controlServo.spin_servo(servoIndex[trash_type], openDegree)  # 쓰레기통 열기
		detectLight.wait_pass()
		controlServo.spin_servo(servoIndex[trash_type], closeDegree) # 쓰레기통 닫기
		print("쓰레기통이 닫혔습니다.")

		jetson2firebase.send_log(trash_type)  # Firebase에 로그 전송
		jetson2firebase.update_count(trash_type)  # Firebase에 쓰레기통 상태 업데이트
		
		# 쓰레기통이 가득 찼는지 확인
		print("쓰레기통이 가득 찼는지 확인 중...")
		isFull = detectLight.detect_full(lightIndex[trash_type])
		if isFull:
			print("쓰레기통이 가득 찼습니다. 관리자에게 알림을 전송합니다.")
			jetson2firebase.update_full(trash_type, True)
			jetson2firebase.send_alert(trash_type)  # 관리자에게 알림 전송
		else:
			print("쓰레기통이 가득 차지 않았습니다.")
