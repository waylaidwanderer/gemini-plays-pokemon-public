import mgba
import time

def handle_battle():
    print("Checking for battle...")
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.25)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.25)

def walk_exact_route(waypoints):
    for wp in waypoints:
        tx, ty = wp
        print(f"Walking to waypoint ({tx}, {ty})...")
        attempts = 0
        while attempts < 35:
            pos = mgba.get_coordinates()
            cur = (pos['x'], pos['y'])
            if cur == (tx, ty):
                break
                
            dx = tx - cur[0]
            dy = ty - cur[1]
            
            if dx < 0: direction = "Left"
            elif dx > 0: direction = "Right"
            elif dy < 0: direction = "Up"
            elif dy > 0: direction = "Down"
            else:
                break
                
            pos_before = pos
            mgba.press_buttons([direction])
            time.sleep(0.55)
            pos = mgba.get_coordinates()
            
            if pos == pos_before:
                print(f"BUMPED at {cur} going {direction} towards {wp}!")
                handle_battle()
                time.sleep(0.5)
                pos = mgba.get_coordinates()
                if pos == pos_before:
                    print("Physical obstruction or text. Retrying direction.")
                    mgba.press_buttons([direction])
                    time.sleep(0.55)
                    pos = mgba.get_coordinates()
                    if pos == pos_before:
                        print("Confirmed solid physical obstruction. Exiting.")
                        return False
            attempts += 1
    return True

print("=== Starting Phase 0: Cinnabar Island to 3F West ===")
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Cinnabar Island East Bypass Route
cinnabar_route = [
    (18, 12),  # Right to Column 18
    (18, 4),   # Up to Row 4
    (6, 4),    # Left to Column 6
    (6, 3)     # Up to enter Mansion
]

if walk_exact_route(cinnabar_route):
    print("At Mansion door. Stepping UP to enter...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)
    
    pos_1f = mgba.get_coordinates()
    print("Entered Mansion 1F West:", pos_1f)
    
    # Walk UP once to clear the doormat warp
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Walk to stairs at (7, 10)
    route_1f = [(7, 10)]
    if walk_exact_route(route_1f):
        print("At 1F West stairs. Stepping UP to 2F West...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        
        print("Arrived on 2F West:", mgba.get_coordinates())
        # Stepping UP to 3F West
        print("At 2F West stairs. Stepping UP to warp to 3F West...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        
        print("Arrived on 3F West:", mgba.get_coordinates())
        mgba.take_screenshot()
    else:
        print("Failed to reach stairs on 1F West.")
        mgba.take_screenshot()
else:
    print("Failed to reach Mansion entrance on Cinnabar Island.")
    mgba.take_screenshot()
