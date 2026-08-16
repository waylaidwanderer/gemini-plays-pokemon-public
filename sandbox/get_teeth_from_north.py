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
# We start at (9, 5) inside Safari Zone Area 2 (North)
# ==========================================================
print("--- RESUMING JOURNEY FROM AREA 2 (NORTH) (9, 5) ---")

area2_waypoints = [
    (9, 3),    # Walk UP to the open Row 3
    (31, 3),   # Walk RIGHT along Row 3 to Column 31 (bypassing barriers)
    (31, 13),  # Walk DOWN Column 31 to Row 13 in front of East Stairs
    (33, 13),  # Walk RIGHT climbing East Stairs onto plateau
    (37, 14),  # Walk onto the Eastern Land Bridge
    (37, 26),  # Walk DOWN the Eastern Land Bridge to Row 26
    (28, 26),  # Walk LEFT to the Southern Plateau exit
    (28, 28),  # Walk DOWN descending Southern Plateau stairs
    (22, 31),  # Walk to Southern Corridor start
    (22, 22),  # Climb Western Southern Plateau stairs
    (16, 22),  # Walk LEFT on plateau
    (16, 28),  # Descend stairs
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
# PHASE 4: Area 3 (West) -> Retrieve Gold Teeth (Corrected Route!)
# ==========================================================
print("--- PHASE 4: Area 3 to Gold Teeth (Corrected Route!) ---")
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
