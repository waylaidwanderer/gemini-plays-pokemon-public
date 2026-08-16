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

# We are at (6, 17) inside Safari Zone Area 2 (North)
print("Resuming Golden Route to retrieve Gold Teeth from (6, 17)...")

waypoints_area2 = [
    (6, 9),   # Walk UP to open horizontal Row 9
    (31, 9),  # Walk RIGHT to Column 31
    (31, 13), # Walk DOWN Column 31 to Row 13
    (33, 13), # Walk RIGHT to climb East Stairs
    (22, 15), # Walk LEFT/DOWN on plateau to Column 22 Row 15
    (20, 15), # Walk LEFT to descend West Stairs
    (12, 15), # Walk LEFT to Column 12
    (12, 28), # Walk DOWN to Row 28
    (12, 30), # Bypass pond
    (8, 30),
    (8, 35)   # Stop adjacent to warp at (8, 36)
]

success = True
for wx, wy in waypoints_area2:
    if not walk_to_waypoint(wx, wy):
        print(f"Failed waypoint in Area 2: ({wx}, {wy})")
        success = False
        break

if success:
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
            success = False
            break

if success:
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
else:
    print("Failed journey. Position:", bridge.get_coordinates())
