from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

# sudo groupadd -f gpio
# sudo chown root:gpio /dev/gpiochip*
# sudo chmod g+rw /dev/gpiochip*

def spin_servo(servo_index, angle):
	kit.servo[servo_index].angle = angle
	print(f"Servo {servo_index} moved to {angle} degrees")
	time.sleep(1)


# for i in range(10):
# 	print("Move to 0")
# 	kit.servo[0].angle = 0
# 	kit.servo[4].angle = 0
# 	kit.servo[8].angle = 0
# 	kit.servo[12].angle = 0
# 	time.sleep(10)

# 	# print("Move to 90")
# 	# kit.servo[0].angle = 90
# 	# kit.servo[4].angle = 90
# 	# kit.servo[8].angle = 90
# 	# kit.servo[12].angle = 90
# 	# time.sleep(1)

# 	print("Move to 180")
# 	kit.servo[0].angle = 180
# 	kit.servo[4].angle = 180
# 	kit.servo[8].angle = 180
# 	kit.servo[12].angle = 180
# 	time.sleep(10)

# 	# print("Move to 270")
# 	# # kit.servo[0].angle = 270
# 	# # kit.servo[4].angle = 270
# 	# # kit.servo[8].angle = 270
# 	# kit.servo[12].angle = 270
# 	# time.sleep(1)

# 	# print("Move to 360")
# 	# kit.servo[12].angle = 360
# 	# time.sleep(1)

# print("Done")
