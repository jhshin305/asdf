import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import detectLight as dl

while True:
	c = input("Enter command (detect_light, wait_pass, detect_full, exit): ").strip().lower()
	if c == "detect_light":
		light_index = int(input("Enter light index (0-3): ").strip())
		result = dl.detect_light(light_index)
		print(f"Light detected: {result}")
	elif c == "wait_pass":
		dl.wait_pass()
		print("Waiting for pass...")
	elif c == "detect_full":
		light_index = int(input("Enter light index (0-3): ").strip())
		result = dl.detect_full(light_index)
		print(f"Is full: {result}")
	elif c == "exit":
		break
	else:
		print("Invalid command. Please try again.")