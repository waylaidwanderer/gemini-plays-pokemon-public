import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.2)
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

# Starting position is (22, 26) inside Area 2 (North)
print("--- PHASE 3 (CONTINUED): Area 2 (North) to Area 3 (West) ---")
waypoints = [
    (22, 22),  # Walk UP climbing stairs onto plateau
    (16, 22),  # Walk Left on plateau
    (16, 28),  # Walk DOWN descending stairs
    (12, 28),  # Walk Left
    (12, 30),  # Walk DOWN to bypass pond
    (8, 30),   # Walk Left to Column 8
    (8, 35)    # Walk DOWN through statues
]

for wp in waypoints:
    walk_to_waypoint(wp[0], wp[1])

# Step Down to transition to Area 3 (West)
print("Transitioning to Area 3 (West)...")
for _ in range(3):
    mgba.press_buttons(["Down"])
    time.sleep(0.5)

time.sleep(1.5)
final_pos = mgba.get_coordinates()
print("Position inside Area 3 (West):", final_pos)
screenshot_path = mgba.take_screenshot()
print(f"Screenshot: {screenshot_path}")
