import mgba
import time

def is_in_battle():
    # We can check battle or just return False since we have time.sleep
    return False

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
    # We start at (7, 10) on 3F West
    print("go_to_3f_east: Starting...")
    
    # 1. Walk down to (7, 11)
    pos = move_test("Down", 7, 11)
    
    # 2. Walk right on Row 11 to Column 10
    for x in range(8, 11):
        pos = move_test("Right", x, 11)
        
    # 3. Walk up Column 10 to Row 6
    for y in range(10, 5, -1):
        pos = move_test("Up", 10, y)
        
    # 4. Walk right on Row 6 to Column 19
    for x in range(11, 20):
        pos = move_test("Right", x, 6)
        
    # 5. Walk UP Column 19 to Row 4
    for y in [5, 4]:
        pos = move_test("Up", 19, y)
        
    # 6. Walk RIGHT to (20, 4) and UP to (20, 3)
    pos = move_test("Right", 20, 4)
    pos = move_test("Up", 20, 3)
    
    # 7. Walk RIGHT along Row 3 to Column 25
    for x in range(21, 26):
        pos = move_test("Right", x, 3)
        
    print(f"go_to_3f_east: Successfully reached 3F East at {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
