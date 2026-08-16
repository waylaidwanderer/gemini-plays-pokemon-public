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
                escape_battle()
                stuck_count = 0
                time.sleep(0.5)
                after_coords = mgba.get_coordinates()
                if after_coords['x'] == x and after_coords['y'] == y:
                    print("Coordinates still unchanged. Clearing text boxes...")
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

print("--- TRYING WEST STAIRS FROM CURRENT POSITION ---")
# Current position: (28, 11)
# Walk LEFT to Column 20, then DOWN to Row 15, then RIGHT onto West Stairs
try:
    walk_to_waypoint(20, 11)
    walk_to_waypoint(20, 15)
    # The West Stairs of Plateau are at (20, 15). Wait, if they face west, we stand at (19, 15) and walk Right?
    # Let's try to walk to (19, 15) then step Right to climb
    walk_to_waypoint(19, 15)
    print("At (19, 15), attempting to climb RIGHT onto West Stairs...")
    walk_to_waypoint(20, 15)
    print("Successfully climbed West Stairs!")
except Exception as e:
    print("Error:", e)

mgba.take_screenshot()
