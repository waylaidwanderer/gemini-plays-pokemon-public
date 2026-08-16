import bridge
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.1)
    bridge.press_buttons(["Down", "Right", "A"])
    time.sleep(1.2)
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.1)
    print("Escape sequence complete.")

def walk_to_waypoint(target_x, target_y):
    print(f"Navigating to waypoint ({target_x}, {target_y})...")
    stuck_count = 0
    last_coords = None
    
    while True:
        curr = bridge.get_coordinates()
        if curr is None:
            print("Coordinates are None. Waiting...")
            time.sleep(0.5)
            continue
            
        x, y = curr
        if x == target_x and y == target_y:
            print(f"Reached waypoint ({target_x}, {target_y})")
            return True
            
        if curr == last_coords:
            stuck_count += 1
            if stuck_count > 4:
                print(f"Stuck at {curr} trying to reach ({target_x}, {target_y}). Attempting escape...")
                escape_battle()
                stuck_count = 0
                time.sleep(0.5)
                # Press B to recover any open menus
                bridge.press_buttons(["B", "B"])
                time.sleep(0.5)
        else:
            stuck_count = 0
            last_coords = curr
            
        # Choose direction to move
        if x < target_x:
            btn = "Right"
        elif x > target_x:
            btn = "Left"
        elif y < target_y:
            btn = "Down"
        elif y > target_y:
            btn = "Up"
            
        bridge.press_buttons([btn])
        time.sleep(0.44)

# We are currently at (3, 4) in the Gatehouse, with "Hi! Is it your first time here?" (YES/NO) open
print("Handling Safari Zone Clerk Dialogue from Turn 41056...")

# 1. "Is it your first time here?" (YES/NO, default YES) -> press A
bridge.press_buttons(["A"])
time.sleep(1.0)

# Mash A to clear rule explanations
for _ in range(8):
    bridge.press_buttons(["A"])
    time.sleep(0.8)
    
# "Would you like to join?" (YES/NO, default YES) -> press A
bridge.press_buttons(["A"])
time.sleep(1.0)

# Mash A to clear payment and ball receipts
for _ in range(6):
    bridge.press_buttons(["A"])
    time.sleep(0.8)
    
# Walk UP to row 0 to transition to Safari Center (15, 25)
print("Walking UP to warp...")
for _ in range(5):
    bridge.press_buttons(["Up"])
    time.sleep(0.4)
    
# Clear welcome dialogue
print("Clearing welcome dialogue and waiting for warp to (15, 25)...")
start_time = time.time()
while True:
    curr = bridge.get_coordinates()
    if curr is not None:
        if curr[0] == 15 and curr[1] == 25:
            print("Successfully entered Safari Zone Center! Position:", curr)
            break
    if time.time() - start_time > 10:
        print("Timeout waiting for warp. Forcing A press...")
        start_time = time.time()
    bridge.press_buttons(["A"])
    time.sleep(0.8)

# ----------------------------------------------------
# PHASE 1: Safari Zone Center directly to Area 1 (East)
# ----------------------------------------------------
print("PHASE 1: Navigating Safari Zone Center to Area 1 (East)...")
waypoints_center = [
    (15, 22),
    (28, 22),
    (28, 10)  # Stop adjacent to warp at (30, 10)
]

for wx, wy in waypoints_center:
    walk_to_waypoint(wx, wy)

# Step Right twice to transition to Area 1 (East)
print("Transitioning to Area 1 (East)...")
bridge.press_buttons(["Right"])
time.sleep(0.5)
bridge.press_buttons(["Right"])
time.sleep(1.0)

curr = bridge.get_coordinates()
print("Emerged in Area 1 (East) at:", curr)

# ----------------------------------------------------
# PHASE 2: Area 1 (East) to Area 2 (North)
# ----------------------------------------------------
print("PHASE 2: Navigating Area 1 (East) to Area 2 (North)...")
waypoints_area1 = [
    (0, 24),
    (20, 24),
    (20, 22),
    (20, 20), # Climbs plateau stairs
    (12, 20),
    (12, 22), # Descends plateau stairs
    (8, 22),
    (8, 8),
    (12, 8),
    (12, 6),  # Climbs northern stairs
    (17, 6),
    (17, 8),  # Descends northern stairs
    (20, 8),
    (20, 3),
    (7, 3),
    (7, 5),
    (1, 5)    # Stop adjacent to warp at (0, 5)
]

for wx, wy in waypoints_area1:
    walk_to_waypoint(wx, wy)

# Step Left twice to transition to Area 2 (North)
print("Transitioning to Area 2 (North)...")
bridge.press_buttons(["Left"])
time.sleep(0.5)
bridge.press_buttons(["Left"])
time.sleep(1.0)

curr = bridge.get_coordinates()
print("Emerged in Area 2 (North) at:", curr)

# ----------------------------------------------------
# PHASE 3: Area 2 (North) to Area 3 (West)
# ----------------------------------------------------
print("PHASE 3: Navigating Area 2 (North) to Area 3 (West)...")
waypoints_area2 = [
    (9, 3),   # Up to Row 3
    (20, 3),  # Right to Column 20
    (20, 9),  # Down to Row 9
    (17, 9),  # Left to Column 17
    (17, 8),  # Up to Row 8
    (17, 6),  # Up onto plateau Column 17 Row 6
    (12, 6),  # Left on plateau to Column 12 Row 6
    (12, 9),  # Down to Row 9 (descending stairs)
    (10, 9),  # Left to Column 10
    (10, 17), # Down Column 10 to Row 17
    (9, 17),  # Left to Column 9
    (9, 22),  # Down to Row 22
    (7, 22),  # Left to Column 7
    (7, 17),  # Up Column 7 to Row 17
    (6, 17),  # Left to Column 6
    (6, 9),   # Up Column 6 to Row 9
    (31, 9),  # Right Row 9 to Column 31
    (31, 13), # Down Column 31 to Row 13
    (33, 13), # Right to climb East Stairs
    (22, 15), # Left/down on plateau
    (20, 15), # Left to descend West Stairs
    (12, 15), # Left to Column 12
    (12, 28), # Down to Row 28
    (12, 30), # Bypass pond
    (8, 30),
    (8, 35)   # Stop adjacent to warp at (8, 36)
]

for wx, wy in waypoints_area2:
    walk_to_waypoint(wx, wy)

# Step Down twice to transition to Area 3 (West)
print("Transitioning to Area 3 (West)...")
bridge.press_buttons(["Down"])
time.sleep(0.5)
bridge.press_buttons(["Down"])
time.sleep(1.0)

curr = bridge.get_coordinates()
print("Emerged in Area 3 (West) at:", curr)

# ----------------------------------------------------
# PHASE 4: Area 3 (West) to Gold Teeth at (19, 24)
# ----------------------------------------------------
print("PHASE 4: Navigating Area 3 (West) to Gold Teeth...")
waypoints_area3 = [
    (26, 2),
    (25, 2),
    (25, 18),
    (21, 18),
    (21, 23),
    (19, 23),
    (19, 24)
]

for wx, wy in waypoints_area3:
    walk_to_waypoint(wx, wy)

# Retrieve Gold Teeth
print("Successfully reached (19, 24) directly above Gold Teeth!")
print("Facing DOWN...")
bridge.press_buttons(["Down"])
time.sleep(0.5)

print("Pressing A to retrieve Gold Teeth...")
bridge.press_buttons(["A"])
time.sleep(1.0)

# Clear dialogue
print("Clearing dialogue...")
bridge.press_buttons(["A"])
time.sleep(0.5)
bridge.press_buttons(["A"])
time.sleep(0.5)

final_pos = bridge.get_coordinates()
print("Retrieval Process Complete! Position:", final_pos)
