import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Escape sequence complete.")

def walk_to_waypoint(target_x, target_y):
    print(f"Navigating to waypoint ({target_x}, {target_y})...")
    stuck_count = 0
    last_coords = None
    
    while True:
        curr = mgba.get_coordinates()
        if curr is None:
            print("Coordinates are None. Waiting...")
            time.sleep(0.5)
            continue
            
        x, y = curr['x'], curr['y']
        if x == target_x and y == target_y:
            print(f"Reached waypoint ({target_x}, {target_y})")
            return True
            
        if (x, y) == last_coords:
            stuck_count += 1
            if stuck_count > 3:
                print(f"Stuck at ({x}, {y}) trying to reach ({target_x}, {target_y})")
                escape_battle()
                time.sleep(0.5)
                stuck_count = 0
                after = mgba.get_coordinates()
                if after['x'] == x and after['y'] == y:
                    print("Coordinates unchanged. Pressing A/B...")
                    mgba.press_buttons(["A", "B", "A", "B"])
                    time.sleep(0.5)
        else:
            stuck_count = 0
            last_coords = (x, y)
            
        # Choose direction to move
        if x < target_x:
            btn = "Right"
        elif x > target_x:
            btn = "Left"
        elif y < target_y:
            btn = "Down"
        elif y > target_y:
            btn = "Up"
            
        mgba.press_buttons([btn])
        time.sleep(0.42)

# Currently at (19, 24)
print("--- NAVIGATING TO WESTERN GROUND LEVEL ---")
waypoints = [
    (19, 18),
    (21, 18),
    (21, 17), # Climb East Stairs to plateau
    (6, 19),  # Walk Left across plateau to West Stairs
    (6, 20)   # Descend West Stairs to Western ground level
]

for wp in waypoints:
    walk_to_waypoint(wp[0], wp[1])

final_pos = mgba.get_coordinates()
print("Position on Western Ground Level:", final_pos)
screenshot_path = mgba.take_screenshot()
print(f"Screenshot: {screenshot_path}")
