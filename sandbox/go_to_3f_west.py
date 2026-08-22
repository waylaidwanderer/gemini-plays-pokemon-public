import mgba
import time

def walk_exact_route(waypoints):
    for wp in waypoints:
        tx, ty = wp
        print(f"Walking to waypoint ({tx}, {ty})...")
        attempts = 0
        while attempts < 30:
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
                return False
            attempts += 1
    return True

print("Current coordinates:", mgba.get_coordinates())

# Eastern bypass route on Cinnabar Island to enter Mansion safely at (6, 3)
route_cinnabar = [(18, 10), (18, 5), (6, 5), (6, 3)]
if walk_exact_route(route_cinnabar):
    print("At Mansion entrance. Stepping UP to enter...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)
    
    pos_1f = mgba.get_coordinates()
    print("Entered Mansion 1F West:", pos_1f)
    # Clear the warp doormat
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # On 1F West, walk safely to 1F stairs at (7, 10)
    route_1f = [(5, 11), (7, 11), (7, 10)]
    if walk_exact_route(route_1f):
        print("At 1F stairs. Stepping UP to warp to 2F West...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos_2f = mgba.get_coordinates()
        print("Arrived on 2F West:", pos_2f)
        
        # On 2F West, step UP onto the stairs at (7, 10) to warp to 3F West
        print("At 2F stairs. Stepping UP to warp to 3F West...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos_3f = mgba.get_coordinates()
        print("Arrived on 3F West:", pos_3f)
        mgba.take_screenshot()
else:
    print("Failed Cinnabar route.")
    mgba.take_screenshot()
