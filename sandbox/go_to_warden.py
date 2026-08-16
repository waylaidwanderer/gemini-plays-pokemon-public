import bridge
import time

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
                print(f"Stuck at {curr} trying to reach ({target_x}, {target_y}). Retrying...")
                bridge.press_buttons(["A", "B"])
                time.sleep(0.5)
                stuck_count = 0
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

# Starting outside Fuchsia Pokemon Center at (19, 28)
print("Starting journey to Warden's House...")

# 1. Walk to Warden's House entrance at (27, 27)
walk_to_waypoint(19, 30)
walk_to_waypoint(27, 30)
walk_to_waypoint(27, 27)

# Enter the Warden's House (triggers transition)
print("Entering Warden's House...")
bridge.press_buttons(["Up"])
time.sleep(1.0)

# Check coordinates inside Warden's House (should emerge at (4, 7) or similar)
curr_house = bridge.get_coordinates()
print("Emerged inside Warden's House at:", curr_house)

if curr_house is not None and curr_house[1] <= 8:
    # 2. Walk to Warden at (2, 3)
    print("Walking to Warden at (2, 3)...")
    walk_to_waypoint(2, 4)
    bridge.press_buttons(["Up"])
    time.sleep(0.5)
    
    # 3. Talk to Warden and get HM04 (Strength)
    print("Talking to Warden...")
    bridge.press_buttons(["A"])
    time.sleep(1.0)
    
    # Mash A to clear dialogue until we receive HM04 and dialogue completely closes
    print("Mashing A to clear dialogue...")
    for _ in range(12):
        bridge.press_buttons(["A"])
        time.sleep(0.8)
        
    print("Warden Dialogue Complete! Position:", bridge.get_coordinates())
else:
    print("Warp failed or coordinates incorrect.")
