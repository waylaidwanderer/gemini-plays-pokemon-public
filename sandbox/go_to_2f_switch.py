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
        print("Failed to reach target! Could be a battle or wall.")
        return False

def go_to_switch():
    path = [
        # Left 4 to (3, 11)
        ("Left", 6, 11),
        ("Left", 5, 11),
        ("Left", 4, 11),
        ("Left", 3, 11),
        # Down 2 to (3, 13)
        ("Down", 3, 12),
        ("Down", 3, 13),
        # Left 2 to (1, 13)
        ("Left", 2, 13),
        ("Left", 1, 13),
        # Up 2 to (1, 11)
        ("Up", 1, 12),
        ("Up", 1, 11),
    ]
    
    for direction, tx, ty in path:
        if not walk_step(direction, tx, ty):
            mgba.take_screenshot()
            return
            
    # Face Right
    print("At (1, 11)! Facing Right...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    
    # Press A to toggle switch
    print("Pressing A to toggle switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.take_screenshot()

go_to_switch()
