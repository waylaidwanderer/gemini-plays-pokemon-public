import mgba
import time

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

# Let's read current coordinates and determine which part of the route we are on!
pos = mgba.get_coordinates()
print("Starting solve_mansion_final_victory.py from:", pos)

# 1. If we are on Cinnabar Island
if pos['x'] >= 0 and pos['x'] <= 20 and pos['y'] >= 0 and pos['y'] <= 20:
    print("--- PHASE 1: CINNABAR ISLAND TO MANSION ENTRANCE ---")
    if pos['x'] == 10 and pos['y'] == 7:
        cinnabar_waypoints = [
            (10, 4),
            (6, 4),
            (6, 3) # Mansion Entrance Door warp
        ]
    else:
        cinnabar_waypoints = [
            (18, 13),
            (18, 4),
            (6, 4),
            (6, 3) # Mansion Entrance Door warp
        ]
    if walk_route(cinnabar_waypoints):
        print("Stepping UP to enter the Mansion...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Entered Mansion! Current position:", pos)

# Update position
pos = mgba.get_coordinates()

# 2. If we are on Mansion 1F West
# Mansion 1F West entrance landing is at (5, 27)
if pos['x'] == 5 and pos['y'] == 27:
    print("--- PHASE 2: MANSION 1F WEST TO 2F WEST ---")
    mansion_1f_west_waypoints = [
        (5, 10),
        (7, 10) # 2F West Stairs
    ]
    if walk_route(mansion_1f_west_waypoints):
        print("Stepping UP onto stairs to warp UP to 2F West...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Arrived on 2F West! Current position:", pos)

# Update position
pos = mgba.get_coordinates()

# 3. If we are on Mansion 2F West and switch needs to be toggled to State B
# 2F West stairs landing is at (7, 10)
if pos['x'] == 7 and pos['y'] == 10:
    print("--- PHASE 3: TOGGLING 2F WEST SWITCH TO STATE B ---")
    mansion_2f_west_waypoints = [
        (7, 11),
        (2, 11),
        (2, 12) # Stand here facing UP to toggle
    ]
    if walk_route(mansion_2f_west_waypoints):
        print("At switch position. Facing UP and toggling to State B...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
        time.sleep(1.5)
        print("Mansion global state is now State B!")

# Update position
pos = mgba.get_coordinates()

# 4. If we are at the 2F West switch, go back down to 1F West
if pos['x'] == 2 and pos['y'] == 12:
    print("--- PHASE 4: RETURNING TO 1F WEST FROM 2F WEST ---")
    mansion_2f_west_return = [
        (2, 11),
        (7, 11),
        (7, 10) # 2F West Stairs
    ]
    if walk_route(mansion_2f_west_return):
        print("Stepping UP onto stairs to warp DOWN to 1F West...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Arrived on 1F West! Current position:", pos)

# Update position
pos = mgba.get_coordinates()

# 5. If we are on 1F West, cross to 1F East and go up the west-central stairs to 2F East
if pos['x'] == 7 and pos['y'] == 10:
    print("--- PHASE 5: CROSSING 1F TO WEST-CENTRAL STAIRS ---")
    mansion_1f_cross_waypoints = [
        (7, 11),
        (15, 11),
        (15, 8),   # Open gate in State B
        (18, 8),
        (18, 10)   # Stairs at (18, 10) on 1F East
    ]
    if walk_route(mansion_1f_cross_waypoints):
        print("Stepping UP onto stairs to warp UP to 2F East (landing at 20, 16)...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Arrived on 2F East! Current position:", pos)

# Update position
pos = mgba.get_coordinates()

# 6. If we are on 2F East, walk to stairs to 3F East
if pos['x'] == 20 and pos['y'] == 16:
    print("--- PHASE 6: WALKING TO 3F EAST STAIRS ---")
    mansion_2f_east_waypoints = [
        (20, 11),
        (15, 11) # Stairs to 3F East
    ]
    if walk_route(mansion_2f_east_waypoints):
        print("Stepping UP onto stairs to warp UP to 3F East (landing at 16, 11)...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Arrived on 3F East! Current position:", pos)

# Update position
pos = mgba.get_coordinates()

# 7. If we are on 3F East, walk to balcony and drop
if pos['x'] == 16 and pos['y'] == 11:
    print("--- PHASE 7: BALCONY DROP ---")
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

# Update position
pos = mgba.get_coordinates()

# 8. If we are on B1F East, walk directly to Secret Key room
if pos['x'] == 19 and pos['y'] == 16:
    print("--- PHASE 8: WALKING TO SECRET KEY ---")
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
        
        # Open menu and DIG out
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

print("Script execution completed. Position:", mgba.get_coordinates())
mgba.take_screenshot()
