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
                print(f"BUMPED or BATTLE at {cur} going {direction} towards {wp}! Exiting to prevent drift.")
                return False
            attempts += 1
    return True

print("=== Starting Perfect Mansion Run Phase 1 from (11, 12) ===")
pos = mgba.get_coordinates()

# 1. Walk from Cinnabar overworld to Mansion entrance and enter
if pos['x'] == 11 and pos['y'] == 12:
    cinnabar_route = [
        (17, 12),
        (17, 4),
        (6, 4),
        (6, 3)
    ]
    if walk_exact_route(cinnabar_route):
        print("At Mansion entrance. Stepping UP to enter...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Entered Mansion position:", pos)

# 2. Inside Mansion 1F West, go up stairs to 2F West
pos = mgba.get_coordinates()
if pos['x'] == 5 and pos['y'] == 27:
    print("Clear doormat warp by stepping UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Walking to 1F West stairs at (7, 10)...")
    route_1f = [(7, 10)]
    if walk_exact_route(route_1f):
        print("At 1F West stairs. Stepping UP to warp to 2F West...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Arrived on 2F West:", pos)

# 3. On 2F West (State A), walk left to switch at (2, 11) and toggle to State B
pos = mgba.get_coordinates()
if pos['x'] == 7 and pos['y'] == 10:
    print("Walking to 2F West switch stand tile at (2, 12)...")
    route_switch_2f = [
        (2, 10),
        (2, 12)
    ]
    if walk_exact_route(route_switch_2f):
        print("At 2F West switch stand tile (2, 12). Facing UP to toggle switch at (2, 11)...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        print("Toggling Mewtwo switch to State B...")
        mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B"])
        time.sleep(1.5)
        print("Switch toggled! Walk back to 2F West stairs at (7, 10)...")
        
        route_back_2f = [
            (2, 10),
            (7, 10)
        ]
        if walk_exact_route(route_back_2f):
            print("At 2F West stairs. Stepping DOWN to warp down to 1F West...")
            mgba.press_buttons(["Down"])
            time.sleep(2.5)
            
            # Step DOWN once to clear the stairs
            mgba.press_buttons(["Down"])
            time.sleep(0.5)
            
            print("PHASE 1 COMPLETE! Final position on 1F West in State B:", mgba.get_coordinates())
            mgba.take_screenshot()
