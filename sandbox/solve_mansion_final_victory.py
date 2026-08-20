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
    # Current: (1, 11) on 2F (State B, facing Up/Right?)
    # 1. Turn Right and toggle the switch to State A
    print("Step 1: Turning Right to face the switch...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    
    print("Step 2: Toggling switch to State A...")
    # Multi-page switch dialogue
    mgba.press_buttons(["A", "sleep 800", "A", "sleep 800", "A", "sleep 800", "A", "sleep 800", "B", "sleep 500"])
    time.sleep(1.0)
    
    # 2. Walk to the east side of column 14 in State A (via row 11)
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
            
    # 3. Walk to central Mewtwo switch at (12, 9) and toggle to State B
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
            
    # Stand at (13, 9) face Left and press A to toggle switch
    print("Step 5: Toggling central switch to State B...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 800", "A", "sleep 800", "A", "sleep 800", "A", "sleep 800", "B", "sleep 500"])
    time.sleep(1.0)
    
    # 4. Walk to (18, 8) stairs in State B
    print("Step 6: Walking to (18, 8) stairs in State B...")
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
    print("Step 7: Ascending to 3F in State B...")
    mgba.press_buttons(["Down"])
    time.sleep(1.2)
    print("Warp complete! Position on 3F:", mgba.get_coordinates())
    
    # 5. Walk to balcony drop on 3F (State B)
    print("Step 8: Walking to balcony drop on 3F...")
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
    print("Step 9: Dropping to 1F...")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    print("Landed on 1F! Position:", mgba.get_coordinates())
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    solve_all()
