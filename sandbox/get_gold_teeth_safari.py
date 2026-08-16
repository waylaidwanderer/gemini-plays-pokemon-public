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

# ==========================================================
# PHASE 0: Fuchsia City to Safari Gatehouse
# ==========================================================
print("PHASE 0: Navigating Fuchsia City to Safari Gatehouse...")

fuchsia_waypoints = [
    (8, 32),
    (8, 30),   # Walk UP through ledge gap
    (24, 30),
    (26, 30),  # Through Column 25 fence gap
    (26, 14)
]

for wx, wy in fuchsia_waypoints:
    if not walk_to_waypoint(wx, wy):
        print(f"Failed fuchsia waypoint: ({wx}, {wy})")
        exit(1)

# Cut the bush at (26, 13)
print("Cutting bush at (26, 13)...")
bridge.press_buttons(["Up"]) # Ensure we face UP towards (26, 13)
time.sleep(0.5)
bridge.press_buttons(["Start"])
time.sleep(0.8)
bridge.press_buttons(["Down", "A"]) # POKEMON menu
time.sleep(1.0)
bridge.press_buttons(["Down", "A"]) # Select TRUFFLE
time.sleep(1.0)
bridge.press_buttons(["A"]) # Choose CUT
time.sleep(3.0) # Wait for animation
bridge.press_buttons(["B", "B"]) # Exit any remaining menu safely
time.sleep(1.0)

# Continue path to Gatehouse
fuchsia_gatehouse_waypoints = [
    (26, 9),
    (19, 9),
    (19, 8),
    (37, 8),
    (37, 2),
    (22, 2),
    (22, 4),
    (18, 4),
    (18, 3) # Emerge in Gatehouse
]

for wx, wy in fuchsia_gatehouse_waypoints:
    if not walk_to_waypoint(wx, wy):
        print(f"Failed gatehouse entry waypoint: ({wx}, {wy})")
        exit(1)

# Wait for map transition to Gatehouse
time.sleep(1.5)
curr = bridge.get_coordinates()
print("Entered Safari Gatehouse! Position:", curr)

# Navigate to clerk at (1, 4) from (3, 4)
walk_to_waypoint(3, 4)
bridge.press_buttons(["Left"]) # Face clerk
time.sleep(0.5)

# Speak to clerk, pay 500, and receive balls
print("Interacting with Gatekeeper clerk...")
bridge.press_buttons(["A"])
time.sleep(1.0)
for _ in range(8):
    bridge.press_buttons(["A"])
    time.sleep(0.8)

# Walk to Gatehouse exit at (3, 0)
print("Walking to Safari Zone Center entrance warp at (3, 0)...")
walk_to_waypoint(3, 0)
time.sleep(1.5)

curr = bridge.get_coordinates()
print("Entered Safari Zone Center! Position:", curr)

# ==========================================================
# PHASE 1: Safari Zone Center to Area 1 (East)
# ==========================================================
print("PHASE 1: Navigating Safari Zone Center...")
waypoints_center = [
    (15, 22),
    (28, 22),
    (28, 10)
]

for wx, wy in waypoints_center:
    if not walk_to_waypoint(wx, wy):
        print(f"Failed center waypoint: ({wx}, {wy})")
        exit(1)

# Step Right to transition to Area 1 (East)
print("Transitioning to Area 1 (East)...")
bridge.press_buttons(["Right", "Right"])
time.sleep(1.5)

curr = bridge.get_coordinates()
print("Entered Area 1 (East)! Position:", curr)

# ==========================================================
# PHASE 2: Area 1 (East) to Area 2 (North)
# ==========================================================
print("PHASE 2: Navigating Area 1 (East)...")
waypoints_area1 = [
    (0, 24),
    (20, 24),
    (20, 20), # Climb plateau stairs
    (12, 20),
    (12, 22), # Descend plateau stairs
    (8, 22),
    (8, 8),
    (12, 6),  # Climb northern plateau stairs
    (17, 6),
    (17, 8),  # Descend northern plateau stairs
    (20, 8),
    (20, 3),
    (7, 3),
    (7, 5)
]

for wx, wy in waypoints_area1:
    if not walk_to_waypoint(wx, wy):
        print(f"Failed Area 1 waypoint: ({wx}, {wy})")
        exit(1)

# Step Left to transition to Area 2 (North)
print("Transitioning to Area 2 (North)...")
bridge.press_buttons(["Left", "Left"])
time.sleep(1.5)

curr = bridge.get_coordinates()
print("Entered Area 2 (North)! Position:", curr)

# ==========================================================
# PHASE 3: Area 2 (North) to Area 3 (West)
# ==========================================================
print("PHASE 3: Navigating Area 2 (North)...")
waypoints_area2 = [
    (22, 31),
    (22, 22), # Climb Western Southern Plateau stairs
    (16, 22),
    (16, 28), # Descend plateau stairs
    (12, 28),
    (12, 30), # Bypass pond
    (8, 30),
    (8, 35)
]

for wx, wy in waypoints_area2:
    if not walk_to_waypoint(wx, wy):
        print(f"Failed Area 2 waypoint: ({wx}, {wy})")
        exit(1)

# Step Down to transition to Area 3 (West)
print("Transitioning to Area 3 (West)...")
bridge.press_buttons(["Down", "Down"])
time.sleep(1.5)

curr = bridge.get_coordinates()
print("Entered Area 3 (West)! Position:", curr)

# ==========================================================
# PHASE 4: Area 3 (West) to Gold Teeth & Retrieve
# ==========================================================
print("PHASE 4: Navigating Area 3 (West) to Gold Teeth...")
waypoints_area3 = [
    (26, 2),
    (25, 2),
    (25, 18),
    (21, 18),
    (21, 26), # Walk DOWN to Row 26 southern corridor
    (19, 26)  # Stand directly below the Gold Teeth
]

for wx, wy in waypoints_area3:
    if not walk_to_waypoint(wx, wy):
        print(f"Failed Area 3 waypoint: ({wx}, {wy})")
        exit(1)

# Standing at (19, 26) facing UP (North)
print("Standing below Gold Teeth at (19, 26). Facing UP...")
bridge.press_buttons(["Up"])
time.sleep(0.5)

print("Retrieving Gold Teeth...")
bridge.press_buttons(["A"])
time.sleep(1.0)
bridge.press_buttons(["A"])
time.sleep(0.8)
bridge.press_buttons(["A"])
time.sleep(0.8)

# DIG out of Safari Zone back to Fuchsia City Pokémon Center
print("Digging out of Safari Zone back to Fuchsia City...")
bridge.press_buttons(["Start"])
time.sleep(0.8)
bridge.press_buttons(["Down", "A"]) # POKEMON menu
time.sleep(1.0)
bridge.press_buttons(["Down", "A"]) # Select TRUFFLE
time.sleep(1.0)
bridge.press_buttons(["Down", "A"]) # Choose DIG
time.sleep(1.0)
bridge.press_buttons(["A"])
time.sleep(3.0) # Wait for DIG warp animation

final_pos = bridge.get_coordinates()
print("Mission Accomplished! Final Position:", final_pos)
