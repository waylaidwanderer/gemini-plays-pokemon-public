import mgba
import time

print("Pressing B multiple times to clear text...")
for i in range(5):
    mgba.press_buttons(["B"])
    time.sleep(0.3)

time.sleep(0.5)
print("Checking position...")
pos = mgba.get_coordinates()
print("Position:", pos)
mgba.take_screenshot()
