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

# We are currently at (4, 2) in the Gatehouse, with "For just P500, you can catch all" open
print("Entering Safari Zone Entry Dialogue...")

# Let's advance dialogue
# 1. "For just P500, you can catch all" -> press A
bridge.press_buttons(["A"])
time.sleep(1.0)

# 2. "the POKéMON you want in the wild!" -> press A
bridge.press_buttons(["A"])
time.sleep(1.0)

# 3. "Would you like to join?" YES/NO menu -> press A to select YES
bridge.press_buttons(["A"])
time.sleep(1.0)

# 4. "That'll be P500 thanks!" -> press A
bridge.press_buttons(["A"])
time.sleep(1.0)

# 5. "We only use special Poké Balls here." -> press A
bridge.press_buttons(["A"])
time.sleep(1.0)

# 6. "ACE received 30 SAFARI BALLs!" -> press A
bridge.press_buttons(["A"])
time.sleep(1.0)

# 7. "We'll call you when you run out of time..." -> press A
bridge.press_buttons(["A"])
time.sleep(1.0)

# 8. "Best of luck!" -> press A to transition to warp
bridge.press_buttons(["A"])
time.sleep(1.0)

# Wait for warp to complete and we are at (15, 25) in Safari Center
print("Waiting for warp to Safari Zone Center (15, 25)...")
start_time = time.time()
while True:
    curr = bridge.get_coordinates()
    if curr is not None:
        if curr[0] == 15 and curr[1] == 25:
            print("Successfully entered Safari Zone Center! Current position:", curr)
            break
    if time.time() - start_time > 10:
        print("Timeout waiting for warp. Forcing A press...")
        start_time = time.time()
    bridge.press_buttons(["A"])
    time.sleep(0.8)

# ----------------------------------------------------
# PHASE 1: Safari Zone Center directly to Area 2 (North)
# ----------------------------------------------------
print("PHASE 1: Navigating Safari Zone Center...")
waypoints_center = [
    (15, 22),
    (28, 22),
    (28, 8),
    (15, 8),
    (15, 0) # transitions to Area 2 (North)
]

success = True
for wx, wy in waypoints_center:
    if not walk_to_waypoint(wx, wy):
        success = False
        break

if success:
    # We should have warped to Area 2 (North) southern corridor around (21, 35) or (20, 35)
    print("Entered Area 2 (North)! Position:", bridge.get_coordinates())
    
    # ----------------------------------------------------
    # PHASE 2: Area 2 (North) to Area 3 (West)
    # ----------------------------------------------------
    print("PHASE 2: Navigating Area 2 (North)...")
    waypoints_area2 = [
        (8, 35),
        (8, 36) # transitions to Area 3 (West)
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
    print("PHASE 3: Navigating Area 3 (West)...")
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
