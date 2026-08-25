import mgba
import time

def test_move(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    print(f"Tried {direction}: {pos_before} -> {pos_after}")
    return pos_after

# Starting at (17, 7) on 1F West
# Walk Left to Column 5
for _ in range(12):
    test_move("Left")

# Test Down on Column 5, 4, 3
for col in [5, 4, 3]:
    pos = mgba.get_coordinates()
    print(f"At column {pos['x']}, testing Down...")
    pos_down = test_move("Down")
    if pos_down != pos:
        print(f"Found open vertical path DOWN at Column {pos['x']}!")
        break
    # Walk Left to next column
    if col > 3:
        test_move("Left")
