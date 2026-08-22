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

print("=== Starting Perfect Mansion Run from (6, 4) ===")

# 1. Step UP to enter Mansion
pos = mgba.get_coordinates()
if pos['x'] == 6 and pos['y'] == 4:
    print("At Mansion door. Stepping UP to enter...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)
    
pos = mgba.get_coordinates()
print("Entered Mansion position:", pos)

# 2. Navigate 1F West to 3F West
if pos['x'] == 5 and pos['y'] == 27:
    print("Clear doormat warp by stepping UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Walking to 1F West stairs...")
    route_1f = [(7, 10)]
    if walk_exact_route(route_1f):
        print("At 1F West stairs. Stepping UP to warp to 2F West...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        
        print("Arrived on 2F West:", mgba.get_coordinates())
        print("Stepping UP to warp to 3F West...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        
        pos = mgba.get_coordinates()
        print("Arrived on 3F West:", pos)
        mgba.take_screenshot()

# 3. 3F West to 3F East Switch and toggle to State B
if pos['x'] == 7 and (pos['y'] == 10 or pos['y'] == 11):
    print("=== 3F West to 3F East Switch ===")
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
        pos = mgba.get_coordinates()
        print("State toggled to State B! Current position:", pos)
        mgba.take_screenshot()

# 4. 3F East (State B) to pit at (26, 6) and drop
if pos['x'] == 11 and pos['y'] == 11:
    print("=== 3F East Switch to Pit Drop ===")
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
        pos = mgba.get_coordinates()
        print("Landed on B1F East:", pos)
        mgba.take_screenshot()

# 5. B1F East to Secret Key, retrieve, and DIG out
if pos['x'] == 19 and (pos['y'] == 5 or pos['y'] == 6 or pos['y'] == 16):
    print("=== B1F East to Secret Key ===")
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
        mgba.press_buttons(["Down", "sleep 100", "A", "sleep 500"])
        time.sleep(1.0)
        mgba.press_buttons(["Down", "Down", "Down", "Down", "Down", "sleep 100", "A", "sleep 500"])
        time.sleep(1.0)
        mgba.press_buttons(["A", "sleep 500"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(3.0)
        print("ESCAPED! Final Cinnabar coordinates:", mgba.get_coordinates())
        mgba.take_screenshot()
