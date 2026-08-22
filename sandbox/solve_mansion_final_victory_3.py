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

# --- PHASE 0: Cinnabar Island to Mansion 3F West stairs ---
# If we are on Cinnabar Island overworld
if y >= 11 and x >= 4 and x <= 18:
    print("=== EXECUTING MASTER PHASE 0: CINNABAR ISLAND TO 3F WEST STAIRS ===")
    
    # Walk the safety bypass route to enter the Mansion safely at (6, 3)
    cinnabar_route = [
        (4, 12),
        (4, 4),
        (6, 4),
        (6, 3) # Mansion Entrance Door warp
    ]
    if walk_exact_route(cinnabar_route):
        print("Stepping UP to enter the Mansion...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos_1f = mgba.get_coordinates()
        print("Entered Mansion 1F West:", pos_1f)
        
        # Walk immediately UP to clear the exit warp
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        # On 1F West, walk to the stairs at (7, 10) and warp UP to 2F West
        route_1f = [(7, 10)]
        if walk_exact_route(route_1f):
            print("At 1F West stairs. Stepping UP to warp...")
            mgba.press_buttons(["Up"])
            time.sleep(2.5)
            pos_2f = mgba.get_coordinates()
            print("Arrived on 2F West:", pos_2f)
            
            # On 2F West, step UP onto the stairs at (7, 10) to warp UP to 3F West
            print("At 2F West stairs. Stepping UP to warp to 3F West...")
            mgba.press_buttons(["Up"])
            time.sleep(2.5)
            pos_3f = mgba.get_coordinates()
            print("Arrived on 3F West:", pos_3f)
            mgba.take_screenshot()

else:
    print("Not starting on Cinnabar Island overworld. Running remaining phases...")

# --- MASTER PHASE 1: 3F West (State A) to 3F East Switch and toggle to State B ---
if x == 7 and (y == 10 or y == 11):
    print("=== EXECUTING MASTER PHASE 1: 3F WEST TO 3F EAST SWITCH ===")
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
        print("At 3F East switch at (11, 11). Facing RIGHT and toggling to State B...")
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B"])
        time.sleep(1.5)
        print("State toggled to State B! Current position:", mgba.get_coordinates())
        mgba.take_screenshot()

# --- MASTER PHASE 2: 3F East (State B) to pit at (26, 6) and drop ---
elif x == 11 and y == 11:
    print("=== EXECUTING MASTER PHASE 2: 3F EAST SWITCH TO PIT DROP ===")
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
        print("Landed on B1F East:", mgba.get_coordinates())
        mgba.take_screenshot()

# --- MASTER PHASE 3: Landed on B1F East. Walk to Secret Key, retrieve, and DIG out ---
elif x == 19 and (y == 5 or y == 6 or y == 16):
    print("=== EXECUTING MASTER PHASE 3: B1F EAST TO SECRET KEY ===")
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
