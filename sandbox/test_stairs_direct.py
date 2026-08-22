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
                    print("Physical obstruction. Exiting.")
                    return False
            attempts += 1
    return True

print("Current coordinates:", mgba.get_coordinates())

# Direct walk to (26, 6) stairs and warp to 2F East (26, 7)
route_1f = [(26, 6)]
if walk_exact_route(route_1f):
    print("At 1F East stairs (26, 6). Stepping UP to warp...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)
    pos_2f = mgba.get_coordinates()
    print("Arrived on 2F East:", pos_2f)
    
    # Try the direct walk to (15, 11) on 2F East
    route_2f = [(26, 11), (15, 11)]
    if walk_exact_route(route_2f):
        print("At 2F East stairs. Stepping UP to warp...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        print("Arrived on 3F East:", mgba.get_coordinates())
        mgba.take_screenshot()
    else:
        print("FAILED 2F East direct walk.")
        mgba.take_screenshot()
else:
    print("FAILED 1F East walk.")
    mgba.take_screenshot()
