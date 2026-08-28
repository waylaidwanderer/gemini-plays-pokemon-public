import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    return pos

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

print("Attempting to step UP onto the stairs at (7, 10)...")
mgba.press_buttons(["Up"])
time.sleep(2.0)

pos = check_pos()
if pos != {"x": 7, "y": 11}:
    print("Successfully stayed on 3F West! New position:", pos)
else:
    print("Warped up and immediately warped back down (State A block) or blocked!")

mgba.take_screenshot()
