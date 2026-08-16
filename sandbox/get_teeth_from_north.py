import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.2)
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Escape sequence complete.")

def walk_to_waypoint(target_x, target_y):
    print(f"Navigating to waypoint ({target_x}, {target_y})...")
    stuck_count = 0
    last_coords = None
    
    while True:
        curr = mgba.get_coordinates()
        if curr is None:
            print("Coordinates are None. Waiting...")
            time.sleep(0.5)
            continue
            
        x, y = curr['x'], curr['y']
        if x == target_x and y == target_y:
            print(f"Reached waypoint ({target_x}, {target_y})")
            return True
            
        if (x, y) == last_coords:
            stuck_count += 1
            if stuck_count > 3:
                print(f"Stuck at ({x}, {y}) trying to reach ({target_x}, {target_y})")
                escape_battle()
                time.sleep(0.5)
                stuck_count = 0
                after = mgba.get_coordinates()
                if after['x'] == x and after['y'] == y:
                    print("Coordinates unchanged. Pressing A/B...")
                    mgba.press_buttons(["A", "B", "A", "B"])
                    time.sleep(0.5)
        else:
            stuck_count = 0
            last_coords = (x, y)
            
        # Choose direction to move
        if x < target_x:
            btn = "Right"
        elif x > target_x:
            btn = "Left"
        elif y < target_y:
            btn = "Down"
        elif y > target_y:
            btn = "Up"
            
        mgba.press_buttons([btn])
        time.sleep(0.42)

# Start at (26, 1) inside Area 3 (West)
print("--- PHASE 4: Area 3 (West) Navigation to Gold Teeth ---")

# Walk to (25, 2)
walk_to_waypoint(25, 2)

# Walk DOWN Column 25 to Row 18
walk_to_waypoint(25, 18)

# Walk Left to Column 21
walk_to_waypoint(21, 18)

# Now, we want to try walking DOWN Column 21 to Row 26.
# If Column 21 is blocked, we will walk Left to Column 19 and walk DOWN Column 19.
curr_pos = mgba.get_coordinates()
cx, cy = curr_pos['x'], curr_pos['y']

print("Attempting to walk DOWN Column 21...")
blocked = False
while cy < 26:
    mgba.press_buttons(["Down"])
    time.sleep(0.42)
    new_pos = mgba.get_coordinates()
    nx, ny = new_pos['x'], new_pos['y']
    if ny == cy:
        # Check if battle or blocked
        escape_battle()
        time.sleep(0.5)
        after_pos = mgba.get_coordinates()
        if after_pos['y'] == cy:
            print("Column 21 is BLOCKED vertically! Trying Column 19...")
            blocked = True
            break
    cx, cy = nx, ny

if blocked:
    # Walk Left to Column 19 on Row 18
    walk_to_waypoint(19, 18)
    
    # Walk DOWN Column 19 to Row 26
    walk_to_waypoint(19, 26)
else:
    # Walk Left from (21, 26) to (19, 26)
    walk_to_waypoint(19, 26)

# We are at (19, 26). Stand facing UP (North)
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

# Press A to pick up the Gold Teeth!
print("Pressing A to pick up the Gold Teeth!")
mgba.press_buttons(["A"])
time.sleep(1.5)

# Clear dialogue "ACE picked up the GOLD TEETH!"
print("Clearing dialogue...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.press_buttons(["A"])
time.sleep(1.0)

final_coords = mgba.get_coordinates()
print("Position after picking up teeth:", final_coords)
screenshot_path = mgba.take_screenshot()
print(f"Screenshot: {screenshot_path}")
