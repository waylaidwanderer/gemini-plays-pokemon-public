import time
import bridge

print("Burning final 10 steps with 450ms delay to trigger Safari Zone expulsion...")

buttons = []
for i in range(10):
    direction = "Up" if i % 2 == 0 else "Down"
    buttons.append(direction)
    buttons.append("sleep 450")

bridge.press_buttons(buttons)
time.sleep(2.0) # Wait for expulsion warp and dialogue

coords = bridge.get_coordinates()
print(f"Coordinates after final expulsion: {coords}")
