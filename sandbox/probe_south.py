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
            print("probe: BUMPED or battle starting. Waiting...")
            time.sleep(1.0)
            # We don't have battle check here, let's just retry
        mgba.press_buttons([step])
        time.sleep(0.4)
        pos_before = pos_after
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    return pos_after

def main():
    # Dismiss the "Got away safely!" screen first
    print("probe_south: Dismissing text box...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"probe_south starting from: {pos}")
    
    # 1. Walk Left to (19, 7)
    while pos['x'] > 19:
        pos = move_test("Left", pos['x'] - 1, pos['y'])
        
    # 2. Walk Down Column 19 to (19, 11)
    for y in range(8, 12):
        pos = move_test("Down", 19, y)
        
    # 3. Walk Right to Column 27 on Row 11
    for x in range(20, 28):
        pos = move_test("Right", x, 11)
        
    # 4. Walk Up Column 27 to Row 8
    for y in [10, 9, 8]:
        pos = move_test("Up", 27, y)
        
    print(f"probe_south: Finished. Final pos: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
