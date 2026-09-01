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
# Walk to (2, 6) facing the switch at (2, 5).

path = [
    ("Up", 4),      # (21, 15) -> (21, 11)
    ("Left", 9),    # (21, 11) -> (12, 11)
    ("Up", 5),      # (12, 11) -> (12, 6)
    ("Left", 10)    # (12, 6) -> (2, 6)
]

print("Walking to the 3F West switch at (2, 5)...")
success = walk_path(path)
if success:
    print("Reached (2, 6) successfully! Turning UP to face the switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Toggle switch with 4 A-presses and check dialogue
    for i in range(1, 5):
        print(f"Pressing A ({i}/4)...")
        mgba.press_buttons(["A"])
        time.sleep(0.5)
        shot = mgba.take_screenshot()
        print(f"Screenshot saved: {shot}")
        
    print("Switch toggle complete. Checking coordinates:")
    print(mgba.get_coordinates())
else:
    print("Failed to reach (2, 6).")
