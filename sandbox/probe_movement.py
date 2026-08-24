import mgba
import time

def test_move(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    print(f"Tried {direction}: {pos_before} -> {pos_after}")
    return pos_after

# We are at (5, 10)
# Let's test moving Left, then Right (back to 5, 10)
pos = test_move("Left")
if pos == {"x": 4, "y": 10}:
    test_move("Right")

# Let's test moving Up, then Down
pos = test_move("Up")
if pos == {"x": 5, "y": 9}:
    test_move("Down")
