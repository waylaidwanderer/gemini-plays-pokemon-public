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
            print(f"Moved to {pos}")
            
            if pos == pos_before:
                print(f"BUMPED or BATTLE at {cur} going {direction} towards {wp}! Exiting to prevent drift.")
                return False
            attempts += 1
    return True

print("=== Starting Perfect Mansion Final Victory Route ===")
pos = mgba.get_coordinates()

# Phase 1: On 2F West (State B) standing at (2, 10), walk to stairs (7, 10) and warp DOWN
if pos['x'] == 2 and pos['y'] == 10:
    print("Already at switch stand (2, 10) in State B. Walking to 2F West stairs...")
    route_to_stairs = [
        (2, 11),
        (7, 11),
        (7, 10)
    ]
    if walk_exact_route(route_to_stairs):
        print("At 2F West stairs. Stepping DOWN to warp to 1F West...")
        mgba.press_buttons(["Down"])
        time.sleep(2.5)
        # Step DOWN once to clear stairs
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
        pos = mgba.get_coordinates()
        print("Arrived on 1F West in State B:", pos)

# Phase 2: On 1F West (State B), walk direct bypass route to 1F East stairs (18, 10)
pos = mgba.get_coordinates()
if (pos['x'] == 7 and pos['y'] == 11) or (pos['x'] == 7 and pos['y'] == 12):
    print("Currently on 1F West (State B). Walking bypass route to 1F East stairs...")
    route_1f = [
        (12, 11),
        (12, 6),
        (18, 6),
        (18, 10)
    ]
    if walk_exact_route(route_1f):
        print("At 1F East stairs. Stepping UP to warp to 2F East...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Arrived on 2F East:", pos)

# Phase 3: On 2F East (State B), walk to 3F East stairs at (15, 11) and warp UP
pos = mgba.get_coordinates()
if pos['x'] == 20 and pos['y'] == 16:
    route_2f_east = [
        (15, 16),
        (15, 11)
    ]
    if walk_exact_route(route_2f_east):
        print("At 2F East stairs. Stepping UP to warp to 3F East...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Arrived on 3F East:", pos)

# Phase 4: On 3F East (State B), walk to pit at (26, 6) and drop to 1F fenced room
pos = mgba.get_coordinates()
if pos['x'] == 16 and pos['y'] == 11:
    route_pit_3f = [
        (10, 11),
        (10, 3),
        (26, 3),
        (26, 6) # Stand next to pit
    ]
    if walk_exact_route(route_pit_3f):
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
        pos = mgba.get_coordinates()
        print("Landed on B1F East:", pos)

# Phase 5: On B1F East (State B), walk directly LEFT to Secret Key, retrieve, and DIG out
pos = mgba.get_coordinates()
if pos['x'] == 25 and pos['y'] == 5:
    route_key = [
        (26, 5),
        (26, 3),
        (21, 3),
        (21, 5),
        (1, 5)
    ]
    if walk_exact_route(route_key):
        print("SUCCESS! Reached Secret Key stand tile (1, 5)!")
        
        # Face UP and retrieve key
        print("Facing UP and retrieving key...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        # Interacting to retrieve Secret Key
        mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B"])
        time.sleep(1.5)
        print("SECRET KEY RETRIEVED! Now DIGging out...")
        mgba.press_buttons(["Start", "sleep 500"])
        time.sleep(1.0)
        # Select POKéMON
        mgba.press_buttons(["Down", "sleep 100", "A", "sleep 500"])
        time.sleep(1.0)
        # Select TRUFFLE (Down 5 times)
        mgba.press_buttons(["Down", "Down", "Down", "Down", "Down", "sleep 100", "A", "sleep 500"])
        time.sleep(1.0)
        # Select DIG (Option 1)
        mgba.press_buttons(["A", "sleep 500"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(3.0)
        print("ESCAPED! Final Cinnabar coordinates:", mgba.get_coordinates())
    else:
        print("Failed route to key.")
