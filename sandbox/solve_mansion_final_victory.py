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
    # Current: (19, 5) on 3F (State A)
    # Walk to balcony drop via Row 6 horizontal bypass corridor to Col 22, then Down to Row 14, then Right to Drop
    print("Step 1: Walking to balcony drop from (19, 5) in State A...")
    path_to_drop = [
        ("Down", 19, 6),
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
    print("Step 2: Dropping to 1F...")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    print("Landed on 1F! Position:", mgba.get_coordinates())
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    solve_all()
