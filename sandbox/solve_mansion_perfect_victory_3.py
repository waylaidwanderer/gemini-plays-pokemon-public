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

print("=== Starting Perfect Mansion Run from (12, 11) ===")
pos = mgba.get_coordinates()

# 1. 3F East (State B) to pit at (26, 6) and drop
if pos['x'] == 12 and pos['y'] == 11:
    print("=== Phase 2: 3F East Switch to Pit Drop ===")
    route_pit = [
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

# 2. B1F East to Secret Key, retrieve, and DIG out
if pos['x'] == 19 and (pos['y'] == 5 or pos['y'] == 6 or pos['y'] == 16):
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
