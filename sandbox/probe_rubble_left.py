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

def test_rubble_left():
    # We are at (22, 3)
    print(f"Starting test_rubble_left from {mgba.get_coordinates()}")
    
    # 1. Walk Left to (20, 3)
    move_test("Left")
    move_test("Left")
    
    # 2. Walk Down to (20, 4)
    move_test("Down")
    
    # 3. Walk Left to (19, 4)
    move_test("Left")
    
    # 4. Walk Down to (19, 5) then (19, 6)
    move_test("Down")
    move_test("Down")
    
    # 5. Walk Right along Row 6 to Column 22
    move_test("Right")
    move_test("Right")
    move_test("Right")
    
    pos = mgba.get_coordinates()
    print(f"Now at {pos}. Testing Column 23 Row 6 (23, 6)...")
    
    # Test Right into (23, 6)
    pos_right = move_test("Right")
    if pos_right:
        # Check if we fell (y is not 6)
        if pos_right['y'] != 6:
            print(f"probe: FELL THROUGH (23, 6)! Pos: {pos_right}")
            return
        else:
            print("probe: (23, 6) is walkable floor!")
            # Try Right into (24, 6)
            pos_right2 = move_test("Right")
            if pos_right2:
                if pos_right2['y'] != 6:
                    print(f"probe: FELL THROUGH (24, 6)! Pos: {pos_right2}")
                    return
                else:
                    print("probe: (24, 6) is walkable floor!")
                    # Try Right into (25, 6)
                    pos_right3 = move_test("Right")
                    if pos_right3:
                        if pos_right3['y'] != 6:
                            print(f"probe: FELL THROUGH (25, 6)! Pos: {pos_right3}")
                            return
                        else:
                            print("probe: (25, 6) is walkable floor!")
                    else:
                        print("probe: (25, 6) is solid.")
                    move_test("Left")
                move_test("Left")
            else:
                print("probe: (24, 6) is solid.")
            move_test("Left")
    else:
        print("probe: (23, 6) is solid.")

if __name__ == "__main__":
    test_rubble_left()
