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

# Starting at (12, 11).
# Walk to (3, 11).
path = [
    ("Left", 9)     # (12, 11) -> (3, 11)
]

print("Walking from (12, 11) to (3, 11)...")
if walk_path(path):
    print("Reached (3, 11)! Turning Left to face the statue at (2, 11)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    # Inspect the switch dialogue step-by-step
    for i in range(1, 5):
        print(f"Pressing A ({i}/4)...")
        mgba.press_buttons(["A"])
        time.sleep(0.5)
        # Capture screenshot to see what is on screen
        shot = mgba.take_screenshot()
        print(f"Screenshot saved after A-press {i}: {shot}")
        
    print("Dialogue inspection complete. Final coordinates:")
    print(mgba.get_coordinates())
else:
    print("Failed to reach (3, 11).")
