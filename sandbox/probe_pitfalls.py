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

def probe_up():
    # We are at (26, 5)
    print(f"probe starting at: {mgba.get_coordinates()}")
    
    # Walk Up to (26, 4)
    pos = move_test("Up")
    if not pos:
        return
        
    # Walk Up to (26, 3)
    pos = move_test("Up")
    if not pos:
        return
        
    # Try to step Up into (26, 2) (golden rubble on Row 2)
    pos_up = move_test("Up")
    if pos_up:
        print(f"probe: Column 26 Row 2 is WALKABLE to {pos_up}")
    else:
        print("probe: Column 26 Row 2 is BLOCKED/SOLID.")
        
    # If we are still on 3F at (26, 3), let's walk Right to (27, 3) and try Up into (27, 2)
    pos = mgba.get_coordinates()
    if pos['y'] == 3:
        move_test("Right")
        pos_up2 = move_test("Up")
        if pos_up2:
            print(f"probe: Column 27 Row 2 is WALKABLE to {pos_up2}")
        else:
            print("probe: Column 27 Row 2 is BLOCKED/SOLID.")

if __name__ == "__main__":
    probe_up()
