import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    # Highlight RUN (Down, Right) and select
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
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
# PHASE 3: Area 2 (North) -> Area 3 (West) (Starting at (20, 22))
# ==========================================================
print("--- PHASE 3 (CONTINUED): Area 2 (North) to Area 3 (West) ---")
# Start at (20, 22) on the plateau.
area2_waypoints = [
    (16, 22), # Walk left on plateau
    (16, 28), # Descend stairs
    (12, 28),
    (12, 30), # Bypass pond
    (8, 30),
    (8, 35)   # Stop exactly at (8, 35) before transition
]

for wp in area2_waypoints:
    walk_to_waypoint(wp[0], wp[1])

print("Walking DOWN to transition to Area 3 (West)...")
for _ in range(3):
    mgba.press_buttons(["Down"])
    time.sleep(0.5)

# Wait for transition
time.sleep(1.5)
coords = mgba.get_coordinates()
print("Emerged in Area 3 (West) at:", coords)

# ==========================================================
# PHASE 4: Area 3 (West) -> Retrieve Gold Teeth
# ==========================================================
print("--- PHASE 4: Area 3 (West) to Gold Teeth ---")
# Emerge at (26, 0).
area3_waypoints = [
    (26, 2),
    (25, 2),
    (25, 18),
    (21, 18),
    (21, 26), # Walk down to the Row 26 Highway
    (19, 26)  # Stand at (19, 26) directly below the teeth!
]

for wp in area3_waypoints:
    walk_to_waypoint(wp[0], wp[1])

# Stand at (19, 26) facing UP (North)
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

# Press A to pick up the Gold Teeth
print("Pressing A to pick up the Gold Teeth!")
mgba.press_buttons(["A"])
time.sleep(1.5)

# Clear dialogue "ACE picked up the GOLD TEETH!"
print("Clearing dialogue...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Retrieval process fully complete! Current position:", mgba.get_coordinates())
