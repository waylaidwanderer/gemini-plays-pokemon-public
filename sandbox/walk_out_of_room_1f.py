import mgba
import time

def test_move(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    print(f"Tried {direction}: {pos_before} -> {pos_after}")
    return pos_after

# Starting at (2, 3) on 1F West
# Walk Down as much as possible on Column 2
curr = mgba.get_coordinates()
while True:
    pos = test_move("Down")
    if pos == curr:
        print("Blocked walking Down. Final position:", pos)
        break
    curr = pos
