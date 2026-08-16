import mgba
import time

def walk_to_waypoint(target_x, target_y):
    print(f"Navigating to waypoint ({target_x}, {target_y})...")
    stuck_count = 0
    last_coords = None
    
    while True:
        curr = mgba.get_coordinates()
        if curr is None:
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
                return False
        else:
            stuck_count = 0
            last_coords = (x, y)
            
        if x < target_x: btn = "Right"
        elif x > target_x: btn = "Left"
        elif y < target_y: btn = "Down"
        else: btn = "Up"
        
        mgba.press_buttons([btn])
        time.sleep(0.42)

print("--- EXITING PC AND WALKING TO GATEHOUSE ---")
# Currently at (3, 6) inside PC.
# Step DOWN to (3, 7)
walk_to_waypoint(3, 7)

# Step DOWN to exit
print("Stepping DOWN to exit...")
mgba.press_buttons(["Down"])
time.sleep(1.5)

curr = mgba.get_coordinates()
print("Position outside PC:", curr)

if curr and curr['x'] == 19 and curr['y'] == 28:
    print("SUCCESS! Outside Pokémon Center.")
    
    # Step 2: Walk to Gatehouse entrance (18, 3)
    waypoints = [
        (24, 28),
        (24, 21),
        (22, 21),
        (22, 4),
        (18, 4),
        (18, 3) # Warp into Gatehouse
    ]
    for wp in waypoints:
        walk_to_waypoint(wp[0], wp[1])
        
    print("Transitioning into Gatehouse...")
    time.sleep(1.5)
    
    # Check position inside Gatehouse (should be 3, 5)
    curr = mgba.get_coordinates()
    print("Position inside Gatehouse:", curr)
    
    # Walk to (3, 4)
    walk_to_waypoint(3, 4)
    
    # Face LEFT
    print("Facing LEFT to speak to clerk...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    final_pos = mgba.get_coordinates()
    print("Final position inside Gatehouse:", final_pos)
    mgba.take_screenshot()
else:
    print("Failed to exit Pokémon Center. Verify current position.")
