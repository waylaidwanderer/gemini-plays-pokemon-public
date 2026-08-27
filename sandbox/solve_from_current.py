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

if pos == {"x": 12, "y": 9}:
    print("Walking to Column 20 Row 6...")
    steps = [
        ("Up", {"x": 12, "y": 8}),
        ("Up", {"x": 12, "y": 7}),
        ("Up", {"x": 12, "y": 6}),
    ]
    for x in range(13, 21):
        steps.append(("Right", {"x": x, "y": 6}))
    if run_steps(steps):
        print("Reached Column 20 on Row 6!")
    else:
        print("Failed to reach Column 20")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 20, "y": 6}:
    print("Walking UP Column 20 to Row 3...")
    steps_up_col20 = [
        ("Up", {"x": 20, "y": 5}),
        ("Up", {"x": 20, "y": 4}),
        ("Up", {"x": 20, "y": 3}),
    ]
    if run_steps(steps_up_col20):
        print("Reached Row 3 on Column 20!")
    else:
        print("Failed to reach Row 3 on Column 20")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 20, "y": 3}:
    print("Walking RIGHT along Row 3 to Column 26...")
    steps_to_pit = []
    for x in range(21, 27):
        steps_to_pit.append(("Right", {"x": x, "y": 3}))
    if run_steps(steps_to_pit):
        print("Reached Column 26 on Row 3!")
    else:
        print("Failed to reach Column 26 on Row 3")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 26, "y": 3}:
    print("Stepping DOWN to drop through the pitfall to 1F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Position after dropping to 1F East:", pos)

if pos == {"x": 26, "y": 4}:
    print("Walking to B1F East stairs...")
    steps_to_stairs = [
        ("Left", {"x": 25, "y": 4}),
        ("Left", {"x": 24, "y": 4}),
        ("Left", {"x": 23, "y": 4}),
        ("Left", {"x": 22, "y": 4}),
        ("Up", {"x": 22, "y": 3}),
    ]
    if not run_steps(steps_to_stairs):
        print("Failed to reach 1F East stairs")
        exit(1)
        
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping down to B1F East:", pos)

print("Finished current chunk! Current position:", pos)
