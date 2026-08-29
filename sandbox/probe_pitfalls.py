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

def probe():
    # We are at (26, 5)
    print(f"probe starting at: {mgba.get_coordinates()}")
    
    # Let's test Column 25 Row 6:
    # Walk Left to (25, 5)
    pos = move_test("Left")
    if pos:
        # Try to step Down into (25, 6)
        pos_down = move_test("Down")
        if pos_down:
            print(f"probe: Column 25 Row 6 is WALKABLE to {pos_down}")
            # step back up
            move_test("Up")
        else:
            print("probe: Column 25 Row 6 is BLOCKED/SOLID.")
        # Walk back to (26, 5)
        move_test("Right")
        
    # Let's test Column 27 Row 6:
    # Walk Right to (27, 5)
    pos = move_test("Right")
    if pos:
        # Try to step Down into (27, 6)
        pos_down = move_test("Down")
        if pos_down:
            print(f"probe: Column 27 Row 6 is WALKABLE to {pos_down}")
            # step back up
            move_test("Up")
        else:
            print("probe: Column 27 Row 6 is BLOCKED/SOLID.")
        # Walk back to (26, 5)
        move_test("Left")

    # Let's test Column 28 Row 6:
    # Walk Right 2 steps to (28, 5)
    pos = move_test("Right")
    if pos:
        pos2 = move_test("Right")
        if pos2:
            # Try to step Down into (28, 6)
            pos_down = move_test("Down")
            if pos_down:
                print(f"probe: Column 28 Row 6 is WALKABLE to {pos_down}")
                # Try to step Down into (28, 7)
                pos_down2 = move_test("Down")
                if pos_down2:
                    print(f"probe: Column 28 Row 7 is WALKABLE to {pos_down2}")
                    # step back up
                    move_test("Up")
                else:
                    print("probe: Column 28 Row 7 is BLOCKED/SOLID.")
                # step back up
                move_test("Up")
            else:
                print("probe: Column 28 Row 6 is BLOCKED/SOLID.")
            # Walk back to (26, 5)
            move_test("Left")
        move_test("Left")

if __name__ == "__main__":
    probe()
