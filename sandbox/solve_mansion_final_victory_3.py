import mgba
import time

# Battle handler
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
                    print("Physical obstruction. Exiting to prevent loop.")
                    return False
            attempts += 1
    return True

# Detect current state and position
pos = mgba.get_coordinates()
x, y = pos['x'], pos['y']
print(f"Detected starting position: ({x}, {y})")

# --- PHASE 2b (from 1F East-Central / Column 15): Walk to stairs at (18, 10) via Column 12 highway ---
if x == 15 and y == 6:
    print("=== EXECUTING PHASE 2B: 1F COLUMN 15 TO 2F EAST (WEST-CENTRAL) ===")
    route = [(12, 6), (12, 11), (18, 11), (18, 10)]
    if walk_exact_route(route):
        print("At 1F East stairs. Stepping UP to warp...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        print("Arrived on 2F East (West-Central):", mgba.get_coordinates())

# --- PHASE 2a (from 1F West): Walk directly to (18, 10) ---
elif x == 7 and (y == 10 or y == 11):
    print("=== EXECUTING PHASE 2A: 1F WEST TO 2F EAST (WEST-CENTRAL) ===")
    route = [(12, 11), (18, 11), (18, 10)]
    if walk_exact_route(route):
        print("At 1F East stairs. Stepping UP to warp...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        print("Arrived on 2F East (West-Central):", mgba.get_coordinates())

# --- PHASE 3: Currently on 2F East (West-Central). Walk to 3F East stairs at (15, 11) ---
elif 12 <= x <= 21 and y >= 9 and not (x == 16 and y == 11):
    print("=== EXECUTING PHASE 3: 2F EAST TO 3F EAST ===")
    route = [(15, 16), (15, 11)]
    if walk_exact_route(route):
        print("At 2F East stairs. Stepping UP to warp...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        print("Arrived on 3F East:", mgba.get_coordinates())

# --- PHASE 4: Currently on 3F East. Walk to Balcony and drop ---
elif x == 16 and y == 11:
    print("=== EXECUTING PHASE 4: 3F EAST TO BALCONY AND DROP ===")
    route = [(20, 11), (20, 18)]
    if walk_exact_route(route):
        print("At balcony ledge. Stepping LEFT to drop...")
        mgba.press_buttons(["Left"])
        time.sleep(3.0)
        print("Landed on B1F East:", mgba.get_coordinates())

# --- PHASE 5: Landed on B1F East. Walk to Secret Key, retrieve it, and DIG out! ---
elif x == 19 and y == 16:
    print("=== EXECUTING PHASE 5: B1F EAST TO SECRET KEY ===")
    route = [(19, 5), (1, 5)]
    if walk_exact_route(route):
        print("At Secret Key stand tile (1, 5). Facing UP and retrieving key...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B"])
        time.sleep(1.5)
        print("SECRET KEY RETRIEVED! Now DIGging out...")
        mgba.press_buttons(["Start", "sleep 500"])
        time.sleep(1.0)
        # Select POKéMON (option 2)
        mgba.press_buttons(["Down", "sleep 100", "A", "sleep 500"])
        time.sleep(1.0)
        # Select TRUFFLE (the 6th Pokémon, so Down 5 times, then A)
        mgba.press_buttons(["Down", "Down", "Down", "Down", "Down", "sleep 100", "A", "sleep 500"])
        time.sleep(1.0)
        # Select DIG (option 1, or press Down if DIG is not first, but TRUFFLE's option 1 is DIG!)
        mgba.press_buttons(["A", "sleep 500"])
        time.sleep(1.0)
        # Confirm
        mgba.press_buttons(["A"])
        time.sleep(3.0)
        print("ESCAPED! Current position:", mgba.get_coordinates())

else:
    print("Starting position does not match any current phase triggers. Please check location!")

mgba.take_screenshot()
