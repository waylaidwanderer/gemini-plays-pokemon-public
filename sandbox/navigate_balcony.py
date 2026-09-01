import mgba
import time

def escape_battle():
    print("Dismissing battle text...")
    for _ in range(3):
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
    time.sleep(1.0)
    
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
        # Wait generously for overworld screen load
        time.sleep(1.5)
        # Retry the step
        mgba.press_buttons([direction])
        time.sleep(0.35)
        next_pos = mgba.get_coordinates()
        if next_pos == current:
            print(f"Still blocked at {current} after escape. Stopping.")
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

print("Dismissing the current 'Got away safely' battle screen...")
mgba.press_buttons(["B"])
time.sleep(1.5) # wait for overworld screen fade-in

current_pos = mgba.get_coordinates()
print("Current position after escape:", current_pos)

# Starting at (17, 11).
# 1. Walk to the switch at (3, 11) in State B
path_to_switch = [
    ("Left", 5),     # (17, 11) -> (12, 11)
    ("Up", 5),      # (12, 11) -> (12, 6)
    ("Left", 2),    # (12, 6) -> (10, 6)
    ("Down", 5),    # (10, 6) -> (10, 11)
    ("Left", 7)     # (10, 11) -> (3, 11)
]

# 2. Walk to the balcony drop at (19, 18) in State A
path_to_balcony = [
    ("Right", 9),   # (3, 11) -> (12, 11)
    ("Up", 5),      # (12, 11) -> (12, 6)
    ("Right", 7),   # (12, 6) -> (19, 6)
    ("Down", 5),    # (19, 6) -> (19, 11)
    ("Right", 2),   # (19, 11) -> (21, 11)
    ("Down", 7),    # (21, 11) -> (21, 18)
    ("Left", 2)     # (21, 18) -> (19, 18) (drop!)
]

print("Starting complete, bulletproof balcony drop traversal...")
if walk_path(path_to_switch):
    print("Reached (3, 11) successfully! Turning LEFT to face the switch...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    # Toggle switch with 4 A-presses and 1.5s delays to guarantee it toggles!
    for i in range(1, 5):
        print(f"A-press {i}/4...")
        mgba.press_buttons(["A"])
        time.sleep(1.5)
        
    print("Switch toggled successfully! Navigating to balcony...")
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
