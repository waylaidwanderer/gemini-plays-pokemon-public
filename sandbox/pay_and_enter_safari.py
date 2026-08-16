import mgba
import time

def press_and_wait(btn, delay=0.5):
    mgba.press_buttons([btn])
    time.sleep(delay)

print("Clearing final dialogue to trigger warp...")
for i in range(5):
    press_and_wait("A", 0.5)
    pos = mgba.get_coordinates()
    print(f"Press {i+1}: Position = {pos}")
    if pos['x'] == 15 and pos['y'] == 25:
        print("WARP SUCCESSFUL!")
        break

pos = mgba.get_coordinates()
if pos['x'] == 15 and pos['y'] == 25:
    # We are in Safari Zone Center!
    # Let's execute the Phase 1 route to Area 1 (East)
    print("Executing Phase 1: Center to Area 1 (East)...")
    waypoints = [
        (15, 22),
        (28, 22),
        (28, 10),
        (30, 10)
    ]
    
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
                    print("Stuck! Attempting to escape battle...")
                    mgba.press_buttons(["Down", "Right", "A"])
                    time.sleep(1.5)
                    mgba.press_buttons(["B", "B", "B"])
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

    for wp in waypoints:
        walk_to_waypoint(wp[0], wp[1])
        
    print("Phase 1 complete! Position:", mgba.get_coordinates())
else:
    print("Warp failed. Current position:", pos)

mgba.take_screenshot()
