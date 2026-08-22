import mgba
import time

def walk_exact_route(waypoints):
    for wp in waypoints:
        tx, ty = wp
        print(f"Walking to waypoint ({tx}, {ty})...")
        attempts = 0
        while attempts < 25:
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
                print("BUMPED or BATTLE! Exiting.")
                return False
            attempts += 1
    return True

print("=== Starting test_stairs_direct.py ===")
pos = mgba.get_coordinates()

# 1. On 1F, walk back to 2F West stairs at (7, 10)
if pos['x'] == 21 and pos['y'] == 3:
    route_back = [
        (20, 3),
        (20, 4),
        (18, 4),
        (18, 6),
        (12, 6),
        (12, 11),
        (7, 11),
        (7, 10)
    ]
    if walk_exact_route(route_back):
        print("At 2F West stairs. Stepping UP to warp to 2F West...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Arrived on 2F West:", pos)

# 2. On 2F West (State B), walk to 2F East and reach 3F East stairs at (15, 11)
pos = mgba.get_coordinates()
if pos['x'] == 7 and pos['y'] == 10:
    print("Bypassing to 2F East...")
    route_2f = [
        (7, 3),
        (26, 3),
        (26, 16),
        (15, 16),
        (15, 11)
    ]
    if walk_exact_route(route_2f):
        print("At 3F East stairs on 2F East. Stepping UP to warp to 3F East...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Arrived on 3F East:", pos)
