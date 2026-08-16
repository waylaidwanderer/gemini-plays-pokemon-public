import mgba
import time

def press_and_wait(btn, delay=0.8):
    mgba.press_buttons([btn])
    time.sleep(delay)

print("--- CHUNK 1: PAYING, ENTERING, AND TRAVERSING CENTER ---")

# We are currently in the dialogue. Press A 10 times to clear dialogue and pay the fee.
print("Clearing dialogue and paying fee...")
for i in range(10):
    press_and_wait("A")

# Now we should be free to move at (3, 4) or (3, 3) in the Gatehouse.
# Let's walk UP into the door warp at (3, 0).
print("Walking UP to enter the Safari Zone Center...")
for _ in range(4):
    press_and_wait("Up", 0.5)

# Wait for map transition to load
time.sleep(1.5)

curr = mgba.get_coordinates()
print("Current Position after warp:", curr)

if curr and curr['x'] == 15 and curr['y'] == 25:
    print("SUCCESS! Entered Safari Zone Center.")
    # Now let's walk to the Area 1 (East) transition at (30, 10)
    # Waypoints inside Center:
    # 1. Walk UP to (15, 22)
    # 2. Walk RIGHT to (28, 22)
    # 3. Walk UP to (28, 10)
    # 4. Walk RIGHT to transition to Area 1 (East) at (30, 10)
    
    def walk_to_waypoint(target_x, target_y):
        print(f"Navigating to waypoint ({target_x}, {target_y})...")
        stuck_count = 0
        last_coords = None
        
        while True:
            curr = mgba.get_coordinates()
            x, y = curr['x'], curr['y']
            if x == target_x and y == target_y:
                print(f"Reached waypoint ({target_x}, {target_y})")
                return True
                
            if (x, y) == last_coords:
                stuck_count += 1
                if stuck_count > 4:
                    print("Stuck! Attempting to clear possible text boxes...")
                    mgba.press_buttons(["A", "B", "A", "B"])
                    time.sleep(0.5)
                    stuck_count = 0
            else:
                stuck_count = 0
                last_coords = (x, y)
                
            if x < target_x: btn = "Right"
            elif x > target_x: btn = "Left"
            elif y < target_y: btn = "Down"
            else: btn = "Up"
            
            mgba.press_buttons([btn])
            time.sleep(0.42)

    center_waypoints = [
        (15, 22),
        (28, 22),
        (28, 10),
        (30, 10)
    ]
    for wp in center_waypoints:
        walk_to_waypoint(wp[0], wp[1])
        
    print("Transitioning to Area 1 (East)...")
    mgba.press_buttons(["Right"])
    time.sleep(1.0)
    final_pos = mgba.get_coordinates()
    print("Final Position:", final_pos)
else:
    print("Failed to enter Safari Zone Center. Please verify current screen.")

mgba.take_screenshot()
