import mgba
import time

def handle_battle():
    print("Checking for battle...")
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    # Escape sequence
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    for _ in range(8):
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
                    print("Still stuck. Trying B press...")
                    mgba.press_buttons(["B"])
                    time.sleep(0.2)
            attempts += 1
        if attempts >= 35:
            print(f"Failed to reach waypoint ({tx}, {ty}).")
            return False
    return True

print("=== STARTING COMPLETE MANSION KEY ROUTE (FROM CINNABAR OVERWORLD) ===")
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Phase 0: Cinnabar overworld to Mansion entrance
if pos['x'] == 5 and pos['y'] == 11:
    print("=== PHASE 0: Walking to Pokémon Mansion entrance ===")
    route_cinnabar = [
        (5, 12),
        (11, 12),
        (11, 4),
        (6, 4)
    ]
    if walk_exact_route(route_cinnabar):
        print("At Mansion door. Stepping UP to enter...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Entered Mansion 1F:", pos)

# Phase 0.5: Walk from Mansion 1F West entrance to stairs
pos = mgba.get_coordinates()
if pos['x'] == 5 and pos['y'] == 27:
    print("=== PHASE 0.5: Walking to 1F West stairs ===")
    route_1f = [
        (5, 11),
        (7, 11),
        (7, 10)
    ]
    if walk_exact_route(route_1f):
        print("At 1F West stairs. Stepping UP to go to 2F West...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Landed on 2F West:", pos)

# Phase 0.75: On 2F West (State A), walk to switch, toggle to State B, return to stairs
pos = mgba.get_coordinates()
if pos['x'] == 7 and pos['y'] == 10:
    # Let's verify we are in State A by checking if we need to toggle
    print("=== PHASE 0.75: Walking to 2F West Mewtwo statue ===")
    route_switch = [
        (7, 11),
        (3, 11)
    ]
    if walk_exact_route(route_switch):
        print("At Mewtwo switch on 2F West. Toggling to State B...")
        mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B", "sleep 600"])
        time.sleep(2.0)
        print("Switch toggled to State B. Returning to stairs...")
        route_back = [
            (7, 11),
            (7, 10)
        ]
        if walk_exact_route(route_back):
            print("Back at 2F West stairs in State B.")
            time.sleep(0.5)

# Phase 1: On 2F West (State B), walk to 2F East stairs and warp UP to 3F East
pos = mgba.get_coordinates()
if pos['x'] == 7 and pos['y'] == 10:
    print("=== PHASE 1: Crossing 2F West to 2F East ===")
    route_2f_cross = [
        (3, 10),
        (3, 3),
        (26, 3),
        (26, 11),
        (15, 11)
    ]
    if walk_exact_route(route_2f_cross):
        print("At 2F East stairs. Stepping UP to warp...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Landed on 3F East:", pos)

# Phase 2: On 3F East (State B), walk to pit and drop
pos = mgba.get_coordinates()
if pos['x'] == 16 and pos['y'] == 11:
    print("=== PHASE 2: Crossing 3F East to Pit ===")
    route_pit_3f = [
        (10, 11),
        (10, 3),
        (26, 3),
        (26, 6)
    ]
    if walk_exact_route(route_pit_3f):
        print("At pit edge. Stepping LEFT to drop...")
        mgba.press_buttons(["Left"])
        time.sleep(3.0)
        pos = mgba.get_coordinates()
        print("LANDED ON 1F FENCED ROOM! Current position:", pos)

# Phase 3: On 1F Fenced Room, walk UP to warp down to B1F East
pos = mgba.get_coordinates()
if pos['x'] == 25 and pos['y'] == 6:
    print("=== PHASE 3: Traversing 1F Fenced Room to B1F East ===")
    for i in range(1, 7):
        print(f"Stepping UP {i}...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Landed on B1F East:", pos)

# Phase 4: B1F East to Secret Key and DIG out
pos = mgba.get_coordinates()
if pos['x'] == 25 and pos['y'] == 5:
    print("=== PHASE 4: Walking B1F East to Secret Key ===")
    route_key = [
        (26, 5),
        (26, 3),
        (21, 3),
        (21, 5),
        (1, 5)
    ]
    if walk_exact_route(route_key):
        print("At Secret Key tile! Facing UP...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        print("Picking up SECRET KEY...")
        mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B"])
        time.sleep(1.5)
        print("SECRET KEY PICKED UP! Using DIG to escape...")
        mgba.press_buttons(["Start", "sleep 500"])
        time.sleep(1.0)
        # Select POKéMON
        mgba.press_buttons(["Down", "sleep 100", "A", "sleep 500"])
        time.sleep(1.0)
        # Select TRUFFLE (Paras is 6th in party, so press Down 5 times from index 0)
        mgba.press_buttons(["Down", "Down", "Down", "Down", "Down", "sleep 100", "A", "sleep 500"])
        time.sleep(1.0)
        # Select DIG (Option 1)
        mgba.press_buttons(["A", "sleep 500"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(3.0)
        print("Mansion Final Escape Successful! Position:", mgba.get_coordinates())
