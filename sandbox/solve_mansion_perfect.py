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
                    # Try a small random action or continue
                    mgba.press_buttons([direction])
                    time.sleep(0.55)
                    pos = mgba.get_coordinates()
                    if pos == pos_before:
                        print("Confirmed solid physical obstruction. Exiting.")
                        return False
            attempts += 1
    return True

print("Starting perfect end-to-end Mansion run!")
pos = mgba.get_coordinates()
x, y = pos['x'], pos['y']
print(f"Current position: ({x}, {y})")

# 1. PHASE 0: Cinnabar overworld to 3F West
if x == 9 and y == 10:
    print("=== Phase 0: Navigating Cinnabar overworld to entrance ===")
    cinnabar_route = [
        (9, 11),  # Down to row 11
        (4, 11),  # Left to column 4 (bypass the cliff)
        (4, 4),   # Up to row 4
        (6, 4),   # Right to column 6
        (6, 3)    # Up to enter Mansion
    ]
    if walk_exact_route(cinnabar_route):
        print("At Mansion door. Stepping UP to enter...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Entered Mansion 1F West:", pos)
        
        # Clear the doormat warp
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        # Walk to stairs at (7, 10)
        route_1f = [(7, 10)]
        if walk_exact_route(route_1f):
            print("At 1F West stairs. Stepping UP to 2F West...")
            mgba.press_buttons(["Up"])
            time.sleep(2.5)
            print("Arrived on 2F West:", mgba.get_coordinates())
            
            # Step UP onto the stairs to warp to 3F West
            print("Stepping UP to 3F West...")
            mgba.press_buttons(["Up"])
            time.sleep(2.5)
            print("Arrived on 3F West:", mgba.get_coordinates())
            mgba.take_screenshot()
            
            # Re-fetch coordinates
            pos = mgba.get_coordinates()
            x, y = pos['x'], pos['y']

# 2. PHASE 1: 3F West (State A) to 3F East Switch and toggle to State B
if x == 7 and (y == 10 or y == 11):
    print("=== Phase 1: 3F West to 3F East Switch ===")
    route_3f_switch = [
        (7, 11),
        (10, 11),
        (10, 3),
        (26, 3),
        (26, 12),
        (12, 12),
        (12, 11),
        (11, 11) # Stand next to switch (12, 11)
    ]
    if walk_exact_route(route_3f_switch):
        print("At 3F East switch. Facing RIGHT and toggling to State B...")
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B"])
        time.sleep(1.5)
        print("State toggled to State B! Current position:", mgba.get_coordinates())
        mgba.take_screenshot()
        
        # Re-fetch coordinates
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']

# 3. PHASE 2: 3F East (State B) to pit at (26, 6) and drop to B1F East
if x == 11 and y == 11:
    print("=== Phase 2: 3F East Switch to Pit Drop ===")
    route_pit = [
        (11, 10),
        (12, 10),
        (12, 5),
        (21, 5),
        (21, 3),
        (26, 3),
        (26, 6) # Stand next to pit
    ]
    if walk_exact_route(route_pit):
        print("At pit edge. Stepping LEFT to drop...")
        mgba.press_buttons(["Left"])
        time.sleep(3.0)
        print("LANDED ON 1F FENCED ROOM! Current position:", mgba.get_coordinates())
        
        # Walk UP 5 times onto the stairs to warp to B1F East
        print("Walking UP to stairs to B1F East...")
        for _ in range(5):
            mgba.press_buttons(["Up"])
            time.sleep(0.5)
        time.sleep(2.0)
        print("Landed on B1F East:", mgba.get_coordinates())
        mgba.take_screenshot()
        
        # Re-fetch coordinates
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']

# 4. PHASE 3: B1F East to Secret Key, retrieve, and DIG out
if x == 19 and (y == 5 or y == 6 or y == 16):
    print("=== Phase 3: B1F East to Secret Key ===")
    route_key = [(19, 5), (1, 5)]
    if walk_exact_route(route_key):
        print("At Secret Key stand tile (1, 5). Facing UP and retrieving key...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B"])
        time.sleep(1.5)
        print("SECRET KEY RETRIEVED! Now DIGging out...")
        mgba.press_buttons(["Start", "sleep 500"])
        time.sleep(1.0)
        # Select POKéMON
        mgba.press_buttons(["Down", "sleep 100", "A", "sleep 500"])
        time.sleep(1.0)
        # Select TRUFFLE (Down 5 times, then A)
        mgba.press_buttons(["Down", "Down", "Down", "Down", "Down", "sleep 100", "A", "sleep 500"])
        time.sleep(1.0)
        # Select DIG (Option 1)
        mgba.press_buttons(["A", "sleep 500"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(3.0)
        print("ESCAPED! Final Cinnabar coordinates:", mgba.get_coordinates())
        mgba.take_screenshot()
