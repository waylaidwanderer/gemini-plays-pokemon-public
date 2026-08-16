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

# We are currently at (13, 9) inside Area 1 (East)
print("Resuming Golden Route to retrieve Gold Teeth from (13, 9) inside Area 1...")

# ----------------------------------------------------
# PHASE 1: Area 1 (East) to Area 2 (North) Warp
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
    (1, 5)    # Walk LEFT to Column 1 (adjacent to warp)
]

success = True
for wx, wy in waypoints_area1:
    if not walk_to_waypoint(wx, wy):
        print(f"Failed waypoint in Area 1: ({wx}, {wy})")
        success = False
        break

if success:
    # We are at (1, 5). We must press Left TWICE to step onto (0, 5) and transition OFF the map boundary
    print("Transitioning to Area 2 (North) by walking OFF the edge...")
    bridge.press_buttons(["Left"])
    time.sleep(0.5)
    bridge.press_buttons(["Left"])
    time.sleep(1.0)
    
    curr = bridge.get_coordinates()
    print("Successfully entered Area 2 (North)! Current position:", curr)
    
    # ----------------------------------------------------
    # PHASE 2: Area 2 (North) to Area 3 (West) Warp
    # ----------------------------------------------------
    waypoints_area2 = [
        (22, 31), # Walk LEFT along open southern corridor
        (22, 22), # Climb Western Southern Plateau stairs
        (16, 22), # Walk LEFT on the plateau to Column 16
        (16, 28), # Descend stairs to ground level
        (12, 28),
        (12, 30), # Bypass pond
        (8, 30),
        (8, 35)   # Adjacent to warp at (8, 36)
    ]
    
    for wx, wy in waypoints_area2:
        if not walk_to_waypoint(wx, wy):
            print(f"Failed waypoint in Area 2: ({wx}, {wy})")
            success = False
            break

if success:
    # We are at (8, 35). We must press Down TWICE to step onto (8, 36) and transition OFF the map boundary
    print("Transitioning to Area 3 (West) by walking OFF the edge...")
    bridge.press_buttons(["Down"])
    time.sleep(0.5)
    bridge.press_buttons(["Down"])
    time.sleep(1.0)
    
    curr = bridge.get_coordinates()
    print("Successfully entered Area 3 (West)! Current position:", curr)
    
    # ----------------------------------------------------
    # PHASE 3: Area 3 (West) to Gold Teeth at (19, 24)
    # ----------------------------------------------------
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
