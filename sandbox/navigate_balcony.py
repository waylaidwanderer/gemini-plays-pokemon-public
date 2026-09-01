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

# Starting at (16, 11).
# 1. Walk to the switch at (2, 5) via Row 6
path_to_switch = [
    ("Right", 2),   # (16, 11) -> (18, 11)
    ("Up", 5),      # (18, 11) -> (18, 6)
    ("Left", 16)    # (18, 6) -> (2, 6)
]

# 2. Walk from (2, 6) to (19, 18) in State A
path_to_balcony = [
    ("Down", 5),    # (2, 6) -> (2, 11)
    ("Right", 10),  # (2, 11) -> (12, 11)
    ("Up", 5),      # (12, 11) -> (12, 6)
    ("Right", 9),   # (12, 6) -> (21, 6)
    ("Down", 12),   # (21, 6) -> (21, 18)
    ("Left", 2)     # (21, 18) -> (19, 18) (drop!)
]

print("Starting complete balcony drop solution sequence...")
if walk_path(path_to_switch):
    print("Reached (2, 6) successfully! Turning UP to face the switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # 4 A-presses to toggle
    for i in range(1, 5):
        print(f"A-press {i}...")
        mgba.press_buttons(["A"])
        time.sleep(0.5)
        
    print("Switch toggled to State A! Navigating to balcony...")
    success = walk_path(path_to_balcony)
    if success:
        print("Drop executed successfully! Checking current location:")
        time.sleep(1.0) # wait for map transition / screen load
        print(mgba.get_coordinates())
        mgba.take_screenshot()
    else:
        print("Interrupted during balcony path. Current coordinates:")
        print(mgba.get_coordinates())
        mgba.take_screenshot()
else:
    print("Failed to reach the switch.")
