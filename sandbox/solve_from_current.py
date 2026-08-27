import mgba
import time
from PIL import Image

def escape_battle():
    print("Attempting to escape battle...")
    # Press B to back out of any sub-menus
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    # Select RUN (Down, Right, A)
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
    time.sleep(1.5)
    # Dismiss "Got away safely!" text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.2)

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Already at expected position: {pos}")
            return True
            
        # Try to move
        mgba.press_buttons([direction])
        time.sleep(0.5)
        
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Successfully moved {direction} to {pos}")
            return True
            
        print(f"Move {direction} failed. Current position: {pos}. (Expected: {expected_coords}). Attempting battle escape/dismissal.")
        escape_battle()
        time.sleep(0.5)
        
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"After escape, we are at expected position: {pos}")
            return True
            
    print(f"Failed to move {direction} to {expected_coords} after {retries} retries.")
    return False

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

pos = mgba.get_coordinates()
print("Starting Mansion solution from current position:", pos)

if pos == {"x": 3, "y": 11}:
    print("Beginning pathing to Row 6...")
    steps = [
        ("Left", {"x": 2, "y": 11}),
        ("Up", {"x": 2, "y": 10}),
        ("Up", {"x": 2, "y": 9}),
        ("Up", {"x": 2, "y": 8}),
        ("Up", {"x": 2, "y": 7}),
        ("Up", {"x": 2, "y": 6}),
    ]
    if not run_steps(steps):
        print("Failed to reach Row 6")
        exit(1)
    pos = mgba.get_coordinates()

# Walk RIGHT along Row 6 to Column 20 on 3F East
if pos == {"x": 2, "y": 6}:
    print("Walking RIGHT to Column 20...")
    steps_east = []
    for x in range(3, 21):
        steps_east.append(("Right", {"x": x, "y": 6}))
    if not run_steps(steps_east):
        print("Failed to reach Column 20")
        exit(1)
    pos = mgba.get_coordinates()

# Walk UP Column 20 to Row 3
if pos == {"x": 20, "y": 6}:
    print("Walking UP Column 20 to Row 3...")
    steps_up_col20 = [
        ("Up", {"x": 20, "y": 5}),
        ("Up", {"x": 20, "y": 4}),
        ("Up", {"x": 20, "y": 3}),
    ]
    if not run_steps(steps_up_col20):
        print("Failed to reach Row 3 on Column 20")
        exit(1)
    pos = mgba.get_coordinates()

# Walk RIGHT along Row 3 to Column 26
if pos == {"x": 20, "y": 3}:
    print("Walking RIGHT along Row 3 to Column 26...")
    steps_to_pit = []
    for x in range(21, 27):
        steps_to_pit.append(("Right", {"x": x, "y": 3}))
    if not run_steps(steps_to_pit):
        print("Failed to reach Column 26 on Row 3")
        exit(1)
    pos = mgba.get_coordinates()

# Step DOWN to drop through the pitfall to 1F East inside the fenced room
if pos == {"x": 26, "y": 3}:
    print("Stepping DOWN to drop through the pitfall to 1F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Position after dropping to 1F East:", pos)

# Walk to B1F East stairs
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

# Cross B1F East to B1F West NORTH and retrieve Secret Key!
if pos == {"x": 22, "y": 3} or pos == {"x": 22, "y": 2}:
    print("Crossing B1F East to B1F West NORTH...")
    if pos["y"] == 2:
        walk_step("Down", {"x": 22, "y": 3})
        pos = mgba.get_coordinates()
        
    if not run_steps([
        ("Down", {"x": 22, "y": 4}),
        ("Left", {"x": 21, "y": 4}),
        ("Left", {"x": 20, "y": 4}),
        ("Left", {"x": 19, "y": 4}),
        ("Down", {"x": 19, "y": 5}),
    ]):
        print("Failed to reach Row 5 on B1F East")
        exit(1)
        
    steps_left = []
    for x in range(18, 0, -1):
        steps_left.append(("Left", {"x": x, "y": 5}))
    if not run_steps(steps_left):
        print("Failed to reach Secret Key room")
        exit(1)
    pos = mgba.get_coordinates()

# Standing at (1, 5) facing UP, pick up the Secret Key!
if pos == {"x": 1, "y": 5}:
    print("Aligning UP towards the Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Retrieving the Secret Key...")
    mgba.press_buttons([
        "A", "sleep 2500",
        "A", "sleep 2500",
        "A", "sleep 2500"
    ])
    time.sleep(8.5)
    pos = mgba.get_coordinates()
    print("Final position after picking up Secret Key:", pos)

print("Mansion key retrieval sequence completed successfully!")
