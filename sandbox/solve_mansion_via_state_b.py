import mgba
import time

# 1. Dismiss "Got away safely!"
print("Dismissing text box...")
mgba.press_buttons(["A"])
time.sleep(1.0) # Wait for overworld to load

def walk_step(direction, target_x, target_y):
    pos = mgba.get_coordinates()
    print(f"Standing at {pos}. Pressing {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    print(f"Now at {new_pos}. Target was ({target_x}, {target_y})")
    if new_pos['x'] == target_x and new_pos['y'] == target_y:
        return True
    else:
        print("Failed to reach target! Could be a battle or obstacle.")
        return False

def solve_final():
    # Current: (3, 12) on 2F in State B
    # Walk to (18, 8) stairs in State B
    print("Walking to stairs in State B...")
    path_to_stairs = [
        ("Up", 3, 11),
        ("Right", 4, 11),
        ("Right", 5, 11),
        ("Right", 6, 11),
        ("Right", 7, 11),
        ("Right", 8, 11),
        ("Right", 9, 11),
        ("Right", 10, 11),
        ("Right", 11, 11),
        ("Down", 11, 12),
        ("Down", 11, 13),
        ("Right", 12, 13),
        ("Right", 13, 13),
        ("Right", 14, 13),
        ("Right", 15, 13),
        ("Right", 16, 13),
        ("Right", 17, 13),
        ("Right", 18, 13),
        ("Up", 18, 12),
        ("Up", 18, 11),
        ("Up", 18, 10),
        ("Up", 18, 9),
    ]
    for d, tx, ty in path_to_stairs:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return
            
    # Step onto (18, 8) to warp to 3F in State B
    print("At (18, 9)! Stepping Up onto stairs warp...")
    mgba.press_buttons(["Up"])
    time.sleep(1.2)
    pos_3f = mgba.get_coordinates()
    print("Warp complete! Position on 3F:", pos_3f)
    
    # Walk on 3F (State B) to balcony drop
    print("Walking to balcony drop on 3F...")
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
            return
            
    # Drop to 1F!
    print("At balcony drop! Stepping Left off edge...")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    print("Landed on 1F! Position:", mgba.get_coordinates())
    mgba.take_screenshot()

solve_final()
