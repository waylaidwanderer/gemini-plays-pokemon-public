import mgba
import time

# 1. Dismiss "Got away safely!"
print("Dismissing text box...")
mgba.press_buttons(["A"])
time.sleep(1.0) # Wait for overworld to load

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
    # Current: (5, 11) on 2F in State B
    # 1. Walk to northwest switch at (2, 12) on 2F
    print("Step 1: Walking to northwest switch on 2F...")
    path_to_nw_switch = [
        ("Left", 4, 11),
        ("Left", 3, 11),
        ("Down", 3, 12),
        ("Down", 3, 13),
        ("Left", 2, 13),
        ("Left", 1, 13),
        ("Up", 1, 12),
        ("Up", 1, 11),
        ("Down", 1, 12),
        ("Right", 2, 12),
    ]
    for d, tx, ty in path_to_nw_switch:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return
            
    # 2. Toggle switch to State A
    print("Step 2: Toggling switch to State A...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "A", "sleep 600", "A"])
    time.sleep(1.0)
    
    # 3. Walk to east side of column 15 on 2F in State A
    print("Step 3: Walking to east side of column 15 in State A...")
    path_to_east_side = [
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
        ("Right", 12, 11),
        ("Right", 13, 11),
        ("Right", 14, 11),
        ("Up", 14, 10),
        ("Up", 14, 9),
        ("Up", 14, 8),
        ("Up", 14, 7),
        ("Up", 14, 6),
        ("Right", 15, 6), # Gate (15, 6) is OPEN in State A!
        ("Right", 16, 6),
        ("Right", 17, 6),
        ("Right", 18, 6),
    ]
    for d, tx, ty in path_to_east_side:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return
            
    # 4. Walk to central Mewtwo switch at (12, 9) and toggle to State B
    print("Step 4: Walking to central Mewtwo switch and toggling to State B...")
    path_to_central_switch = [
        ("Left", 17, 6),
        ("Left", 16, 6),
        ("Left", 15, 6),
        ("Left", 14, 6),
        ("Left", 13, 6),
        ("Down", 13, 7),
        ("Down", 13, 8),
        ("Down", 13, 9),
    ]
    for d, tx, ty in path_to_central_switch:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return
            
    # Stand at (13, 9) face Left and press A
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "A", "sleep 600", "A"])
    time.sleep(1.0)
    
    # 5. Walk to (18, 8) stairs in State B
    print("Step 5: Walking to (18, 8) stairs in State B...")
    path_to_stairs = [
        ("Up", 13, 8),
        ("Up", 13, 7),
        ("Up", 13, 6),
        ("Right", 14, 6),
        ("Right", 15, 6),
        ("Right", 16, 6),
        ("Right", 17, 6),
        ("Right", 18, 6),
        ("Down", 18, 7),
    ]
    for d, tx, ty in path_to_stairs:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return
            
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
            return
            
    # Drop to 1F!
    print("Step 8: Dropping to 1F...")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    print("Landed on 1F! Position:", mgba.get_coordinates())
    mgba.take_screenshot()

solve_mansion()
