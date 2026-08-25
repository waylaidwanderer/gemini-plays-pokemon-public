import mgba
import time

def test_move(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    print(f"Tried {direction}: {pos_before} -> {pos_after}")
    return pos_after

# Starting at (10, 7) on 1F West
# Let's walk Right and check if we can go Down at any column from 10 to 17
for col in range(10, 18):
    pos = mgba.get_coordinates()
    print(f"At column {pos['x']}, testing Down...")
    pos_down = test_move("Down")
    if pos_down != pos:
        print(f"Found open vertical path DOWN at Column {pos['x']}!")
        break
    # Walk Right to next column
    if col < 17:
        pos_right = test_move("Right")
        if pos_right == pos:
            print(f"Blocked walking Right at Column {pos['x']}!")
            break
