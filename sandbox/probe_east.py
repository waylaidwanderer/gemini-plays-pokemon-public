import mgba
import time

def move_test(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"probe: Pressing '{step}' to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([step])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 4:
        if pos_before == pos_after:
            print("probe: BUMPED. Retrying...")
            # Dismiss potential battle screen
            mgba.press_buttons(["B"])
            time.sleep(0.5)
        mgba.press_buttons([step])
        time.sleep(0.4)
        pos_before = pos_after
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    return pos_after

def main():
    # We are at (14, 1) on 3F
    print("probe_east: Starting at", mgba.get_coordinates())
    
    # Let's test Column 15 on Rows 1 to 7
    # We are currently at Row 1.
    for y in range(1, 8):
        # 1. Walk vertically to Row y on Column 14
        pos = mgba.get_coordinates()
        while pos['y'] < y:
            pos = move_test("Down", 14, pos['y'] + 1)
            if not pos: return
        while pos['y'] > y:
            pos = move_test("Up", 14, pos['y'] - 1)
            if not pos: return
            
        # 2. Try to step RIGHT into Column 15 Row y
        print(f"probe_east: Testing Column 15 Row {y} (15, {y})...")
        pos_right = move_test("Right", 15, y)
        if pos_right:
            print(f"probe_east: Column 15 Row {y} is OPEN! Walked onto: {pos_right}")
            # Step back left to Column 14 Row y
            move_test("Left", 14, y)
        else:
            print(f"probe_east: Column 15 Row {y} is CLOSED.")

if __name__ == "__main__":
    main()
