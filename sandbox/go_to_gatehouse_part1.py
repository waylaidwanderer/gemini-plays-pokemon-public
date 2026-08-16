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
                print(f"Stuck at {curr} trying to reach ({target_x}, {target_y}). Retrying...")
                bridge.press_buttons(["A", "B"])
                time.sleep(0.5)
                stuck_count = 0
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
        time.sleep(0.44)

# 1. Exit Pokémon Center
print("Exiting Pokémon Center...")
walk_to_waypoint(3, 4)
walk_to_waypoint(3, 7)

# Step down to exit
print("Stepping DOWN to exit...")
bridge.press_buttons(["Down"])
time.sleep(1.0)

# Check coordinates in overworld
curr = bridge.get_coordinates()
print("Emerged in Fuchsia City at:", curr)

# 2. Walk Part 1 Waypoints
part1_waypoints = [
    (8, 28),
    (8, 32),
    (1, 32),
    (1, 18),
    (22, 18),
    (22, 14)
]

success = True
for idx, (wx, wy) in enumerate(part1_waypoints):
    print(f"Part 1 Waypoint {idx+1}/{len(part1_waypoints)}: ({wx}, {wy})")
    if not walk_to_waypoint(wx, wy):
        success = False
        break

if success:
    print("Part 1 Navigation Complete! Current Position:", bridge.get_coordinates())
else:
    print("Part 1 Navigation Failed! Current Position:", bridge.get_coordinates())
