import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import jetson2firebase as j2f

while True:
    c = input("Enter command (update_count, send_log, new_send_alert, update_full, exit): ").strip().lower()
    if c == "update_count":
        bin_type = input("Enter bin type (plastic, glass, paper, can): ").strip().lower()
        j2f.update_count(bin_type)
    elif c == "send_log":
        bin_type = input("Enter bin type (plastic, glass, paper, can): ").strip().lower()
        j2f.send_log(bin_type)
    elif c == "new_send_alert":
        bin_type = input("Enter bin type (plastic, glass, paper, can): ").strip().lower()
        j2f.new_send_alert(bin_type)
    elif c == "update_full":
        bin_type = input("Enter bin type (plastic, glass, paper, can): ").strip().lower()
        j2f.update_full(bin_type)
    elif c == "exit":
        break
    else:
        print("Invalid command. Please try again.")