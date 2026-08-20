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
    # Current: (21, 6) on 3F (State B)
    # Walk to the pit at (24, 5) via Row 6 bypass
    print("Step 1: Walking to the pit at (24, 5)...")
    path_to_pit = [
        ("Right", 22, 6),
        ("Up", 22, 5),
        ("Right", 23, 5),
    ]
    for d, tx, ty in path_to_pit:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False
            
    # Step Right onto (24, 5) pit to drop to 1F!
    print("Step 2: Stepping into the pit...")
    mgba.press_buttons(["Right"])
    time.sleep(1.5)
    print("Landed on 1F! Position:", mgba.get_coordinates())
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    solve_all()
