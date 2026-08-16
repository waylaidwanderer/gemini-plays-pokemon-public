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

# 100% Physically Verified, Collision-Free Route to Pokemon Center from (36, 21)
waypoints = [
    (36, 17), # UP Column 36 to Row 17
    (37, 17), # RIGHT to Column 37
    (37, 9),  # UP Column 37 to Row 9
    (26, 9),  # LEFT Row 9 to Column 26
    (26, 14), # DOWN Column 26 to Row 14 (through cut bush at 26,13)
    (22, 14), # LEFT Row 14 to Column 22
    (22, 18), # DOWN Column 22 to Row 18
    (1, 18),  # LEFT Row 18 to Column 1
    (1, 32),  # DOWN Column 1 to Row 32
    (8, 32),  # RIGHT Row 32 to Column 8
    (8, 28),  # UP Column 8 through ledge gap to Row 28
    (19, 28), # RIGHT Row 28 to Column 19
    (19, 27)  # UP into the Pokémon Center!
]

print("Starting manual route to Pokemon Center from (36, 21)...")
success = True
for idx, (wx, wy) in enumerate(waypoints):
    print(f"Waypoint {idx+1}/{len(waypoints)}: ({wx}, {wy})")
    if not walk_to_waypoint(wx, wy):
        success = False
        break

if success:
    print("Successfully entered Fuchsia City Pokémon Center!")
    print("Position:", bridge.get_coordinates())
else:
    print("Failed manual route. Position:", bridge.get_coordinates())
