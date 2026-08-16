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
# PHASE 4 (RE-ROUTE THROUGH PLATEAU): (19, 24) -> Gold Teeth!
# ==========================================================
print("Closing BAG and Start menus...")
# Press B three times to exit BAG/menus completely and return to overworld
mgba.press_buttons(["B", "B", "B"])
time.sleep(1.5)

print("--- PHASE 4: RE-ROUTING THROUGH PLATEAU ---")
waypoints = [
    (19, 18), # Walk UP to Row 18
    (21, 18), # Walk RIGHT to Column 21 (under East Stairs)
    (21, 16), # Walk UP to climb East Stairs onto Plateau at (21, 16)
    (6, 16),  # Walk LEFT all the way on Plateau to (6, 16)
    (6, 20),  # Walk DOWN to descend West Stairs onto ground at (6, 20)
    (6, 26),  # Walk DOWN to Row 26 (Highway)
    (19, 26)  # Walk RIGHT to Column 19 (directly below the teeth!)
]

for wp in waypoints:
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
