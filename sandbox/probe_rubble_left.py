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

def test_rubble_row_7():
    # We start at (22, 6)
    print(f"Starting test_rubble_row_7 from {mgba.get_coordinates()}")
    
    # 1. Walk down to (22, 7)
    pos = move_test("Down")
    if not pos: return
    
    # 2. Test Right into (23, 7)
    print("Testing (23, 7)...")
    pos_right = move_test("Right")
    if pos_right:
        if pos_right['y'] != 7:
            print(f"probe: FELL THROUGH (23, 7)! Pos: {pos_right}")
            return
        else:
            print("probe: (23, 7) is walkable floor!")
            
            # Test UP into (23, 6) from (23, 7)
            print("Testing (23, 6) from (23, 7)...")
            pos_up = move_test("Up")
            if pos_up:
                if pos_up['y'] != 6:
                    print(f"probe: FELL THROUGH (23, 6)! Pos: {pos_up}")
                    return
                else:
                    print("probe: (23, 6) is walkable floor!")
                    move_test("Down")
                    
            # Test Right into (24, 7) from (23, 7)
            print("Testing (24, 7)...")
            pos_right2 = move_test("Right")
            if pos_right2:
                if pos_right2['y'] != 7:
                    print(f"probe: FELL THROUGH (24, 7)! Pos: {pos_right2}")
                    return
                else:
                    print("probe: (24, 7) is walkable floor!")
                    
                    # Test UP into (24, 6) from (24, 7)
                    print("Testing (24, 6) from (24, 7)...")
                    pos_up2 = move_test("Up")
                    if pos_up2:
                        if pos_up2['y'] != 6:
                            print(f"probe: FELL THROUGH (24, 6)! Pos: {pos_up2}")
                            return
                        else:
                            print("probe: (24, 6) is walkable floor!")
                            move_test("Down")
                            
                    # Test Right into (25, 7) from (24, 7)
                    print("Testing (25, 7)...")
                    pos_right3 = move_test("Right")
                    if pos_right3:
                        if pos_right3['y'] != 7:
                            print(f"probe: FELL THROUGH (25, 7)! Pos: {pos_right3}")
                            return
                        else:
                            print("probe: (25, 7) is walkable floor!")
                            
                            # Test UP into (25, 6) from (25, 7)
                            print("Testing (25, 6) from (25, 7)...")
                            pos_up3 = move_test("Up")
                            if pos_up3:
                                if pos_up3['y'] != 6:
                                    print(f"probe: FELL THROUGH (25, 6)! Pos: {pos_up3}")
                                    return
                                else:
                                    print("probe: (25, 6) is walkable floor!")
                                    move_test("Down")
                                    
                            # Test Right into (26, 7) from (25, 7)
                            print("Testing (26, 7)...")
                            pos_right4 = move_test("Right")
                            if pos_right4:
                                if pos_right4['y'] != 7:
                                    print(f"probe: FELL THROUGH (26, 7)! Pos: {pos_right4}")
                                    return
                                else:
                                    print("probe: (26, 7) is walkable floor!")
                                    
                                    # Test UP into (26, 6) from (26, 7)
                                    print("Testing (26, 6) from (26, 7)...")
                                    pos_up4 = move_test("Up")
                                    if pos_up4:
                                        if pos_up4['y'] != 6:
                                            print(f"probe: FELL THROUGH (26, 6)! Pos: {pos_up4}")
                                            return
                                        else:
                                            print("probe: (26, 6) is walkable floor!")
                                            move_test("Down")
                                    move_test("Left")
                            move_test("Left")
                    move_test("Left")
            move_test("Left")
            
    print("probe: Finished Row 7 tests.")

if __name__ == "__main__":
    test_rubble_row_7()
