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

print("Escaping wild battle first...")
escape_battle()

current_pos = mgba.get_coordinates()
print("Current position after escape:", current_pos)

# Starting at (11, 11).
# Walk final chunk: 1 step Right, 5 steps Up, 7 steps Right, 5 steps Down, 2 steps Right, 7 steps Down, 2 steps Left (drop!)
path = [
    ("Right", 1),   # (11, 11) -> (12, 11)
    ("Up", 5),      # (12, 11) -> (12, 6)
    ("Right", 7),   # (12, 6) -> (19, 6)
    ("Down", 5),    # (19, 6) -> (19, 11)
    ("Right", 2),   # (19, 11) -> (21, 11)
    ("Down", 7),    # (21, 11) -> (21, 18)
    ("Left", 2)     # (21, 18) -> (19, 18) (drop!)
]

print("Starting final balcony drop path...")
success = walk_path(path)
if success:
    print("Drop executed successfully! Checking current location:")
    time.sleep(1.0) # wait for map transition / screen load
    print(mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("Balcony path interrupted. Current coordinates:")
    print(mgba.get_coordinates())
    mgba.take_screenshot()
