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

# Start from (19, 20)
print("--- NAVIGATING TO PC ENTRANCE VIA C24 ---")
waypoints = [
    (24, 20), # Walk RIGHT to Column 24
    (24, 28), # Walk DOWN Column 24 to Row 28
    (19, 28)  # Walk LEFT along Row 28 to Column 19
]

success = True
for wp in waypoints:
    if not walk_to_waypoint(wp[0], wp[1]):
        success = False
        break

if success:
    # Step Up to enter
    print("Stepping UP to enter Pokémon Center...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5)

    final_pos = mgba.get_coordinates()
    print("Position after entering:", final_pos)
    mgba.take_screenshot()
else:
    print("Failed to reach waypoints.")
