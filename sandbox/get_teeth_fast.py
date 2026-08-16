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

# Starting at (26, 14) in Fuchsia City
print("Starting Ultimate Gold Teeth Route...")
print("Current position:", bridge.get_coordinates())

# Waypoints to Gatehouse from (26, 14)
waypoints_gatehouse = [
    (26, 9),
    (37, 9),
    (37, 2),
    (22, 2),
    (22, 4),
    (18, 4),
    (18, 3) # enters Gatehouse
]

success = True
for wx, wy in waypoints_gatehouse:
    if not walk_to_waypoint(wx, wy):
        success = False
        break

if success:
    print("Inside Safari Gatehouse! Moving to clerk...")
    # Walk to clerk at (2, 4)
    walk_to_waypoint(3, 5)
    walk_to_waypoint(3, 4)
    walk_to_waypoint(2, 4)
    bridge.press_buttons(["Left"])
    time.sleep(0.5)
    
    # Talk to clerk and pay 500
    print("Paying 500 Pokedollars...")
    bridge.press_buttons(["A"])
    time.sleep(0.8)
    bridge.press_buttons(["A"]) # YES to paying
    time.sleep(0.8)
    for _ in range(6):
        bridge.press_buttons(["A"])
        time.sleep(0.8)
        
    # Walk UP to row 0 to trigger welcome warp
    print("Walking UP to warp...")
    for _ in range(4):
        bridge.press_buttons(["Up"])
        time.sleep(0.4)
        
    # Clear welcome warp dialogue (mash A until coordinates change to Safari Center (15, 25))
    print("Clearing welcome dialogue...")
    while True:
        curr = bridge.get_coordinates()
        if curr != (2, 2) and curr != (3, 2) and curr != (4, 2) and curr is not None:
            # We warped!
            if curr[0] == 15 and curr[1] == 25:
                print("Successfully entered Safari Zone Center! Current position:", curr)
                break
        bridge.press_buttons(["A"])
        time.sleep(0.8)

    # ----------------------------------------------------
    # PHASE 1: Safari Zone Center directly to Area 2 (North)
    # ----------------------------------------------------
    waypoints_center = [
        (15, 22),
        (28, 22),
        (28, 8),
        (15, 8),
        (15, 0) # transitions to Area 2 (North) at (21, 35) or (20, 35)
    ]
    
    for wx, wy in waypoints_center:
        if not walk_to_waypoint(wx, wy):
            success = False
            break

if success:
    # We should have warped to Area 2 (North) southern corridor around (21, 35)
    print("Entered Area 2 (North)! Position:", bridge.get_coordinates())
    
    # ----------------------------------------------------
    # PHASE 2: Area 2 (North) to Area 3 (West)
    # ----------------------------------------------------
    waypoints_area2 = [
        (8, 35),
        (8, 36) # transitions to Area 3 (West) at (26, 0)
    ]
    
    for wx, wy in waypoints_area2:
        if not walk_to_waypoint(wx, wy):
            success = False
            break

if success:
    # We should have warped to Area 3 (West) at (26, 0)
    print("Entered Area 3 (West)! Position:", bridge.get_coordinates())
    
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
    
    # Verify coordinates and item retrieval
    final_pos = bridge.get_coordinates()
    print("Final Position:", final_pos)
else:
    print("Failed journey. Position:", bridge.get_coordinates())
