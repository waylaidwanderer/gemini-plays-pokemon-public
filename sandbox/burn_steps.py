import time
import bridge

print("Burning final steps to trigger expulsion...")

buttons = []
for i in range(10):
    direction = "Up" if i % 2 == 0 else "Down"
    buttons.append(direction)
    buttons.append("sleep 50")

bridge.press_buttons(buttons)
time.sleep(2.0) # Wait for expulsion warp and PA system dialogue to start

coords = bridge.get_coordinates()
print(f"Current Coordinates after final burn: {coords}")
