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

print("--- EXITING PC ---")
# Currently at (12, 7) inside PC.
# Walk UP to Row 5, LEFT to Column 3, DOWN to Row 7, then exit!
waypoints = [
    (12, 5),
    (3, 5),
    (3, 7)
]

success = True
for wp in waypoints:
    if not walk_to_waypoint(wp[0], wp[1]):
        success = False
        break

if success:
    print("Stepping DOWN to exit...")
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    final_pos = mgba.get_coordinates()
    print("Final position outside:", final_pos)
    mgba.take_screenshot()
else:
    print("Failed to exit PC.")
