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

def solve_all():
    # Current: (13, 12) on 2F in State B
    # 1. Walk to northwest switch at (2, 12) on 2F
    print("Step 1: Walking to northwest switch on 2F...")
    path_to_nw_switch = [
        ("Left", 12, 12),
        ("Left", 11, 12),
        ("Left", 10, 12),
        ("Left", 9, 12),
        ("Left", 8, 12),
        ("Left", 7, 12),
        ("Left", 6, 12),
        ("Left", 5, 12),
        ("Left", 4, 12),
        ("Left", 3, 12),
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
    
    # 3. Walk to 2F stairs at (7, 10) in State A
    print("Step 3: Walking to 2F stairs...")
    path_to_stairs = [
        ("Right", 3, 12),
        ("Up", 3, 11),
        ("Right", 4, 11),
        ("Right", 5, 11),
        ("Right", 6, 11),
        ("Right", 7, 11),
    ]
    for d, tx, ty in path_to_stairs:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return
            
    # Step UP to stairs warp to go to 3F in State A
    print("Step 4: Ascending to 3F in State A...")
    mgba.press_buttons(["Up"])
    time.sleep(1.2)
    print("Warp complete! Position on 3F:", mgba.get_coordinates())
    
    # 4. Walk to (11, 11) on 3F in State A
    print("Step 5: Walking to 3F switch...")
    path_to_3f_switch = [
        ("Right", 8, 11),
        ("Right", 9, 11),
        ("Down", 9, 12),
        ("Right", 10, 12),
        ("Right", 11, 12),
        ("Up", 11, 11),
    ]
    for d, tx, ty in path_to_3f_switch:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return
            
    # 5. Toggle 3F switch to State B
    print("Step 6: Toggling 3F switch to State B...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "A", "sleep 600", "A"])
    time.sleep(1.0)
    
    # 6. Walk to balcony drop on 3F (State B)
    print("Step 7: Walking to balcony drop on 3F...")
    path_to_balcony = [
        ("Down", 11, 12),
        ("Right", 12, 12),
        ("Right", 13, 12),
        ("Right", 14, 12),
        ("Right", 15, 12),
        ("Right", 16, 12),
        ("Right", 17, 12),
        ("Right", 18, 12),
        ("Up", 18, 11),
        ("Up", 18, 10),
        ("Up", 18, 9),
        ("Up", 18, 8),
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

solve_all()
