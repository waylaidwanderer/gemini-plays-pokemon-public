import mgba
import time

def walk_step(direction, target_x, target_y):
    pos = mgba.get_coordinates()
    print(f"Standing at {pos}. Pressing {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    print(f"Now at {new_pos}. Target was ({target_x}, {target_y})")
    if new_pos['x'] == target_x and new_pos['y'] == target_y:
        return True
    else:
        print("Failed to reach target! Could be a battle or obstacle.")
        return False

def go_to_switch():
    path = [
        # 1. Walk Left to (11, 5)
        ("Left", 13, 5),
        ("Left", 12, 5),
        ("Left", 11, 5),
        # 2. Walk Down to (11, 11)
        ("Down", 11, 6),
        ("Down", 11, 7),
        ("Down", 11, 8),
        ("Down", 11, 9),
        ("Down", 11, 10),
        ("Down", 11, 11),
        # 3. Walk Left to (3, 11)
        ("Left", 10, 11),
        ("Left", 9, 11),
        ("Left", 8, 11),
        ("Left", 7, 11),
        ("Left", 6, 11),
        ("Left", 5, 11),
        ("Left", 4, 11),
        ("Left", 3, 11),
        # 4. Walk Down to (3, 13)
        ("Down", 3, 12),
        ("Down", 3, 13),
        # 5. Walk Left to (1, 13)
        ("Left", 2, 13),
        ("Left", 1, 13),
        # 6. Walk Up to (1, 11)
        ("Up", 1, 12),
        ("Up", 1, 11),
    ]
    
    success = True
    for direction, tx, ty in path:
        if not walk_step(direction, tx, ty):
            success = False
            break
            
    if success:
        # Stand at (1, 11) face Right and press A
        print("At (1, 11)! Facing Right...")
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        print("Pressing A to toggle switch...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
    mgba.take_screenshot()

go_to_switch()
