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
    # Current: (19, 12) on 3F (State A)
    # 1. Walk back to 3F switch at (11, 11) via Row 6 horizontal corridor
    print("Step 1: Walking back to 3F switch...")
    back_to_switch = [
        ("Up", 19, 11),
        ("Up", 19, 10),
        ("Up", 19, 9),
        ("Up", 19, 8),
        ("Up", 19, 7),
        ("Up", 19, 6),
        ("Left", 18, 6),
        ("Left", 17, 6),
        ("Left", 16, 6),
        ("Left", 15, 6),
        ("Left", 14, 6),
        ("Left", 13, 6),
        ("Left", 12, 6),
        ("Left", 11, 6),
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
            
    # 2. Toggle 3F switch to State B
    print("Step 2: Toggling 3F switch to State B...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 800", "A", "sleep 800", "A", "sleep 800", "A", "sleep 800", "B", "sleep 500"])
    time.sleep(1.0)
    
    # 3. Walk to the pit at (24, 5) on 3F (State B)
    print("Step 3: Walking to pit at (24, 5)...")
    path_to_pit = [
        ("Up", 11, 10),
        ("Up", 11, 9),
        ("Up", 11, 8),
        ("Up", 11, 7),
        ("Up", 11, 6),
        ("Right", 12, 6),
        ("Right", 13, 6),
        ("Right", 14, 6),
        ("Right", 15, 6),
        ("Right", 16, 6),
        ("Right", 17, 6),
        ("Right", 18, 6),
        ("Up", 18, 5),
        ("Right", 19, 5),
        ("Right", 20, 5),
        ("Right", 21, 5), # Gate (21, 5) is OPEN in State B!
        ("Right", 22, 5),
        ("Right", 23, 5),
    ]
    for d, tx, ty in path_to_pit:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False
            
    # Step onto (24, 5) pit to drop to 1F!
    print("Step 4: Stepping into the pit...")
    mgba.press_buttons(["Right"])
    time.sleep(1.5)
    print("Landed on 1F! Position:", mgba.get_coordinates())
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    solve_all()
