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
        mgba.press_buttons([step])
        time.sleep(0.4)
        pos_before = pos_after
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    return pos_after

def main():
    # We are at (5, 16) on 2F West
    print("go_to_3f: Starting at", mgba.get_coordinates())
    
    # 1. Walk UP Column 5 to Row 11
    for y in range(15, 10, -1):
        move_test("Up", 5, y)
        
    # 2. Walk RIGHT to (7, 11)
    move_test("Right", 6, 11)
    move_test("Right", 7, 11)
    
    # 3. Walk UP onto the stairs at (7, 10) to warp UP to 3F West!
    print("go_to_3f: Stepping onto stairs to warp UP...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"go_to_3f: Arrived on 3F! Position: {pos}")

if __name__ == "__main__":
    main()
