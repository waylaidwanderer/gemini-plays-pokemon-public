import mgba
import time

def escape_battle():
    print("Dismissing battle text...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        
    print("Waiting for SHELLBY send-out animation...")
    time.sleep(2.5) # generous delay
    
    print("Selecting RUN...")
    mgba.press_buttons(["Down"])
    time.sleep(0.25)
    mgba.press_buttons(["Right"])
    time.sleep(0.25)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    print("Dismissing 'Got away safely!'...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)

def step(direction):
    current = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.35)
    next_pos = mgba.get_coordinates()
    if next_pos == current:
        print(f"Blocked at {current}. Attempting battle escape...")
        escape_battle()
        time.sleep(1.5)
        # Retry the step
        mgba.press_buttons([direction])
        time.sleep(0.35)
        next_pos = mgba.get_coordinates()
        if next_pos == current:
            print(f"Still blocked at {current} after escape.")
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

# Starting at (5, 10).
# 1. Walk to the switch at (2, 5) from (2, 6) in State B
path_to_switch = [
    ("Down", 1),    # (5, 10) -> (5, 11)
    ("Left", 3),    # (5, 11) -> (2, 11)
    ("Up", 5)       # (2, 11) -> (2, 6)
]

# 2. Walk to the stairs at (5, 10) in State A
path_to_stairs = [
    ("Up", 4),      # (2, 6) -> (2, 2)
    ("Right", 3),   # (2, 2) -> (5, 2)
    ("Down", 8)     # (5, 2) -> (5, 10) (warp)
]

print("Executing 2F West Navigation...")
if walk_path(path_to_switch):
    print("Reached (2, 6) successfully! Turning UP to face the switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Toggle switch with 4 A-presses and 1.5s delays
    for i in range(1, 5):
        print(f"A-press {i}/4...")
        mgba.press_buttons(["A"])
        time.sleep(1.5)
        
    print("Switch toggled successfully to State A! Navigating to stairs...")
    success = walk_path(path_to_stairs)
    if success:
        print("Stairs taken successfully! Checking coordinates...")
        time.sleep(1.5) # wait for warp
        print("Final Position:", mgba.get_coordinates())
        mgba.take_screenshot()
    else:
        print("Interrupted on path to stairs. Coordinates:", mgba.get_coordinates())
        mgba.take_screenshot()
else:
    print("Failed to reach the switch.")
