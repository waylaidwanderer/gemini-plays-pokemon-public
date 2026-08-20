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
    # Starting from (12, 12) on 3F (State B)
    print("Step 1: Walking to balcony drop from (12, 12) on 3F...")
    path_to_balcony = [
        ("Right", 13, 12),
        ("Right", 14, 12),
        ("Right", 15, 12),
        ("Right", 16, 12),
        ("Right", 17, 12),
        ("Right", 18, 12),
        ("Up", 18, 11),
        ("Up", 18, 10),
        ("Up", 18, 9),
        ("Up", 18, 8),
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
    print("Step 2: Dropping to 1F...")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    print("Landed on 1F! Position:", mgba.get_coordinates())
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    solve_all()
