import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
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

# Currently at (19, 24)
print("--- NAVIGATING TO GOLD TEETH ---")

# 1. Walk UP to Row 18
walk_to_waypoint(19, 18)

# 2. Walk Right to Column 21
walk_to_waypoint(21, 18)

# 3. Walk DOWN Column 21 to Row 26
walk_to_waypoint(21, 26)

# 4. Walk Left to Column 19 on Row 26
walk_to_waypoint(19, 26)

# 5. Face UP (North)
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

# Take screenshot to verify if we see the item ball at (19, 25)
screenshot_path = mgba.take_screenshot()
print(f"Standing below teeth screenshot: {screenshot_path}")

# 6. Press A to pick up the Gold Teeth
print("Pressing A to pick up the Gold Teeth...")
mgba.press_buttons(["A"])
time.sleep(1.5)

# Clear dialogue "ACE picked up the GOLD TEETH!"
print("Clearing dialogue...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.press_buttons(["A"])
time.sleep(1.0)

# Check coordinates
curr = mgba.get_coordinates()
print("Position after retrieval:", curr)
screenshot_path2 = mgba.take_screenshot()
print(f"Final screenshot: {screenshot_path2}")
