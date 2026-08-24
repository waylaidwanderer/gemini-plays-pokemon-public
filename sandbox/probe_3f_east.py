import mgba
import time

def test_move(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    print(f"Tried {direction}: {pos_before} -> {pos_after}")
    return pos_after

# Starting at (22, 6)
# 1. Try Up to (22, 5)
pos = test_move("Up")
if pos == {"x": 22, "y": 5}:
    test_move("Down") # Move back to (22, 6)

# 2. Move Left to (21, 6) and try Up to (21, 5)
pos = test_move("Left")
if pos == {"x": 21, "y": 6}:
    pos_up = test_move("Up")
    if pos_up == {"x": 21, "y": 5}:
        test_move("Down") # back to (21, 6)
    test_move("Right") # back to (22, 6)

# 3. Move Left, Left to (20, 6) and try Up to (20, 5)
pos = test_move("Left")
if pos == {"x": 21, "y": 6}:
    pos2 = test_move("Left")
    if pos2 == {"x": 20, "y": 6}:
        pos_up = test_move("Up")
        if pos_up == {"x": 20, "y": 5}:
            test_move("Down")
        test_move("Right")
    test_move("Right")
