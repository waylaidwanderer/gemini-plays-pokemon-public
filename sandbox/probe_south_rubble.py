import mgba
import time

def move_test(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"probe: Pressing '{step}' to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([step])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 3:
        if pos_before == pos_after:
            print("probe: BUMPED.")
            return None
        mgba.press_buttons([step])
        time.sleep(0.4)
        pos_before = pos_after
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    return pos_after

def main():
    # We are at (25, 3)
    pos = mgba.get_coordinates()
    print(f"probe_south_rubble starting from: {pos}")
    
    # 1. Walk Right to (28, 3) -- wait, (28, 3) is rubble, so walk to (28, 4)
    # (25, 3) -> (26, 3) -> (27, 3) -> (27, 4) -> (28, 4)
    pos = move_test("Right", 26, 3)
    pos = move_test("Right", 27, 3)
    pos = move_test("Down", 27, 4)
    pos = move_test("Right", 28, 4)
    
    if not pos:
        print("probe: Failed to reach (28, 4)")
        return
        
    # 2. Walk Down Column 28 to Row 9
    for y in [5, 6, 7, 8, 9]:
        pos = move_test("Down", 28, y)
        if not pos:
            print(f"probe: Stopped walking Down Column 28 at Row {y-1}")
            break
            
    # 3. Test Left into Column 27 from different rows on Column 28
    pos = mgba.get_coordinates()
    current_y = pos['y']
    print(f"probe: At {pos}. Testing Left on Row {current_y}...")
    
    # Test Left into (27, current_y)
    pos_left = move_test("Left", 27, current_y)
    if pos_left:
        if pos_left['y'] != current_y or pos_left['x'] != 27:
            print(f"probe: FELL THROUGH on Row {current_y}! Current: {pos_left}")
            return
        else:
            print(f"probe: Walked onto (27, {current_y})!")
            move_test("Right", 28, current_y)
            
    # Walk Up Column 28 and test Left at other rows
    for y in range(current_y - 1, 3, -1):
        pos = move_test("Up", 28, y)
        if not pos: break
        print(f"probe: Testing Left on Row {y}...")
        pos_left = move_test("Left", 27, y)
        if pos_left:
            if pos_left['y'] != y or pos_left['x'] != 27:
                print(f"probe: FELL THROUGH on Row {y}! Current: {pos_left}")
                return
            else:
                print(f"probe: Walked onto (27, {y})!")
                move_test("Right", 28, y)
                
    print("probe: Finished all right-side tests.")

if __name__ == "__main__":
    main()
