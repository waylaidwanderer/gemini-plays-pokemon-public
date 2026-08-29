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
            # Run from battle if active
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
    # We are at (28, 4) with "Got away safely!" active
    print("go_to_switch_state_a: Dismissing text box...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print("go_to_switch_state_a: Current position:", pos)
    
    # 1. Walk back to Column 20 Row 3
    # (28, 4) -> (27, 4) -> (27, 3) -> (20, 3)
    pos = move_test("Left", 27, 4)
    pos = move_test("Up", 27, 3)
    for x in range(26, 19, -1):
        pos = move_test("Left", x, 3)
        
    # 2. Walk to Row 6 Column 19
    # (20, 3) -> (20, 4) -> (19, 4) -> (19, 5) -> (19, 6)
    pos = move_test("Down", 20, 4)
    pos = move_test("Left", 19, 4)
    pos = move_test("Down", 19, 5)
    pos = move_test("Down", 19, 6)
    
    # 3. Walk LEFT on Row 6 to Column 10
    for x in range(18, 9, -1):
        pos = move_test("Left", x, 6)
        
    # 4. Walk DOWN Column 10 to Row 11
    for y in [7, 8, 9, 10, 11]:
        pos = move_test("Down", 10, y)
        
    # 5. Walk LEFT on Row 11 to Column 1 (bypassing warp at (7, 10))
    for x in range(9, 0, -1):
        pos = move_test("Left", x, 11)
        
    # 6. Walk to switch at (2, 12)
    pos = move_test("Down", 1, 12)
    pos = move_test("Right", 2, 12)
    
    # 7. Toggle switch to State A
    print("At switch. Toggling to State A...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    print(f"Finished toggle_to_state_a. Current pos: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
