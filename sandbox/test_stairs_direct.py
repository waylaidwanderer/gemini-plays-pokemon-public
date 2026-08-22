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

# Direct test route: from (18, 6) to (15, 11) via Row 3 and Column 26
route = [(15, 6), (15, 3), (26, 3), (26, 7), (26, 11), (15, 11)]
if walk_exact_route(route):
    print("SUCCESS! Reached stairs at (15, 11) directly from 2F East!")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)
    print("Coordinates on 3F East:", mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("FAILED route.")
    mgba.take_screenshot()
