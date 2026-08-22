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

# --- MASTER PHASE 2: 2F East (State B) to 3F East via Row 3 and Column 18 ---
route_2f = [(26, 3), (18, 3), (18, 11), (15, 11)]
if walk_exact_route(route_2f):
    print("At 2F East stairs. Stepping UP to warp...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)
    pos_3f = mgba.get_coordinates()
    print("Arrived on 3F East:", pos_3f)
    
    # --- MASTER PHASE 3: 3F East (State B) to 3F Switch and toggle to State A ---
    if pos_3f['x'] == 16 and pos_3f['y'] == 11:
        route_3f = [(23, 11), (23, 3), (11, 3), (11, 11)]
        if walk_exact_route(route_3f):
            print("At 3F East switch at (11, 11). Facing RIGHT and toggling to State A...")
            mgba.press_buttons(["Right"])
            time.sleep(0.5)
            mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B"])
            time.sleep(1.5)
            pos_switch = mgba.get_coordinates()
            print("State toggled to State A! Current position:", pos_switch)
            
            # --- MASTER PHASE 4: 3F East (State A) to balcony drop at (24, 14) and drop ---
            route_drop = [(11, 12), (24, 12), (24, 14)]
            if walk_exact_route(route_drop):
                print("At balcony drop. Stepping LEFT to drop...")
                mgba.press_buttons(["Left"])
                time.sleep(3.0)
                print("LANDED ON B1F! Current position:", mgba.get_coordinates())
                mgba.take_screenshot()
else:
    print("FAILED route on 2F East.")
    mgba.take_screenshot()
