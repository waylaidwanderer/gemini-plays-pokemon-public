import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    # Press Down, Right, A to run
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Escape sequence complete.")

def step(direction):
    curr = mgba.get_coordinates()
    cx, cy = curr['x'], curr['y']
    mgba.press_buttons([direction])
    time.sleep(0.45)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == cx and new_pos['y'] == cy:
        # Blocked or battle
        # Check if in battle (let's do escape_battle just in case)
        escape_battle()
        time.sleep(0.5)
        after = mgba.get_coordinates()
        if after['x'] == cx and after['y'] == cy:
            print(f"Collision moving {direction} from ({cx}, {cy})")
            return False, (cx, cy)
        else:
            print(f"Moved successfully after escaping battle to ({after['x']}, {after['y']})")
            return True, (after['x'], after['y'])
    else:
        return True, (new_pos['x'], new_pos['y'])

# We are at (19, 24).
# Let's explore the left side by trying to find a path to y=26.
# We will do a simple exploration.
# Let's try to walk Left to Column 16.
print("Starting exploration from (19, 24)...")
visited = set([(19, 24)])
path = []

def walk_to_waypoint(target_x, target_y):
    while True:
        curr = mgba.get_coordinates()
        cx, cy = curr['x'], curr['y']
        if cx == target_x and cy == target_y:
            return True
        if cx < target_x: btn = "Right"
        elif cx > target_x: btn = "Left"
        elif cy < target_y: btn = "Down"
        else: btn = "Up"
        
        success, pos = step(btn)
        if not success:
            return False

# Try walking UP to Row 18
print("Walking UP to Row 18...")
for _ in range(6):
    success, pos = step("Up")
    if not success or pos[1] == 18:
        break

# Now we are at some y <= 24. Let's try to walk Left to Column 16
curr = mgba.get_coordinates()
cx, cy = curr['x'], curr['y']
print(f"At ({cx}, {cy}). Trying to walk Left to Column 16...")
for _ in range(10):
    curr = mgba.get_coordinates()
    if curr['x'] == 16:
        break
    success, pos = step("Left")
    if not success:
        # If blocked Left, try walking UP
        print("Blocked Left. Trying to go UP...")
        success_up, pos_up = step("Up")
        if not success_up:
            print("Also blocked UP!")
            break

# Let's check our position
curr = mgba.get_coordinates()
cx, cy = curr['x'], curr['y']
print(f"After trying Left: At ({cx}, {cy})")

# Try to walk DOWN to Row 26
print("Trying to walk DOWN to Row 26...")
for _ in range(15):
    curr = mgba.get_coordinates()
    if curr['y'] == 26:
        print("REACHED ROW 26!!!")
        break
    success, pos = step("Down")
    if not success:
        # Blocked DOWN, try Left or Right
        print("Blocked DOWN. Trying Left...")
        success_l, pos_l = step("Left")
        if not success_l:
            print("Blocked Left too. Trying Right...")
            success_r, pos_r = step("Right")
            if not success_r:
                print("Completely blocked!")
                break

curr = mgba.get_coordinates()
print("Final exploration position:", curr)
mgba.take_screenshot()
