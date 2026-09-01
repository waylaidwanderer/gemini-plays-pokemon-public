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
        # Wait generously for the overworld to load back in!
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
# Walk final balcony drop path in State A:
path = [
    ("Right", 4),   # (17, 11) -> (21, 11)
    ("Down", 7),    # (21, 11) -> (21, 18)
    ("Left", 2)     # (21, 18) -> (19, 18) (drop!)
]

print("Starting final balcony drop path...")
success = walk_path(path)
if success:
    print("Drop executed successfully! Checking current location:")
    time.sleep(1.5) # wait for map transition / screen load
    print(mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("Balcony path interrupted. Current coordinates:")
    print(mgba.get_coordinates())
    mgba.take_screenshot()
