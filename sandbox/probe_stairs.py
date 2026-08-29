import mgba
import time

def move_test(step):
    pos_before = mgba.get_coordinates()
    print(f"probe: Pressing '{step}' from {pos_before}...")
    mgba.press_buttons([step])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    if pos_before != pos_after:
        print(f"probe: MOVED to {pos_after}!")
        return pos_after
    else:
        print("probe: Did not move.")
        return None

def test_stairs():
    # We are at (24, 3)
    pos = mgba.get_coordinates()
    print(f"test_stairs: Starting at {pos}")
    
    # Walk Left to (23, 3)
    pos = move_test("Left")
    if not pos: return
    
    # Walk Left to (22, 3)
    pos = move_test("Left")
    if not pos: return
    
    # Step Up to (22, 2)
    pos_up = move_test("Up")
    if pos_up:
        print(f"test_stairs: Walked UP to {pos_up}!")
    else:
        print("test_stairs: (22, 2) is BLOCKED/SOLID.")

if __name__ == "__main__":
    test_stairs()
