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
    # 1. We are currently at (25, 3) on 1F in State B.
    # Walk to the 1F/2F stairs at (22, 2) and go up to 2F.
    print("Step 1: Walking to 2F stairs on 1F...")
    path_to_stairs_1f = [
        ("Up", 25, 2),
        ("Left", 24, 2),
        ("Left", 23, 2),
    ]
    for d, tx, ty in path_to_stairs_1f:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False
            
    # Step Left onto (22, 2) stairs to warp to 2F
    print("Step 2: Stepping onto stairs to warp to 2F...")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    print("Warp complete! Position on 2F:", mgba.get_coordinates())
    
    # 2. On 2F (State B), walk to the (18, 8) stairs and go to 3F
    print("Step 3: Walking to 3F stairs on 2F...")
    # Land at (22, 2) on 2F
    path_to_stairs_2f = [
        ("Left", 21, 2),
        ("Left", 20, 2),
        ("Left", 19, 2),
        ("Left", 18, 2),
        ("Down", 18, 3),
        ("Down", 18, 4),
        ("Down", 18, 5),
        ("Down", 18, 6),
        ("Down", 18, 7),
    ]
    for d, tx, ty in path_to_stairs_2f:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False
            
    # Step Down onto (18, 8) stairs to warp to 3F
    print("Step 4: Stepping onto stairs to warp to 3F...")
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    print("Warp complete! Position on 3F:", mgba.get_coordinates())
    
    # 3. On 3F (State B), walk along row 3 and column 25 to balcony drop
    print("Step 5: Walking to balcony drop on 3F (State B)...")
    # Land at (18, 8) on 3F
    path_to_drop_3f = [
        ("Up", 18, 7),
        ("Up", 18, 6),
        ("Up", 18, 5),
        ("Up", 18, 4),
        ("Up", 18, 3),
        ("Right", 19, 3),
        ("Right", 20, 3),
        ("Right", 21, 3),
        ("Right", 22, 3),
        ("Right", 23, 3),
        ("Right", 24, 3),
        ("Right", 25, 3),
        ("Down", 25, 4),
        ("Down", 25, 5),
        ("Down", 25, 6), # OPEN in State B! (Gate on column 25 row 8 is OPEN!)
        ("Down", 25, 7),
        ("Down", 25, 8),
        ("Down", 25, 9),
        ("Down", 25, 10),
        ("Down", 25, 11),
        ("Down", 25, 12),
        ("Down", 25, 13),
        ("Down", 25, 14),
        ("Left", 24, 14),
    ]
    for d, tx, ty in path_to_drop_3f:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False
            
    # Drop to 1F B1F stairs!
    print("Step 6: Dropping to 1F B1F stairs...")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    print("Landed on 1F! Position:", mgba.get_coordinates())
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    solve_all()
