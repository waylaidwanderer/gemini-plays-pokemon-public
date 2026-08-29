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

def probe_south():
    # We are at (22, 7)
    print(f"probe_south starting from: {mgba.get_coordinates()}")
    
    # 1. Walk Left to (19, 7)
    pos = move_test("Left", 21, 7)
    if not pos: return
    pos = move_test("Left", 20, 7)
    if not pos: return
    pos = move_test("Left", 19, 7)
    if not pos: return
    
    # 2. Walk Down Column 19 to (19, 11)
    for y in range(8, 12):
        pos = move_test("Down", 19, y)
        if not pos: return
        
    # 3. Walk Right to Column 27 on Row 11
    for x in range(20, 28):
        pos = move_test("Right", x, 11)
        if not pos: return
        
    # 4. Walk Up Column 27 to Row 8
    for y in [10, 9, 8]:
        pos = move_test("Up", 27, y)
        if not pos: return
        
    print(f"probe_south: Successfully reached (27, 8)! Current pos: {mgba.get_coordinates()}")

if __name__ == "__main__":
    probe_south()
