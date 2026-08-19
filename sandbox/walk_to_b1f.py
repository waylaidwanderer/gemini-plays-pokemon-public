import mgba
import time

print("Going to 1F...")
pos = mgba.get_coordinates()
print("Starting position:", pos)

if pos['x'] == 7 and pos['y'] == 11:
    print("Moving Up to (7, 10) to warp to 1F...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
print("New position:", mgba.get_coordinates())
mgba.take_screenshot()
