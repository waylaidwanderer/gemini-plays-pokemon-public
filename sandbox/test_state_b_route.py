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
    # Current: (9, 11) on 3F in State A
    # 1. Walk to stairs at (7, 10) and go down to 2F
    print("Going down to 2F...")
    path_to_stairs = [
        ("Left", 8, 11),
        ("Left", 7, 11),
    ]
    for d, tx, ty in path_to_stairs:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return
            
    print("At (7, 11)! Stepping Up to stairs warp...")
    mgba.press_buttons(["Up"])
    time.sleep(1.2)
    print("Now at position:", mgba.get_coordinates())
    
    # Now we should be at (7, 11) on 2F
    pos = mgba.get_coordinates()
    if pos['y'] == 11:
        # We are on 2F! Walk to the northwest switch
        print("Walking to northwest switch on 2F...")
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
                
        # Toggle switch to State B
        print("Toggling switch to State B...")
        mgba.press_buttons(["Up", "sleep 400", "A", "sleep 1000", "A", "sleep 1000", "A", "sleep 1000", "A"])
        time.sleep(1.0)
        
        # Walk back to stairs at (7, 10) on 2F
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
                
        # Ascend to 3F
        print("At (7, 11) on 2F! Stepping Up to stairs warp...")
        mgba.press_buttons(["Up"])
        time.sleep(1.2)
        print("Now at position on 3F:", mgba.get_coordinates())
        
        # Now we are on 3F at (7, 11) in State B!
        # Let's test walking Right
        print("Testing walk East on 3F in State B...")
        for i in range(5):
            pos = mgba.get_coordinates()
            mgba.press_buttons(["Right"])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            print(f"Step Right {i+1}: {pos} -> {new_pos}")
            if new_pos == pos:
                print("Blocked in State B!")
                break
                
    mgba.take_screenshot()

run_test()
