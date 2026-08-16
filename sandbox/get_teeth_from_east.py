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

# We are currently at (13, 9) inside Safari Zone Area 1 (East)
print("Resuming Golden Route from Area 1 (East) at (13, 9)...")

# ----------------------------------------------------
# AREA 1 (EAST) TO AREA 2 (NORTH)
# ----------------------------------------------------
waypoints_area1 = [
    (12, 9),
    (12, 8),
    (12, 6),  # Climb West stairs of Northern Plateau
    (17, 6),  # Walk RIGHT on plateau
    (17, 8),  # Descend East stairs
    (20, 8),  # Walk RIGHT to Column 20
    (20, 3),  # Walk UP to Row 3
    (7, 3),   # Walk LEFT to Column 7
    (7, 5),   # Walk DOWN to Row 5
    (1, 5)    # Walk LEFT to Column 1 (adjacent to warp at (0, 5))
]

success = True
for wx, wy in waypoints_area1:
    if not walk_to_waypoint(wx, wy):
        print(f"Failed waypoint in Area 1: ({wx}, {wy})")
        success = False
        break

if success:
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
    # We can emerge at (39, 31) or (39, 5). We handle both dynamically!
    if curr is not None:
        cx, cy = curr
        waypoints_area2 = []
        if cy < 15:
            # We are in the northern part (39, 5)
            print("Detected northern start in Area 2. Routing via Column 39...")
            waypoints_area2 = [
                (39, 9),
                (39, 31),
                (22, 31)
            ]
        else:
            # We are in the southern part (39, 31)
            print("Detected southern start in Area 2. Routing directly to Column 22...")
            waypoints_area2 = [
                (22, 31)
            ]
            
        # Add the rest of the Area 2 path
        waypoints_area2.extend([
            (22, 22), # Climbs Southern Plateau stairs
            (16, 22),
            (16, 28), # Descends plateau stairs
            (12, 28),
            (12, 30), # Bypasses pond
            (8, 30),
            (8, 35)   # Stop adjacent to warp at (8, 36)
        ])

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
