import time
import bridge

print("Starting test_row21.py...")

# Try walking RIGHT along row 21
for i in range(20):
    pos = bridge.get_coordinates()
    print(f"At {pos}, pressing Right...")
    bridge.press_buttons(["Right"])
    time.sleep(0.7)

pos = bridge.get_coordinates()
print(f"Final coordinates: {pos}")
