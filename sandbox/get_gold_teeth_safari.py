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

for wx, wy in fuchsia_waypoints:
    if not walk_to_waypoint(wx, wy):
        print(f"Failed fuchsia waypoint: ({wx}, {wy})")
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
