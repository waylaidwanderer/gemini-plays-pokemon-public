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

# 1. Walk from (10, 10) to (3, 11)
path = [
    ("Down", 1),    # (10, 10) -> (10, 11)
    ("Left", 7)     # (10, 11) -> (3, 11)
]

print("Resuming navigation to (3, 11)...")
if walk_path(path):
    print("Reached (3, 11) successfully! Turning LEFT to face the switch...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    print("Final position check:", mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("Navigation interrupted. Current coordinates:")
    print(mgba.get_coordinates())
    mgba.take_screenshot()
