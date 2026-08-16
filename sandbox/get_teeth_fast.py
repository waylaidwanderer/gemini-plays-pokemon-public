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

# We are currently at (18, 33) inside Area 2 (North) with the signpost textbox open
print("Closing signpost textbox first...")
for _ in range(3):
    bridge.press_buttons(["B"])
    time.sleep(0.8)

# Now we are in the overworld at (18, 33) facing RIGHT
print("Resuming Golden Route in Area 2 (North) from (18, 33)...")

waypoints_area2 = [
    (18, 31), # Walk UP to Row 31 to bypass signpost
    (22, 31), # Walk LEFT/RIGHT to Column 22 on Row 31
    (22, 22), # Climb Western Southern Plateau stairs
    (16, 22), # Walk LEFT on the plateau to Column 16
    (16, 28), # Descend plateau stairs to ground level
    (12, 28),
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
    # Step Down twice to transition to Area 3 (West)
    print("Transitioning to Area 3 (West)...")
    bridge.press_buttons(["Down"])
    time.sleep(0.5)
    bridge.press_buttons(["Down"])
    time.sleep(1.0)

    curr = bridge.get_coordinates()
    print("Emerged in Area 3 (West) at:", curr)

    # ----------------------------------------------------
    # AREA 3 (WEST) TO GOLD TEETH AT (19, 24)
    # ----------------------------------------------------
    print("PHASE 4: Navigating Area 3 (West) to Gold Teeth...")
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
