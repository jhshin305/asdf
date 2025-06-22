import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import controlServo as cs

while True:
	c = input("Enter command (spin_servo, exit): ").strip().lower()
	if c == "spin_servo":
		servo_index = int(input("Enter servo index (0-3): ").strip())
		degree = int(input("Enter degree (0-180): ").strip())
		cs.spin_servo(servo_index, degree)
	elif c == "exit":
		break
	else:
		print("Invalid command. Please try again.")