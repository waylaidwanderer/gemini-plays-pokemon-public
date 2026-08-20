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
    # Current: (14, 6) on 3F (State B)
    # 1. Walk back to 3F switch at (11, 11)
    print("Step 1: Walking back to 3F switch from (14, 6)...")
    back_to_switch = [
        ("Up", 14, 5),
        ("Left", 13, 5),
        ("Left", 12, 5),
        ("Left", 11, 5),
        ("Down", 11, 6),
        ("Down", 11, 7),
        ("Down", 11, 8),
        ("Down", 11, 9),
        ("Down", 11, 10),
        ("Down", 11, 11),
    ]
    for d, tx, ty in back_to_switch:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False
            
    # 2. Toggle 3F switch to State A
    print("Step 2: Toggling 3F switch to State A...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 800", "A", "sleep 800", "A", "sleep 800", "A", "sleep 800", "B", "sleep 500"])
    time.sleep(1.0)
    
    # 3. Walk to balcony drop on 3F (State A)
    print("Step 3: Walking to balcony drop in State A...")
    path_to_drop = [
        ("Up", 11, 10),
        ("Up", 11, 9),
        ("Up", 11, 8),
        ("Up", 11, 7),
        ("Up", 11, 6),
        ("Up", 11, 5),
        ("Right", 12, 5),
        ("Right", 13, 5),
        ("Right", 14, 5),
        ("Right", 15, 5), # OPEN in State A!
        ("Right", 16, 5),
        ("Right", 17, 5),
        ("Right", 18, 5),
        ("Down", 18, 6),
        ("Right", 19, 6),
        ("Right", 20, 6),
        ("Right", 21, 6),
        ("Right", 22, 6),
        ("Down", 22, 7),
        ("Down", 22, 8), # OPEN in State A!
        ("Down", 22, 9),
        ("Down", 22, 10),
        ("Down", 22, 11),
        ("Down", 22, 12),
        ("Down", 22, 13),
        ("Down", 22, 14),
        ("Right", 23, 14),
        ("Right", 24, 14),
    ]
    for d, tx, ty in path_to_drop:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False
            
    # Drop to 1F!
    print("Step 4: Dropping to 1F...")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    print("Landed on 1F! Position:", mgba.get_coordinates())
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    solve_all()
