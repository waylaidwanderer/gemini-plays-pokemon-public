import mgba
import time

def try_move(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        print(f"{direction}: BLOCKED")
        return False
    else:
        print(f"{direction}: SUCCESS to ({pos_after['x']}, {pos_after['y']})")
        opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[direction]
        mgba.press_buttons([opposite])
        time.sleep(0.3)
        return True

print("Probing from current position:")
try_move("Left")
try_move("Right")
try_move("Up")
try_move("Down")
