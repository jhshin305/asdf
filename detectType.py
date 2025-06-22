def detect_type():
	t = input("쓰레기 종류를 입력하세요 (plastic, paper, can, food): ").strip().lower()
	if t in ['plastic', 'paper', 'can', 'food']:
		return t
	else:
		print("알 수 없는 쓰레기 종류입니다.")
		return 'unknown'