import mgba
import time

# Robust battle handler
def handle_battle():
    print("Checking for battle...")
    # Press B to clear any initial text
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.25)
    # Attempt to flee (Down, Right, A)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    # Clear dialogue
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.25)

# Robust path follower with zero learning bumps (pre-defined safe paths)
def walk_exact_route(waypoints):
    for wp in waypoints:
        tx, ty = wp
        print(f"Walking to waypoint ({tx}, {ty})...")
        attempts = 0
        while attempts < 40:
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
                    print("Still stuck. Exiting to avoid soft-lock/button waste.")
                    return False
            attempts += 1
    return True

# Detect current state and position
pos = mgba.get_coordinates()
x, y = pos['x'], pos['y']
print(f"Detected starting position: ({x}, {y})")

# --- PHASE 1: We are on 1F West (State A). Go to 2F West. ---
# Current location is around (11, 7) or (11, 12).
if x > 10 and y < 15 and x < 15: # 1F West center
    print("=== EXECUTING PHASE 1: 1F WEST TO 2F WEST ===")
    route = [(12, 7), (12, 11), (7, 11), (7, 10)]
    if walk_exact_route(route):
        print("At 1F West stairs. Stepping UP to warp...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        print("Arrived on 2F West:", mgba.get_coordinates())

# --- PHASE 2: We are on 2F West (State A). Go to Switch and toggle to State B. ---
elif x == 7 and (y == 10 or y == 11):
    print("=== EXECUTING PHASE 2: 2F WEST TO SWITCH ===")
    route = [(7, 11), (2, 11), (2, 12)]
    if walk_exact_route(route):
        print("At switch (2, 12). Facing UP and toggling to State B...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
        time.sleep(1.5)
        print("Mansion state is now State B!", mgba.get_coordinates())

# --- PHASE 3: We are at Switch on 2F West (State B). Return to 1F West. ---
elif x == 2 and y == 12:
    print("=== EXECUTING PHASE 3: 2F WEST RETURNING TO 1F WEST ===")
    route = [(2, 11), (7, 11), (7, 10)]
    if walk_exact_route(route):
        print("At 2F West stairs. Stepping UP to warp...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        print("Arrived on 1F West:", mgba.get_coordinates())

# --- PHASE 4: We are on 1F West (State B) after returning. Cross to 1F East and go to 2F East. ---
# Wait, if we just landed on 1F West, we are at (7, 11) or (7, 10).
# Let's make sure we walk safely to 1F East stairs at (26, 6) via Row 3.
elif x == 7 and y == 11:
    print("=== EXECUTING PHASE 4: 1F WEST TO 2F EAST ===")
    route = [(12, 11), (12, 3), (26, 3), (26, 6)]
    if walk_exact_route(route):
        print("At 1F East stairs. Stepping UP to warp...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        print("Arrived on 2F East:", mgba.get_coordinates())

# --- PHASE 5: We are on 2F East (State B). Go to 3F East via Row 3 and Column 15. ---
elif x == 26 and y == 7:
    print("=== EXECUTING PHASE 5: 2F EAST TO 3F EAST ===")
    route = [(26, 3), (15, 3), (15, 11)]
    if walk_exact_route(route):
        print("At 2F East stairs. Stepping UP to warp...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        print("Arrived on 3F East:", mgba.get_coordinates())

# --- PHASE 6: We are on 3F East (State B). Go to Balcony and drop. ---
elif x == 16 and y == 11:
    print("=== EXECUTING PHASE 6: 3F EAST BALCONY DROP ===")
    route = [(20, 11), (20, 18)]
    if walk_exact_route(route):
        print("At balcony ledge. Stepping LEFT to drop...")
        mgba.press_buttons(["Left"])
        time.sleep(3.0)
        print("Landed on B1F East:", mgba.get_coordinates())

# --- PHASE 7: We land on B1F East (State B). Walk directly to Secret Key and retrieve it. ---
elif x == 19 and y == 16:
    print("=== EXECUTING PHASE 7: B1F EAST TO SECRET KEY ===")
    route = [(19, 5), (1, 5)]
    if walk_exact_route(route):
        print("At Secret Key location (1, 5). Facing UP and retrieving key...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B"])
        time.sleep(1.5)
        print("SECRET KEY RETRIEVED SUCCESSFULLY!", mgba.get_coordinates())

else:
    print("Starting position does not match any current phase triggers. Please check location!")

mgba.take_screenshot()
