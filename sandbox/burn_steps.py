import time
import bridge

print("Burning 90 steps...")

buttons = []
for i in range(90):
    direction = "Up" if i % 2 == 0 else "Down"
    buttons.append(direction)
    buttons.append("sleep 50")

bridge.press_buttons(buttons)
time.sleep(1.0)

coords = bridge.get_coordinates()
print(f"Current Coordinates: {coords}")
