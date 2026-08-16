import mgba
import time

def move_to(target_x, target_y):
    current = mgba.get_coordinates()
    cx, cy = current['x'], current['y']
    print(f"Starting movement from ({cx}, {cy}) to ({target_x}, {target_y})")
    
    while (cx != target_x) or (cy != target_y):
        if cx < target_x:
            btn = "Right"
            next_x, next_y = cx + 1, cy
        elif cx > target_x:
            btn = "Left"
            next_x, next_y = cx - 1, cy
        elif cy < target_y:
            btn = "Down"
            next_x, next_y = cx, cy + 1
        else:
            btn = "Up"
            next_x, next_y = cx, cy - 1
            
        # Press button
        mgba.press_buttons([btn])
        time.sleep(0.4)
        
        # Verify position
        new_pos = mgba.get_coordinates()
        nx, ny = new_pos['x'], new_pos['y']
        
        if nx == cx and ny == cy:
            print(f"BUMPED/BLOCKED at ({cx}, {cy}) trying to move {btn}!")
            return False
            
        cx, cy = nx, ny
        print(f"Moved to ({cx}, {cy})")
        
    print("Arrived at target destination!")
    return True

# New waypoints from current position (23, 8)
waypoints = [
    (23, 9),   # Walk DOWN to Row 9 (bypass the NPC at 24, 8)
    (37, 9),   # Walk RIGHT to Column 37 along Row 9
    (37, 2),   # Walk UP to Row 2
    (22, 2),   # Walk LEFT to Column 22
    (22, 4),   # Walk DOWN to Row 4 (to clear the gatehouse building boundary)
    (18, 4),   # Walk LEFT to Column 18
    (18, 3)    # Walk UP to enter the Gatehouse
]

success = True
for wp in waypoints:
    success = move_to(wp[0], wp[1])
    if not success:
        print("Navigation aborted due to blockage.")
        break
