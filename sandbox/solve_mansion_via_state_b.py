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

def solve_mansion():
    # 1. Walk from current (18, 7) on 2F in State A to the switch at (2, 12)
    print("Walking to northwest switch on 2F in State A...")
    path_to_switch = [
        # Walk Left on Row 7 to (11, 7)
        ("Left", 17, 7),
        ("Left", 16, 7),
        ("Left", 15, 7),
        ("Left", 14, 7),
        ("Left", 13, 7),
        ("Left", 12, 7),
        ("Left", 11, 7),
        # Walk Down on Column 11 to (11, 11)
        ("Down", 11, 8),
        ("Down", 11, 9),
        ("Down", 11, 10),
        ("Down", 11, 11),
        # Walk Left to (3, 11)
        ("Left", 10, 11),
        ("Left", 9, 11),
        ("Left", 8, 11),
        ("Left", 7, 11),
        ("Left", 6, 11),
        ("Left", 5, 11),
        ("Left", 4, 11),
        ("Left", 3, 11),
        # Walk to (2, 12) via Row 13
        ("Down", 3, 12),
        ("Down", 3, 13),
        ("Left", 2, 13),
        ("Left", 1, 13),
        ("Up", 1, 12),
        ("Up", 1, 11),
        ("Down", 1, 12),
        ("Right", 2, 12),
    ]
    for d, tx, ty in path_to_switch:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return
            
    # 2. Toggle switch to State B
    print("Toggling switch to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "A", "sleep 600", "A"])
    time.sleep(1.0)
    
    # 3. Walk from switch to (18, 8) stairs in State B
    print("Walking to stairs in State B...")
    path_to_stairs = [
        ("Right", 3, 12),
        ("Up", 3, 11),
        ("Right", 4, 11),
        ("Right", 5, 11),
        ("Right", 6, 11),
        ("Right", 7, 11),
        ("Right", 8, 11),
        ("Right", 9, 11),
        ("Right", 10, 11),
        ("Right", 11, 11),
        ("Down", 11, 12),
        ("Down", 11, 13),
        ("Right", 12, 13),
        ("Right", 13, 13),
        ("Right", 14, 13),
        ("Right", 15, 13),
        ("Right", 16, 13),
        ("Right", 17, 13),
        ("Right", 18, 13),
        ("Up", 18, 12),
        ("Up", 18, 11),
        ("Up", 18, 10),
        ("Up", 18, 9),
    ]
    for d, tx, ty in path_to_stairs:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return
            
    # 4. Step onto (18, 8) to warp to 3F in State B
    print("At (18, 9)! Stepping Up onto stairs warp...")
    mgba.press_buttons(["Up"])
    time.sleep(1.2)
    print("Warp complete! Position on 3F:", mgba.get_coordinates())
    mgba.take_screenshot()

solve_mansion()
