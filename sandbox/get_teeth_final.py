import mgba
import time
import os

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
            if stuck_count > 4:
                print(f"Stuck at ({x}, {y}) trying to reach ({target_x}, {target_y})")
                # Fallback dialogue clearing just in case
                mgba.press_buttons(["A", "B", "A", "B"])
                time.sleep(0.5)
                stuck_count = 0
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

print("--- RETRIEVING GOLD TEETH VIA COLUMN 16 BYPASS ---")
# Current position is (21, 24).
waypoints = [
    (16, 24), # Walk LEFT to Column 16 on Row 24 (completely open, grass-free!)
    (16, 26), # Walk DOWN Column 16 to Row 26 (completely open, grass-free!)
    (19, 26)  # Walk RIGHT to Column 19 directly below the Gold Teeth (completely open!)
]

for wp in waypoints:
    walk_to_waypoint(wp[0], wp[1])

# Stand at (19, 26) facing UP (North)
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

# Press A to pick up the Gold Teeth
print("Pressing A to pick up the Gold Teeth!")
mgba.press_buttons(["A"])
time.sleep(1.5)

# Clear dialogue "ACE picked up the GOLD TEETH!"
print("Clearing dialogue...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.press_buttons(["A"])
time.sleep(1.0)

# Verify final position and items
final_pos = mgba.get_coordinates()
print("Final check of position:", final_pos)

# Obsolete files cleanup
obsolete_files = [
    "get_teeth_from_north.py",
    "get_teeth_from_east.py",
    "get_teeth_fast.py",
    "check_stairs.py",
    "go_to_gatehouse.py"
]
for f in obsolete_files:
    if os.path.exists(f):
        try:
            os.remove(f)
            print(f"Successfully deleted obsolete file: {f}")
        except Exception as e:
            print(f"Error deleting {f}: {e}")
