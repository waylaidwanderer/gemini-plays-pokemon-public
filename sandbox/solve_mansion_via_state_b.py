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

def solve_remaining():
    # Current: (1, 11) on 2F
    # Walk to (2, 12)
    path_to_switch = [
        ("Down", 1, 12),
        ("Right", 2, 12),
    ]
    for d, tx, ty in path_to_switch:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return
            
    # Toggle switch to State B
    print("Toggling switch to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "A", "sleep 600", "A"])
    time.sleep(1.0)
    
    # Walk to (18, 8) stairs in State B
    print("Walking to stairs in State B...")
    path_to_stairs = [
        ("Right", 3, 12),
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
    print("Warp complete! Position on 3F:", mgba.get_coordinates())
    mgba.take_screenshot()

solve_remaining()
