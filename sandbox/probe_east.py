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
            # Select RUN if in battle (let's do simple run select)
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
    # We are at (10, 4) in the battle-end overworld screen
    print("probe_east: Starting at", mgba.get_coordinates())
    
    # Dismiss "Got away safely!"
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print("probe_east: Post-dismiss position:", pos)
    
    # Walk RIGHT Row 4 to Column 19
    for x in range(11, 20):
        pos = move_test("Right", x, 4)
        if not pos:
            print(f"probe_east: Blocked at Column {x} Row 4.")
            return
            
    # Walk right to (20, 4) then up to (20, 3)
    pos = move_test("Right", 20, 4)
    if not pos: return
    pos = move_test("Up", 20, 3)
    if not pos: return
    
    # Walk RIGHT to (25, 3)
    for x in range(21, 26):
        pos = move_test("Right", x, 3)
        if not pos: return
        
    print(f"probe_east: Successfully reached 3F East at {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
