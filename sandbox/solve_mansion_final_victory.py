import mgba
import time

CURRENT_PHASE = 1  # Reset to Phase 1 since we are outside the Mansion!

def handle_battle():
    print("Coordinates did not change. Battle or obstacle detected! Attempting to flee...")
    # Clear dialogue
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.25)
    # Flee (Down, Right, A)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    # Clear dialogue
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.25)

def walk_to_waypoint(wx, wy):
    print(f"Navigating to waypoint ({wx}, {wy})...")
    attempts = 0
    while attempts < 60:
        pos = mgba.get_coordinates()
        if pos['x'] == wx and pos['y'] == wy:
            return True
            
        dx = wx - pos['x']
        dy = wy - pos['y']
        
        # Decide direction
        if dx < 0:
            direction = "Left"
        elif dx > 0:
            direction = "Right"
        elif dy < 0:
            direction = "Up"
        elif dy > 0:
            direction = "Down"
        else:
            break
            
        pos_before = pos
        mgba.press_buttons([direction])
        time.sleep(0.55)
        pos = mgba.get_coordinates()
        
        if pos == pos_before:
            print(f"BUMPED at {pos} going {direction} towards ({wx}, {wy})")
            handle_battle()
            time.sleep(0.5)
            pos = mgba.get_coordinates()
            if pos == pos_before:
                # Try alternative direction if possible
                if dx != 0 and dy != 0:
                    alt_dir = "Up" if dy < 0 else "Down"
                    print(f"Trying alternative vertical direction {alt_dir}...")
                    mgba.press_buttons([alt_dir])
                    time.sleep(0.55)
        attempts += 1
    return False

def walk_route(waypoints):
    for wp in waypoints:
        if not walk_to_waypoint(wp[0], wp[1]):
            print(f"Failed to reach waypoint {wp}")
            return False
    return True

pos = mgba.get_coordinates()
print(f"Starting solve_mansion_final_victory.py from {pos} in CURRENT_PHASE {CURRENT_PHASE}")

# --- PHASE 1: CINNABAR ISLAND TO MANSION ENTRANCE (STATE A) ---
if CURRENT_PHASE == 1:
    print("--- RUNNING PHASE 1: CINNABAR ISLAND TO MANSION ENTRANCE ---")
    cinnabar_waypoints = [
        (18, 12),
        (18, 5),
        (6, 5),
        (6, 4),
        (6, 3) # Mansion Entrance Door warp
    ]
    if walk_route(cinnabar_waypoints):
        print("Stepping UP to enter the Mansion...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Entered Mansion! Current position:", pos)
        CURRENT_PHASE = 2

# Update position
pos = mgba.get_coordinates()

# --- PHASE 2: 1F WEST TO 1F EAST (STATE A) ---
if pos['x'] == 5 and pos['y'] == 27 and CURRENT_PHASE == 2:
    print("--- RUNNING PHASE 2: 1F WEST TO 1F EAST (STATE A) ---")
    mansion_1f_west_waypoints = [
        (5, 5),
        (26, 5),
        (26, 6) # Stairs at (26, 6)
    ]
    if walk_route(mansion_1f_west_waypoints):
        print("Stepping UP onto stairs to warp UP to 2F East...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Arrived on 2F East! Current position:", pos)
        CURRENT_PHASE = 3

# Update position
pos = mgba.get_coordinates()

# --- PHASE 3: 2F EAST TO 2F WEST SWITCH (STATE A) ---
if pos['x'] == 26 and pos['y'] == 7 and CURRENT_PHASE == 3:
    print("--- RUNNING PHASE 3: 2F EAST TO 2F WEST SWITCH (STATE A) ---")
    mansion_2f_east_to_switch = [
        (26, 6),
        (12, 6),
        (12, 10),
        (11, 10), # open gate in State A
        (10, 10),
        (10, 11),
        (3, 11),
        (3, 12),
        (2, 12) # Switch stand tile
    ]
    if walk_route(mansion_2f_east_to_switch):
        print("At switch. Facing UP and toggling to State B...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
        time.sleep(1.5)
        print("Mansion global state is now State B!")
        CURRENT_PHASE = 4

# Update position
pos = mgba.get_coordinates()

# --- PHASE 4: 2F WEST SWITCH TO 1F WEST (STATE B) ---
if pos['x'] == 2 and pos['y'] == 12 and CURRENT_PHASE == 4:
    print("--- RUNNING PHASE 4: RETURNING TO 1F WEST FROM 2F WEST (STATE B) ---")
    mansion_2f_west_return = [
        (3, 12),
        (3, 11),
        (7, 11),
        (7, 10) # 2F West Stairs
    ]
    if walk_route(mansion_2f_west_return):
        print("Stepping UP onto stairs to warp DOWN to 1F West...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Arrived on 1F West! Current position:", pos)
        CURRENT_PHASE = 5

# Update position
pos = mgba.get_coordinates()

# --- PHASE 5: 1F WEST TO 1F EAST (STATE B) ---
if pos['x'] == 7 and (pos['y'] == 10 or pos['y'] == 11) and CURRENT_PHASE == 5:
    print("--- RUNNING PHASE 5: 1F WEST TO 1F EAST (STATE B) ---")
    mansion_1f_cross_waypoints = [
        (12, 11),
        (12, 5),
        (26, 5),
        (26, 6) # Stairs at (26, 6) on 1F East
    ]
    if walk_route(mansion_1f_cross_waypoints):
        print("Stepping UP onto stairs to warp UP to 2F East...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Arrived on 2F East! Current position:", pos)
        CURRENT_PHASE = 6

# Update position
pos = mgba.get_coordinates()

# --- PHASE 6: 2F EAST TO 3F EAST (STATE B) ---
if pos['x'] == 26 and pos['y'] == 7 and CURRENT_PHASE == 6:
    print("--- RUNNING PHASE 6: 2F EAST TO 3F EAST (STATE B) ---")
    mansion_2f_east_waypoints = [
        (26, 6),
        (15, 6),
        (15, 11) # Stairs to 3F East
    ]
    if walk_route(mansion_2f_east_waypoints):
        print("Stepping UP onto stairs to warp UP to 3F East...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Arrived on 3F East! Current position:", pos)
        CURRENT_PHASE = 7

# Update position
pos = mgba.get_coordinates()

# --- PHASE 7: 3F EAST TO BALCONY AND DROP (STATE B) ---
if pos['x'] == 16 and pos['y'] == 11 and CURRENT_PHASE == 7:
    print("--- RUNNING PHASE 7: 3F EAST TO BALCONY DROP (STATE B) ---")
    mansion_3f_east_waypoints = [
        (20, 11),
        (20, 18) # Balcony ledge
    ]
    if walk_route(mansion_3f_east_waypoints):
        print("At balcony edge. Stepping LEFT to drop to B1F East...")
        mgba.press_buttons(["Left"])
        time.sleep(3.0)
        pos = mgba.get_coordinates()
        print("Landed on B1F East! Current position:", pos)
        CURRENT_PHASE = 8

# Update position
pos = mgba.get_coordinates()

# --- PHASE 8: B1F EAST TO SECRET KEY ROOM (STATE B) ---
if pos['x'] == 19 and pos['y'] == 16 and CURRENT_PHASE == 8:
    print("--- RUNNING PHASE 8: WALKING TO SECRET KEY ---")
    mansion_b1f_waypoints = [
        (19, 5),
        (1, 5) # Standing below key
    ]
    if walk_route(mansion_b1f_waypoints):
        print("At Secret Key location. Facing UP and retrieving key...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 200"])
        time.sleep(1.0)
        print("SECRET KEY RETRIEVED!")
        CURRENT_PHASE = 9

# Update position
pos = mgba.get_coordinates()

# --- PHASE 9: ESCAPE USING DIG ---
if CURRENT_PHASE == 9:
    print("--- RUNNING PHASE 9: ESCAPE USING DIG ---")
    print("Opening menu to DIG out...")
    mgba.press_buttons(["Start"])
    time.sleep(1.0)
    mgba.press_buttons(["Down", "sleep 100", "A"])
    time.sleep(1.5)
    for _ in range(5):
        mgba.press_buttons(["Down"])
        time.sleep(0.2)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(3.0)
    print("Escaped Mansion! Final position:", mgba.get_coordinates())

print("Final position at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
