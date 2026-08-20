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
    # Starting from (19, 6) on 3F (State B)
    print("Step 1: Walking from (19, 6) to balcony drop...")
    path_to_drop = [
        ("Right", 20, 6),
        ("Right", 21, 6),
        ("Right", 22, 6),
        ("Down", 22, 7),
        ("Down", 22, 8),
        ("Down", 22, 9),
        ("Down", 22, 10),
        ("Down", 22, 11),
        ("Down", 22, 12),
        ("Down", 22, 13),
        ("Down", 24, 14), # Wait! Can we walk directly from (22, 13) to (24, 14) using walk_step? No, we should walk to (22, 14) first!
    ]
    # Let's write the complete coordinate-by-coordinate path
    path_to_drop = [
        ("Right", 20, 6),
        ("Right", 21, 6),
        ("Right", 22, 6),
        ("Down", 22, 7),
        ("Down", 22, 8),
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
    print("Step 2: Dropping to 1F...")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    print("Landed on 1F! Position:", mgba.get_coordinates())
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    solve_all()
