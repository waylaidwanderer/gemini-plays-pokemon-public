import bridge
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.1)
    bridge.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.1)
    print("Escape sequence complete.")

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
                print(f"Unchanged position at {curr}. Checking if in battle...")
                escape_battle()
                stuck_count = 0
                time.sleep(0.5)
                after_coords = bridge.get_coordinates()
                if after_coords == curr:
                    print("Coordinates still unchanged. Retrying movement...")
                    bridge.press_buttons(["A", "B", "A", "B"])
                    time.sleep(0.5)
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

# Step 1: Walk back onto the plateau at (17, 6)
# Current: (10, 22)
print("Current position:", bridge.get_coordinates())
waypoints = [
    (10, 9),
    (17, 9),
    (17, 8),
    (17, 7), # climb ladder
    (17, 6)  # on plateau!
]

for wx, wy in waypoints:
    walk_to_waypoint(wx, wy)

# Step 2: Move to (18, 6)
walk_to_waypoint(18, 6)

# Step 3: Test rows on Column 19
# We will try Row 4, 5, 6, 7 on Column 19
for test_row in [4, 5, 6, 7]:
    print(f"\n--- Testing Row {test_row} on Column 19 ---")
    
    # Walk to Column 18, test_row
    if walk_to_waypoint(18, test_row):
        # Try to step RIGHT onto Column 19
        curr = bridge.get_coordinates()
        print(f"Standing at {curr}. Attempting to walk RIGHT onto Column 19...")
        bridge.press_buttons(["Right"])
        time.sleep(0.5)
        
        new_coords = bridge.get_coordinates()
        if new_coords == (19, test_row):
            print(f"SUCCESS! Row {test_row} Column 19 is WALKABLE!")
            # Walk back Left to continue testing
            bridge.press_buttons(["Left"])
            time.sleep(0.5)
        else:
            print(f"FAILED! Row {test_row} Column 19 is BLOCKED.")
            # If we accidentally entered a battle, escape it
            if new_coords == curr:
                # We bumped
                pass
            else:
                # We warped or moved unexpectedly
                print(f"Unexpected coordinate after RIGHT: {new_coords}")
