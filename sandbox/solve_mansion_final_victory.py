import mgba
import time

def walk_step(direction, target_x, target_y):
    pos = mgba.get_coordinates()
    print(f"Standing at {pos}. Pressing {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    new_pos = mgba.get_coordinates()
    print(f"Now at {new_pos}. Target was ({target_x}, {target_y})")
    if new_pos['x'] == target_x and new_pos['y'] == target_y:
        return True
    else:
        print("Failed to reach target! Could be a battle or obstacle.")
        return False

def solve_all():
    # 1. Walk from (9, 9) back to northwest switch at (1, 11) on 2F (State B)
    print("Step 1: Walking back to northwest switch at (1, 11)...")
    path_to_nw_switch = [
        ("Left", 8, 9),
        ("Left", 7, 9),
        ("Left", 6, 9),
        ("Left", 5, 9),
        ("Down", 5, 10),
        ("Down", 5, 11),
        ("Down", 5, 12),
        ("Down", 5, 13),
        ("Left", 4, 13),
        ("Left", 3, 13),
        ("Left", 2, 13),
        ("Left", 1, 13),
        ("Up", 1, 12),
        ("Up", 1, 11),
    ]
    for d, tx, ty in path_to_nw_switch:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False
            
    # 2. Toggle switch to State A (from (1, 11) facing Right)
    print("Step 2: Toggling switch to State A...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "A", "sleep 600", "A"])
    time.sleep(1.0)
    
    # 3. Walk to east side of column 14 on 2F in State A (row 11 gate is open!)
    print("Step 3: Walking to east side in State A...")
    path_to_east_side = [
        ("Down", 1, 12),
        ("Down", 1, 13),
        ("Right", 2, 13),
        ("Right", 3, 13),
        ("Right", 4, 13),
        ("Right", 5, 13),
        ("Up", 5, 12),
        ("Up", 5, 11),
        ("Right", 6, 11),
        ("Right", 7, 11),
        ("Right", 8, 11),
        ("Right", 9, 11),
        ("Right", 10, 11),
        ("Right", 11, 11), # Gate on Column 11 is OPEN in State A!
        ("Right", 12, 11),
        ("Right", 13, 11),
        ("Right", 14, 11),
    ]
    for d, tx, ty in path_to_east_side:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False
            
    # 4. Walk to central Mewtwo switch at (12, 9) and toggle to State B
    print("Step 4: Walking to central Mewtwo switch and toggling to State B...")
    path_to_central_switch = [
        ("Up", 14, 10),
        ("Up", 14, 9),
        ("Left", 13, 9),
    ]
    for d, tx, ty in path_to_central_switch:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False
            
    # Stand at (13, 9) face Left and press A
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "A", "sleep 600", "A"])
    time.sleep(1.0)
    
    # 5. Walk to (18, 8) stairs in State B (since we are on the east side!)
    print("Step 5: Walking to (18, 8) stairs in State B...")
    path_to_stairs = [
        ("Right", 14, 9),
        ("Up", 14, 8),
        ("Up", 14, 7),
        ("Up", 14, 6),
        ("Right", 15, 6), # Gate (15, 6) is OPEN in State B!
        ("Right", 16, 6),
        ("Right", 17, 6),
        ("Right", 18, 6),
        ("Down", 18, 7),
    ]
    for d, tx, ty in path_to_stairs:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False
            
    # Step onto (18, 8) stairs to warp to 3F in State B
    print("Step 6: Ascending to 3F in State B...")
    mgba.press_buttons(["Down"])
    time.sleep(1.2)
    print("Warp complete! Position on 3F:", mgba.get_coordinates())
    
    # 6. Walk to balcony drop on 3F (State B)
    print("Step 7: Walking to balcony drop on 3F...")
    path_to_balcony = [
        ("Up", 18, 7),
        ("Up", 18, 6),
        ("Up", 18, 5),
        ("Right", 19, 5),
        ("Right", 20, 5),
        ("Right", 21, 5), # Gate (21, 5) is OPEN in State B!
        ("Right", 22, 5),
        ("Right", 23, 5),
        ("Right", 24, 5),
        ("Down", 24, 6),
        ("Down", 24, 7),
        ("Down", 24, 8),
        ("Down", 24, 9),
        ("Down", 24, 10),
        ("Down", 24, 11),
        ("Down", 24, 12),
        ("Down", 24, 13),
        ("Down", 24, 14),
    ]
    for d, tx, ty in path_to_balcony:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False
            
    # Drop to 1F!
    print("Step 8: Dropping to 1F...")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    print("Landed on 1F! Position:", mgba.get_coordinates())
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    solve_all()
