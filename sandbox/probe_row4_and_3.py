import mgba
import time

# 1. Dismiss the "Got away safely!" screen
mgba.press_buttons(["B"])
time.sleep(1.5) # Wait for fade back to overworld

def test_move(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    print(f"Tried {direction}: {pos_before} -> {pos_after}")
    return pos_after

# Starting at (19, 4) on 3F East
# 2. Test Left to (18, 4)
pos_left = test_move("Left")
if pos_left == {"x": 18, "y": 4}:
    # Test Up to (18, 3)
    pos_up = test_move("Up")
    if pos_up == {"x": 18, "y": 3}:
        test_move("Down") # Back to (18, 4)
    test_move("Right") # Back to (19, 4)

# 3. Test Right to (20, 4)
pos_right = test_move("Right")
if pos_right == {"x": 20, "y": 4}:
    # Test Up to (20, 3)
    pos_up = test_move("Up")
    if pos_up == {"x": 20, "y": 3}:
        test_move("Down") # Back to (20, 4)
    test_move("Left") # Back to (19, 4)
