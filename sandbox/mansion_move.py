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
    # Phase 1: Go down to 2F from current (9, 11) on 3F State B
    print("Phase 1: Going down to 2F...")
    path_to_stairs = [
        ("Left", 8, 11),
        ("Left", 7, 11),
    ]
    for d, tx, ty in path_to_stairs:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return
            
    print("At (7, 11) on 3F. Stepping Up onto stairs...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    print("Standing on stairs. Stepping Down to warp to 2F...")
    mgba.press_buttons(["Down"])
    time.sleep(1.2)
    print("Warp complete! Position:", mgba.get_coordinates())
    
    # Phase 2: Walk to northwest switch on 2F
    print("Phase 2: Walking to northwest switch on 2F...")
    path_to_switch = [
        ("Left", 6, 11),
        ("Left", 5, 11),
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
    for d, tx, ty in path_to_switch:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return
            
    # Phase 3: Toggle switch to State A
    print("Phase 3: Toggling switch to State A...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "A", "sleep 600", "A"])
    time.sleep(1.0)
    
    # Phase 4: Walk back to 2F stairs
    print("Phase 4: Walking back to 2F stairs...")
    path_back_to_stairs = [
        ("Right", 3, 12),
        ("Up", 3, 11),
        ("Right", 4, 11),
        ("Right", 5, 11),
        ("Right", 6, 11),
        ("Right", 7, 11),
    ]
    for d, tx, ty in path_back_to_stairs:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return
            
    # Phase 5: Ascend to 3F in State A
    print("Phase 5: Ascending to 3F in State A...")
    mgba.press_buttons(["Up"])
    time.sleep(1.2)
    print("Warp complete! Position on 3F:", mgba.get_coordinates())
    
    # Phase 6: Walk to 3F switch at (11, 11) in State A
    print("Phase 6: Walking to 3F switch...")
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
            
    # Phase 7: Toggle 3F switch to State B
    print("Phase 7: Toggling 3F switch to State B...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "A", "sleep 600", "A"])
    time.sleep(1.0)
    
    # Phase 8: Walk to balcony drop on 3F in State B
    print("Phase 8: Walking to balcony drop...")
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
        ("Right", 21, 5),
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
            
    # Phase 9: Drop to 1F!
    print("Phase 9: Dropping to 1F...")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    print("Landed on 1F! Position:", mgba.get_coordinates())
    mgba.take_screenshot()

solve_mansion()
