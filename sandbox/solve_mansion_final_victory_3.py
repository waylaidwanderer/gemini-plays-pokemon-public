import mgba
import time

def handle_battle():
    print("Checking for battle...")
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    for _ in range(6):
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

print("=== STARTING THE DIRECT 2F EAST KEY ROUTE ===")
pos = mgba.get_coordinates()
print("Starting position:", pos)

if pos['x'] == 21 and pos['y'] == 3:
    print("=== PHASE 1: Navigating 2F East (State A) ===")
    route_2f_switch = [
        (26, 3),
        (26, 11),
        (14, 11)
    ]
    if walk_exact_route(route_2f_switch):
        print("Successfully reached 2F East Switch stand!")
        print("Facing LEFT and toggling switch to State B...")
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B"])
        time.sleep(1.5)
        print("Toggled! Walking to 2F East stairs...")
        if walk_exact_route([(15, 11)]):
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
        # Select TRUFFLE (Down 5 times)
        mgba.press_buttons(["Down", "Down", "Down", "Down", "Down", "sleep 100", "A", "sleep 500"])
        time.sleep(1.0)
        # Select DIG (Option 1)
        mgba.press_buttons(["A", "sleep 500"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(3.0)
        print("Mansion Final Escape Successful! Position:", mgba.get_coordinates())
