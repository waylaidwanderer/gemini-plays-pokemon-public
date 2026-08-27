import mgba
import time

def escape_battle():
    print("Attempting to escape battle...")
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
    time.sleep(1.5)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.2)

def walk_step(direction, expected_coords, retries=10):
    for i in range(retries):
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            return True
        mgba.press_buttons([direction])
        time.sleep(0.5)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction} to {pos}")
            return True
        print(f"Blocked or battle! Current: {pos}, Expected: {expected_coords}")
        escape_battle()
        time.sleep(0.5)
    return False

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

pos = mgba.get_coordinates()
print("Starting from:", pos)

if pos == {"x": 24, "y": 11}:
    print("Walking to B1F East stairs...")
    steps = [
        ("Left", {"x": 23, "y": 11}),
        ("Up", {"x": 23, "y": 10}),
        ("Up", {"x": 23, "y": 9}),
        ("Up", {"x": 23, "y": 8}),
        ("Up", {"x": 23, "y": 7}),
        ("Left", {"x": 22, "y": 7}),
        ("Up", {"x": 22, "y": 6}),
        ("Up", {"x": 22, "y": 5}),
        ("Up", {"x": 22, "y": 4}),
        ("Up", {"x": 22, "y": 3}),
    ]
    if run_steps(steps):
        print("Reached B1F East stairs pre-warp!")
    else:
        print("Failed to reach stairs")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 22, "y": 3}:
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping down to B1F East:", pos)

print("Finished stairs warp! Current position:", pos)
