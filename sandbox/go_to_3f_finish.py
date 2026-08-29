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
            # Simple battle run select if in battle
            mgba.press_buttons(["Down", "Right", "A"])
            time.sleep(1.0)
            mgba.press_buttons(["B"])
            time.sleep(0.5)
        mgba.press_buttons([step])
        time.sleep(0.4)
        pos_before = pos_after
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    return pos_after

def main():
    # We are at (7, 10) on 3F West
    print("go_to_3f_finish: Starting...")
    
    pos = mgba.get_coordinates()
    if pos['x'] == 7 and pos['y'] == 10:
        # 1. Walk down to (7, 11)
        pos = move_test("Down", 7, 11)
        
    # 2. Walk right to Column 10
    # From (7, 11) to (10, 11)
    while pos['x'] < 10:
        pos = move_test("Right", pos['x'] + 1, 11)
        
    # 3. Walk UP Column 10 to Row 6
    while pos['y'] > 6:
        pos = move_test("Up", 10, pos['y'] - 1)
        
    # 4. Walk right to (19, 6)
    while pos['x'] < 19:
        pos = move_test("Right", pos['x'] + 1, 6)
        
    # 5. Walk UP Column 19 to Row 4
    while pos['y'] > 4:
        pos = move_test("Up", 19, pos['y'] - 1)
        
    # 6. Walk to (20, 4) then UP to (20, 3)
    pos = move_test("Right", 20, 4)
    pos = move_test("Up", 20, 3)
    
    # 7. Walk RIGHT to (25, 3)
    while pos['x'] < 25:
        pos = move_test("Right", pos['x'] + 1, 3)
        
    print(f"go_to_3f_finish: Finished. Current position on 3F East: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
