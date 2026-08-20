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

def run_test():
    # 1. We are at (7, 10) on 3F. Step Down to warp to 2F!
    print("Stepping Down to warp to 2F...")
    mgba.press_buttons(["Down"])
    time.sleep(1.2)
    pos = mgba.get_coordinates()
    print("Now on floor. Position:", pos)
    
    # 2. Walk to northwest switch on 2F (starts at (7, 11))
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
            
    # 3. Toggle switch to State B
    print("Toggling switch to State B...")
    # First turn Up to face (2, 11)
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    # A, A, A, A to toggle switch
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "A", "sleep 600", "A"])
    time.sleep(1.0)
    
    # 4. Walk back to 2F stairs
    print("Walking back to 2F stairs...")
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
            
    # 5. Ascend to 3F
    print("At (7, 11) on 2F! Stepping Up to stairs warp...")
    mgba.press_buttons(["Up"])
    time.sleep(1.2)
    pos_3f = mgba.get_coordinates()
    print("Now at position on 3F:", pos_3f)
    
    # 6. Test walking East on 3F in State B
    print("Testing walk East on 3F in State B...")
    path_east_3f = [
        ("Right", 8, 11),
        ("Right", 9, 11),
        ("Right", 10, 11),
        ("Right", 11, 11),
        ("Right", 12, 11),
    ]
    for d, tx, ty in path_east_3f:
        if not walk_step(d, tx, ty):
            break
            
    mgba.take_screenshot()

run_test()
