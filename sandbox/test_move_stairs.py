import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    print("Position:", pos)
    return pos

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

print("Attempting to step UP onto the stairs at (5, 10)...")
mgba.press_buttons(["Up"])
time.sleep(1.5)

pos = check_pos()
if pos != {"x": 5, "y": 11}:
    print("Warped or moved! New position:", pos)
else:
    print("Blocked! We are still at (5, 11).")

mgba.take_screenshot()
