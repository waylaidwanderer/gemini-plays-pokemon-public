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
    # Starting from (19, 4) on 3F
    # Walk to the pit via Row 3 and Column 25 (bypassing row 3 column 19 railing)
    print("Step 1: Walking to the pit via Row 3 and Column 25...")
    path_to_pit = [
        ("Right", 20, 4),
        ("Up", 20, 3),
        ("Right", 21, 3),
        ("Right", 22, 3),
        ("Right", 23, 3),
        ("Right", 24, 3),
        ("Right", 25, 3),
        ("Down", 25, 4),
        ("Down", 25, 5),
    ]
    for d, tx, ty in path_to_pit:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False
            
    # Step Left onto (24, 5) pit to drop to 1F!
    print("Step 2: Stepping into the pit at (24, 5)...")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    print("Landed on 1F! Position:", mgba.get_coordinates())
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    solve_all()
