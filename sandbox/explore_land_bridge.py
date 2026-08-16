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
                print(f"Stuck at {curr} trying to reach ({target_x}, {target_y})")
                return False
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

# Current: (13, 9)
print("Current position:", bridge.get_coordinates())

# Waypoints to climb onto the plateau at (17, 6)
waypoints = [
    (17, 9),
    (17, 8),
    (17, 7), # climb ladder
    (17, 6)  # on plateau!
]

success = True
for wx, wy in waypoints:
    if not walk_to_waypoint(wx, wy):
        success = False
        break

if success:
    # Test Row 4, 5, 6, 7 on Column 19
    for test_row in [4, 5, 6, 7]:
        print(f"\n--- Testing Row {test_row} on Column 19 ---")
        
        # Walk to Column 18, test_row
        if walk_to_waypoint(18, test_row):
            curr = bridge.get_coordinates()
            print(f"Standing at {curr}. Attempting to walk RIGHT onto Column 19...")
            bridge.press_buttons(["Right"])
            time.sleep(0.5)
            
            new_coords = bridge.get_coordinates()
            if new_coords == (19, test_row):
                print(f"SUCCESS! Row {test_row} Column 19 is WALKABLE!")
                bridge.press_buttons(["Left"])
                time.sleep(0.5)
            else:
                print(f"FAILED! Row {test_row} Column 19 is BLOCKED.")
else:
    print("Failed to reach plateau. Current position:", bridge.get_coordinates())
