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
                after_coords = bridge.get_coordinates()
                if after_coords == curr:
                    print("Coordinates still unchanged. Retrying movement with A/B mash...")
                    bridge.press_buttons(["A", "B", "A", "B"])
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

# Starting at (5, 22) in Safari Zone Area 1 (East)
print("Resuming Golden Route from Area 1 (East) at (5, 22)...")

# Walk down to Row 24 and resume Area 1 waypoints
walk_to_waypoint(4, 22)
walk_to_waypoint(4, 24)
walk_to_waypoint(5, 24)

waypoints_area1 = [
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
    if not walk_to_waypoint(wx, wy):
        print(f"Failed waypoint in Area 1: ({wx}, {wy})")
        break

# Step Left onto the warp to Area 2 (North)
print("Transitioning to Area 2 (North)...")
bridge.press_buttons(["Left"])
time.sleep(1.0)

# Check coordinates in Area 2 (North)
curr = bridge.get_coordinates()
print("Emerged in Area 2 (North) at:", curr)

# ----------------------------------------------------
# AREA 2 (NORTH) TO AREA 3 (WEST)
# ----------------------------------------------------
print("Navigating Area 2 (North)...")
waypoints_area2 = [
    (22, 31),
    (22, 22), # Climbs Southern Plateau stairs
    (16, 22),
    (16, 28), # Descends plateau stairs
    (12, 28),
    (12, 30), # Bypasses pond
    (8, 30),
    (8, 35)   # Stop adjacent to warp at (8, 36)
]

for wx, wy in waypoints_area2:
    if not walk_to_waypoint(wx, wy):
        print(f"Failed waypoint in Area 2: ({wx}, {wy})")
        break

# Step Down onto the warp to Area 3 (West)
print("Transitioning to Area 3 (West)...")
bridge.press_buttons(["Down"])
time.sleep(1.0)

# Check coordinates in Area 3 (West)
curr = bridge.get_coordinates()
print("Emerged in Area 3 (West) at:", curr)

# ----------------------------------------------------
# AREA 3 (WEST) TO GOLD TEETH AT (19, 24)
# ----------------------------------------------------
print("Navigating Area 3 (West)...")
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
    if not walk_to_waypoint(wx, wy):
        print(f"Failed waypoint in Area 3: ({wx}, {wy})")
        break

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
