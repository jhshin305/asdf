import playsound

def play_sound(binType):
	"""
	지정된 쓰레기 종류에 따라 사운드를 재생합니다.
	
	:param binType: 쓰레기 종류 (plastic, paper, metal, food)
	"""
	sound_files = {
		'plastic': 'sounds/plastic.mp3',
		'paper': 'sounds/paper.mp3',
		'metal': 'sounds/metal.mp3',
		'food': 'sounds/food.mp3',
		'unknown': 'sounds/unknown.mp3'
	}
	
	if binType in sound_files:
		playsound.playsound(sound_files[binType])
		print(f"{binType} 사운드를 재생합니다.")
	else:
		print(f"알 수 없는 쓰레기 종류: {binType}. 사운드를 재생할 수 없습니다.")