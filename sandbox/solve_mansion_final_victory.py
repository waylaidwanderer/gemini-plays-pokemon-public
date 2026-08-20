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
    # Starting from (22, 7) on 3F (State A)
    # Walk to balcony drop via Column 19 and Row 14 (completely unblocked bypass!)
    print("Step 1: Walking to balcony drop via Column 19 and Row 14...")
    path_to_drop = [
        ("Left", 21, 7),
        ("Left", 20, 7),
        ("Left", 19, 7),
        ("Down", 19, 8),
        ("Down", 19, 9),
        ("Down", 19, 10),
        ("Down", 19, 11),
        ("Down", 19, 12),
        ("Down", 19, 13),
        ("Down", 19, 14),
        ("Right", 20, 14),
        ("Right", 21, 14),
        ("Right", 22, 14),
        ("Right", 23, 14),
        ("Right", 24, 14),
    ]
    for d, tx, ty in path_to_drop:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False
            
    # Drop to 1F!
    print("Step 2: Dropping to 1F...")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    print("Landed on 1F! Position:", mgba.get_coordinates())
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    solve_all()
