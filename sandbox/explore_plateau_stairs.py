import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
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

print("--- EXPLORING SAFARI CENTER PLATEAU ---")
# 1. Walk to (20, 21) which is in front of the stairs
walk_to_waypoint(20, 22)
walk_to_waypoint(20, 21)

# 2. Walk UP to climb onto the plateau (20, 20)
mgba.press_buttons(["Up"])
time.sleep(0.5)
print("Position after climbing stairs:", mgba.get_coordinates())

# 3. Explore on the plateau: let's try walking UP as far as possible
for step in range(10):
    curr = mgba.get_coordinates()
    print(f"Step {step}: Position = {curr}")
    mgba.press_buttons(["Up"])
    time.sleep(0.42)
    # Escape battle if any
    new_curr = mgba.get_coordinates()
    if new_curr is None:
        escape_battle()
        time.sleep(0.5)

final_pos = mgba.get_coordinates()
print("Final position on plateau:", final_pos)
mgba.take_screenshot()
