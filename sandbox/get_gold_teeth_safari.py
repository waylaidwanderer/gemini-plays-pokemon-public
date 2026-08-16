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
# PHASE 0: Clear Entry Dialogue and Enter Safari Zone Center
# ==========================================================
print("Clearing gatehouse dialogue to enter Safari Zone...")
# We received 30 Safari Balls. Let's clear the remaining lines of dialogue.
for i in range(12):
    mgba.press_buttons(["A"])
    time.sleep(0.4)

print("Waiting for map transition to Safari Zone Center...")
time.sleep(2.0)

# Verify we are in Safari Zone Center at (15, 25)
coords = mgba.get_coordinates()
print("Emerged at coordinates:", coords)

# ==========================================================
# PHASE 1: Safari Zone Center -> Area 1 (East)
# ==========================================================
print("--- PHASE 1: Safari Zone Center to Area 1 (East) ---")
center_waypoints = [
    (15, 22),
    (28, 22),
    (28, 10)  # Stop exactly at (28, 10) before transition
]

for wp in center_waypoints:
    walk_to_waypoint(wp[0], wp[1])

print("Walking RIGHT to transition to Area 1 (East)...")
for _ in range(3):
    mgba.press_buttons(["Right"])
    time.sleep(0.5)

# Wait for transition
time.sleep(1.5)
coords = mgba.get_coordinates()
print("Emerged in Area 1 (East) at:", coords)

# ==========================================================
# PHASE 2: Area 1 (East) -> Area 2 (North)
# ==========================================================
print("--- PHASE 2: Area 1 (East) to Area 2 (North) ---")
# Emerge at (0, 22) or (0, 23). First go to (0, 24)
area1_waypoints = [
    (0, 24),
    (20, 24),
    (20, 20), # Climb plateau stairs
    (12, 20),
    (12, 22), # Descend plateau stairs
    (8, 22),
    (8, 8),
    (12, 8),  # Climb northern plateau stairs to (12, 6)
    (12, 6),
    (17, 6),
    (17, 8),  # Descend stairs to ground
    (20, 8),
    (20, 3),
    (7, 3),
    (7, 5)    # Stop exactly at (7, 5) before transition
]

for wp in area1_waypoints:
    walk_to_waypoint(wp[0], wp[1])

print("Walking LEFT to transition to Area 2 (North)...")
for _ in range(8):
    mgba.press_buttons(["Left"])
    time.sleep(0.5)

# Wait for transition
time.sleep(1.5)
coords = mgba.get_coordinates()
print("Emerged in Area 2 (North) at:", coords)

# ==========================================================
# PHASE 3: Area 2 (North) -> Area 3 (West)
# ==========================================================
print("--- PHASE 3: Area 2 (North) to Area 3 (West) ---")
# Emerge at (39, 31).
area2_waypoints = [
    (22, 31),
    (22, 22), # Climb stairs
    (16, 22),
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
