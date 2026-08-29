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
    # We are at (1, 16) on 2F West
    print("go_to_3f_finish: Starting...")
    
    # 1. Walk Right along Row 16 to Column 5
    for x in range(2, 6):
        move_test("Right", x, 16)
        
    # 2. Walk UP Column 5 to Row 11
    for y in range(15, 10, -1):
        move_test("Up", 5, y)
        
    # 3. Walk RIGHT to (7, 11)
    move_test("Right", 6, 11)
    move_test("Right", 7, 11)
    
    # 4. Step UP onto stairs at (7, 10) to warp UP to 3F West!
    print("go_to_3f_finish: Stepping onto stairs at (7, 10)...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"go_to_3f_finish: Arrived on 3F! Position: {pos}")
    
    # 5. Walk right to Column 10
    # From (7, 11) to (10, 11)
    for x in range(8, 11):
        move_test("Right", x, 11)
        
    # 6. Walk UP Column 10 to Row 6
    for y in range(10, 5, -1):
        move_test("Up", 10, y)
        
    # 7. Walk right to (19, 6)
    for x in range(11, 20):
        move_test("Right", x, 6)
        
    # 8. Walk UP to (19, 4)
    move_test("Up", 19, 5)
    move_test("Up", 19, 4)
    
    # 9. Walk to (20, 4) then UP to (20, 3)
    move_test("Right", 20, 4)
    move_test("Up", 20, 3)
    
    # 10. Walk RIGHT to (25, 3)
    for x in range(21, 26):
        move_test("Right", x, 3)
        
    print(f"go_to_3f_finish: Finished. Current position on 3F East: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
