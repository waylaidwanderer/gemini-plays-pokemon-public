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
                print(f"BUMPED or BATTLE at {cur} going {direction} towards {wp}! Exiting to prevent drift.")
                return False
            attempts += 1
    return True

print("=== Starting Perfect Secret Key Retrieval from (21, 6) ===")
pos = mgba.get_coordinates()

if pos['x'] == 21 and pos['y'] == 6:
    # Route: Up to Row 3, Right to Column 25, Down to Row 9, Left to Column 18 (Switch)
    route_switch = [
        (21, 3),
        (25, 3),
        (25, 9),
        (18, 9)
    ]
    if walk_exact_route(route_switch):
        print("At (18, 9). Facing LEFT to look at the statue at (17, 9)...")
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        
        print("Toggling B1F switch to State B...")
        mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B"])
        time.sleep(1.5)
        print("State toggled to State B! Re-fetching coordinates...")
        pos = mgba.get_coordinates()
        print("Position after switch toggle:", pos)
        mgba.take_screenshot()

# If we are standing at (18, 9) or (17, 9) after toggle, walk to Secret Key at (1, 5)
pos = mgba.get_coordinates()
if (pos['x'] == 18 or pos['x'] == 17) and pos['y'] == 9:
    print("=== Phase 2: Walk from Switch to Secret Key ===")
    route_key = [
        (18, 9), # ensure we are on Column 18
        (18, 5), # Up to Row 5
        (1, 5)   # Left to Northwest Room
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
        mgba.take_screenshot()
    else:
        print("Failed route to key.")
        mgba.take_screenshot()
