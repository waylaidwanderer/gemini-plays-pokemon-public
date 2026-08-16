import bridge
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.1)
    bridge.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
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
                print(f"Unchanged position at {curr}. Checking if in battle...")
                escape_battle()
                stuck_count = 0
                time.sleep(0.5)
                after_coords = bridge.get_coordinates()
                if after_coords == curr:
                    print("Coordinates still unchanged. Retrying movement...")
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
        time.sleep(0.4)

# Waypoints starting from current position (10, 17) in Area 2 (North)
waypoints = [
    (9, 17),   # Walk left to Column 9
    (9, 35),   # Walk down Column 9 to southern corridor
    (8, 35),   # Walk left to Column 8
    (8, 36),   # Transitions to Area 3 (West) at (26, 0)
    
    # Phase 4: Area 3 (West) to (19, 24)
    (26, 2),
    (25, 2),
    (25, 18),
    (21, 18),
    (21, 23),
    (19, 23),
    (19, 24)
]

print("Continuing golden route from (10, 17)...")
success = True
for idx, (wx, wy) in enumerate(waypoints):
    print(f"Waypoint {idx+1}/{len(waypoints)}: ({wx}, {wy})")
    if not walk_to_waypoint(wx, wy):
        success = False
        break

if success:
    print("Reached (19, 24) successfully!")
    # Face DOWN
    bridge.press_buttons(["Down"])
    time.sleep(0.4)
    
    # Press A to pick up Gold Teeth
    print("Pressing A to retrieve Gold Teeth...")
    bridge.press_buttons(["A"])
    time.sleep(1.0)
    
    # Clear text box dialogue
    print("Clearing dialogue...")
    bridge.press_buttons(["A"])
    time.sleep(0.5)
    bridge.press_buttons(["A"])
    time.sleep(0.5)
    
    print("Retrieval process complete. Position:", bridge.get_coordinates())
else:
    print("Failed Golden Route. Position:", bridge.get_coordinates())
