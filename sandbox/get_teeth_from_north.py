import bridge
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    # Mash B to clear any "appeared" text
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.1)
    
    # Select RUN (Down, Right, A)
    bridge.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    
    # Clear "Got away safely!" text
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
                # If we were in dialogue or battle, we cleared it.
                # Let's see if coordinates changed.
                after_coords = bridge.get_coordinates()
                if after_coords == curr:
                    print("Coordinates still unchanged. Retrying movement...")
                    # Sometimes we need to clear random text or handle a different screen
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

# Full Waypoint list from Safari Center entrance (15, 25) to (19, 24) in Area 3 (West)
waypoints = [
    # Phase 1: Center to Area 1 (East)
    (15, 22),
    (27, 22),
    (27, 10),
    (29, 10), # Transitions to Area 1 (East) at (0, 22)
    
    # Phase 2: Area 1 (East) to Area 2 (North)
    (20, 22),
    (20, 20), # Climb stairs
    (12, 20), # Walk left on plateau
    (12, 22), # Descend stairs
    (8, 22),
    (8, 8),
    (12, 8),
    (12, 6),  # Climb northern stairs
    (17, 6),  # Walk right on plateau
    (17, 8),  # Descend northern stairs
    (20, 8),
    (20, 3),  # Up to row 3
    (7, 3),   # Walk left along row 3
    (7, 5),   # Down to row 5
    (0, 5),   # Transitions to Area 2 (North) at (39, 31)
    
    # Phase 3: Area 2 (North) to Area 3 (West)
    (22, 31), # Walk left along row 31
    (22, 22), # Climb plateau stairs
    (16, 22), # Walk left on plateau
    (16, 28), # Descend stairs to grass
    (12, 28),
    (12, 30), # Bypass the pond
    (8, 30),
    (8, 35),  # Through the statue gap
    (8, 36),  # Transitions to Area 3 (West) at (26, 0)
    
    # Phase 4: Area 3 (West) to (19, 24)
    (26, 2),
    (25, 2),
    (25, 18),
    (21, 18),
    (21, 23),
    (19, 23),
    (19, 24)
]

print("Starting golden route to Gold Teeth...")
success = True
for idx, (wx, wy) in enumerate(waypoints):
    # If the map transition occurs, we might temporarily get None or jump coordinates.
    # The waypoint pathfinder handles this since it will navigate from whichever coordinate we currently are at.
    print(f"Waypoints progress: {idx}/{len(waypoints)}")
    if not walk_to_waypoint(wx, wy):
        success = False
        break

if success:
    print("Successfully reached (19, 24) facing DOWN!")
    # Face DOWN
    bridge.press_buttons(["Down"])
    time.sleep(0.4)
    
    # Interact with Gold Teeth at (19, 25)
    print("Pressing A to retrieve Gold Teeth...")
    bridge.press_buttons(["A"])
    time.sleep(1.0)
    
    # Clear text box dialogue
    print("Clearing dialogue...")
    bridge.press_buttons(["A"])
    time.sleep(0.5)
    bridge.press_buttons(["A"])
    time.sleep(0.5)
    
    print("Retrieved Gold Teeth! Current position:", bridge.get_coordinates())
else:
    print("Failed golden route. Current position:", bridge.get_coordinates())
