import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    # Highlight RUN (Down, Right) and select
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
            if stuck_count > 4:
                print(f"Stuck at ({x}, {y}) trying to reach ({target_x}, {target_y})")
                escape_battle()
                stuck_count = 0
                time.sleep(0.5)
                after_coords = mgba.get_coordinates()
                if after_coords['x'] == x and after_coords['y'] == y:
                    print("Coordinates still unchanged. Clearing text boxes...")
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

# ==========================================================
# We start at (21, 11) inside Safari Zone Area 2 (North)
# ==========================================================
print("--- RUNNING FULL GOLD TEETH RETRIEVAL FROM CURRENT POSITION ---")

# Step 1: Reach East Stairs of Northern Plateau in Area 2 (North)
area2_part1 = [
    (31, 11),  # Walk RIGHT to Column 31
    (31, 13),  # Walk DOWN to Row 13 (adjacent to stairs)
    (32, 13),  # Walk RIGHT onto stairs to climb the Northern Plateau
]

# Step 2: Traverse Plateau and Southern Corridor to transition to Area 3 (West)
area2_part2 = [
    (37, 13),  # Walk RIGHT on plateau to Eastern Land Bridge
    (37, 26),  # Walk DOWN Eastern Land Bridge to Row 26
    (28, 26),  # Walk LEFT to Southern Plateau exit stairs
    (28, 28),  # Descend stairs to ground level Southern Corridor
    (22, 31),  # Walk LEFT to Column 22
    (22, 22),  # Climb Western Southern Plateau stairs
    (16, 22),  # Walk LEFT on plateau
    (16, 28),  # Descend Western stairs to grass
    (12, 28),  # Walk LEFT to Column 12
    (12, 30),  # Walk DOWN to Row 30 to bypass the pond
    (8, 30),   # Walk LEFT to Column 8
    (8, 35)    # Walk DOWN adjacent to warp
]

# Execute Area 2 Part 1
print("Executing Area 2 Part 1: Climbing Northern Plateau...")
for wp in area2_part1:
    walk_to_waypoint(wp[0], wp[1])

# Execute Area 2 Part 2
print("Executing Area 2 Part 2: Navigating to Area 3 (West)...")
for wp in area2_part2:
    walk_to_waypoint(wp[0], wp[1])

print("Transitioning to Area 3 (West)...")
mgba.press_buttons(["Down"])
time.sleep(0.5)
mgba.press_buttons(["Down"])
time.sleep(1.0)

# ==========================================================
# PHASE 4: Area 3 (West) -> Retrieve Gold Teeth
# ==========================================================
print("--- PHASE 4: Area 3 to Gold Teeth ---")
area3_waypoints = [
    (26, 2),
    (25, 2),
    (25, 18),
    (21, 18),
    (21, 16), # Climb East Stairs onto plateau
    (6, 16),  # Walk LEFT across plateau
    (6, 20),  # Descend West Stairs to ground level
    (6, 26),  # Walk DOWN Column 6 to the Row 26 Highway
    (19, 26)  # Walk RIGHT along Row 26 directly below Gold Teeth
]
for wp in area3_waypoints:
    walk_to_waypoint(wp[0], wp[1])

# Stand at (19, 26) facing UP
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

# Take screenshot to verify item ball is present
screenshot_path = mgba.take_screenshot()
print(f"Standing below teeth screenshot: {screenshot_path}")

# Press A to pick up the Gold Teeth
print("Pressing A to pick up the Gold Teeth...")
mgba.press_buttons(["A"])
time.sleep(1.5)

# Clear dialogue "ACE picked up the GOLD TEETH!"
print("Clearing dialogue...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.press_buttons(["A"])
time.sleep(1.0)

final_pos = mgba.get_coordinates()
print("Position after retrieval attempt:", final_pos)
screenshot_path2 = mgba.take_screenshot()
print(f"Final screenshot: {screenshot_path2}")
