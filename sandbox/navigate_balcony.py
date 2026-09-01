import mgba
import time

def step(direction):
    current = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.35)
    next_pos = mgba.get_coordinates()
    if next_pos == current:
        print(f"Blocked at {current} trying to move {direction}")
        return False
    return next_pos

def walk_path(path_steps):
    for direction, count in path_steps:
        print(f"Moving {direction} {count} times...")
        for _ in range(count):
            res = step(direction)
            if not res:
                return False
            print(f"Moved to {res}")
    return True

# Starting at (21, 15).
# 1. Walk back to (3, 11) to toggle the switch properly.
path_to_switch = [
    ("Up", 4),      # (21, 15) -> (21, 11)
    ("Left", 18)    # (21, 11) -> (3, 11)
]

# 2. Walk to the balcony in State A.
path_to_balcony = [
    ("Right", 18),  # (3, 11) -> (21, 11)
    ("Down", 7),    # (21, 11) -> (21, 18)
    ("Left", 2)     # (21, 18) -> (19, 18) (drop!)
]

print("Walking to the switch at (3, 11)...")
if walk_path(path_to_switch):
    print("Reached (3, 11)! Facing LEFT towards the switch at (2, 11)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    # Toggle switch with 4 A-presses and GENEROUS 1.2s delays
    for i in range(1, 5):
        print(f"A-press {i}/4...")
        mgba.press_buttons(["A"])
        time.sleep(1.2)
        
    print("Switch toggled. Walking to the balcony in State A...")
    success = walk_path(path_to_balcony)
    if success:
        print("Balcony drop executed successfully! Checking current position:")
        time.sleep(1.0)
        print(mgba.get_coordinates())
        mgba.take_screenshot()
    else:
        print("Failed on the balcony path. Current coordinates:")
        print(mgba.get_coordinates())
        mgba.take_screenshot()
else:
    print("Failed to reach the switch.")
