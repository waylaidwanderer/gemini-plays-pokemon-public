import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    # Clear any battle start text
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    # Highlight RUN (Down, Right) and select
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    # Clear "ACE ran away" text
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

print("--- PAYING AND ENTERING SAFARI ZONE ---")
# Currently at (4, 3) in Gatehouse.
# Walk to (3, 4)
walk_to_waypoint(3, 4)

# Face LEFT
print("Facing LEFT to speak to clerk...")
mgba.press_buttons(["Left"])
time.sleep(0.5)

# Talk to clerk to pay and enter
print("Speaking to clerk...")
mgba.press_buttons(["A"])
time.sleep(1.0)
# "Would you like to join the hunt?"
mgba.press_buttons(["A"])
time.sleep(1.0)
# Select YES (default)
mgba.press_buttons(["A"])
time.sleep(1.0)
# "That'll be 500. We only use special Pokeballs."
mgba.press_buttons(["A"])
time.sleep(1.0)
# "ACE received 30 SAFARI BALLS!"
mgba.press_buttons(["A"])
time.sleep(1.0)
# "We'll call you when you run out of time or SAFARI BALLS!"
mgba.press_buttons(["A"])
time.sleep(1.0)
# "Good luck!"
mgba.press_buttons(["A"])
time.sleep(1.0)

# Walk into the warp door at (3, 0) or (4, 0)
print("Entering Safari Zone Center...")
walk_to_waypoint(3, 1)
mgba.press_buttons(["Up"])
time.sleep(1.5)

curr_pos = mgba.get_coordinates()
print("Position inside Safari Zone Center:", curr_pos)

# ==========================================================
# PHASE 1: Safari Zone Center -> Area 1 (East)
# ==========================================================
print("--- PHASE 1: Center to Area 1 (East) ---")
center_waypoints = [
    (15, 22),
    (28, 22),
    (28, 10),
    (30, 10) # Walk RIGHT to transition to Area 1 (East)
]
for wp in center_waypoints:
    walk_to_waypoint(wp[0], wp[1])
time.sleep(1.0)

# ==========================================================
# PHASE 2: Area 1 (East) -> Area 2 (North)
# ==========================================================
print("--- PHASE 2: Area 1 to Area 2 (North) ---")
area1_waypoints = [
    (0, 24),
    (20, 24),
    (20, 22),
    (20, 20), # Climb plateau stairs
    (12, 20), # Walk LEFT on plateau
    (12, 22), # Descend stairs
    (8, 22),
    (8, 8),
    (12, 8),
    (12, 6),  # Climb northern plateau stairs
    (17, 6),  # Walk RIGHT on plateau
    (17, 8),  # Descend plateau stairs
    (20, 8),
    (20, 3),
    (7, 3),
    (7, 5),
    (0, 5)    # Walk LEFT to transition to Area 2 (North)
]
for wp in area1_waypoints:
    walk_to_waypoint(wp[0], wp[1])
time.sleep(1.0)

# ==========================================================
# PHASE 3: Area 2 (North) -> Area 3 (West) (Corrected Northwest Route!)
# ==========================================================
print("--- PHASE 3: Area 2 to Area 3 (West) ---")
area2_waypoints = [
    (9, 3),    # Walk UP Column 9 to Row 3
    (20, 3),   # Walk RIGHT along Row 3 to Column 20
    (20, 11),  # Walk DOWN Column 20 to Row 11
    (25, 11),  # Walk RIGHT to Column 25
    (25, 17),  # Walk DOWN to Row 17
    (31, 17),  # Walk RIGHT to Column 31
    (31, 13),  # Walk UP to Row 13
    (32, 13),  # Climb East Stairs onto Northern Plateau
    (37, 13),  # Walk RIGHT on plateau
    (37, 26),  # Walk DOWN Eastern Land Bridge to Row 26
    (28, 26),  # Walk LEFT on plateau
    (28, 28),  # Descend Southern Plateau stairs to ground
    (22, 31),  # Walk LEFT along southern corridor
    (22, 22),  # Climb Western Southern Plateau stairs
    (16, 22),  # Walk LEFT on plateau
    (16, 28),  # Descend stairs to grass
    (12, 28),
    (12, 30),  # Bypass pond
    (8, 30),
    (8, 35)    # Adjacent to warp
]
for wp in area2_waypoints:
    walk_to_waypoint(wp[0], wp[1])

print("Walking DOWN to transition to Area 3 (West)...")
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
