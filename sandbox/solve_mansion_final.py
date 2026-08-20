import mgba
import time

# Complete, self-correcting Mansion solver.
# Resumes automatically from whichever floor/position we are currently on!

button_count = 0

def press_buttons_safe(buttons):
    global button_count
    button_count += len(buttons)
    return mgba.press_buttons(buttons)

def handle_battle():
    print("Action blocked or battle detected! Running battle auto-pilot...")
    for _ in range(5):
        press_buttons_safe(["B"])
        time.sleep(0.15)
    # Select RUN
    press_buttons_safe(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.0)
    for _ in range(5):
        press_buttons_safe(["B"])
        time.sleep(0.15)

def step_to(target_x, target_y):
    while True:
        pos = mgba.get_coordinates()
        if pos is None:
            time.sleep(0.3)
            continue
        
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            print(f"Reached target: ({target_x}, {target_y})")
            break
            
        direction = None
        if x < target_x:
            direction = "Right"
        elif x > target_x:
            direction = "Left"
        elif y < target_y:
            direction = "Down"
        elif y > target_y:
            direction = "Up"
            
        print(f"Current pos: ({x}, {y}). Pressing {direction} to reach ({target_x}, {target_y})...")
        press_buttons_safe([direction])
        time.sleep(0.4)
        
        after = mgba.get_coordinates()
        if after == pos:
            # We didn't move. Let's handle battle/NPC blocking
            handle_battle()
            after_retry = mgba.get_coordinates()
            if after_retry == pos:
                print("Still blocked. Detouring Up first...")
                press_buttons_safe(["Up"])
                time.sleep(0.35)
    return True

# Get our current map context by looking at our coordinates:
pos = mgba.get_coordinates()
if pos is None:
    print("Error: Could not get coordinates.")
    exit(0)

x, y = pos['x'], pos['y']
print(f"Current coordinates at start: ({x}, {y})")

# Determine which state / step we are on based on coordinates and active floor:
# Outside Cinnabar Island: y < 20 (Mansion entrance is at row 3-4, outside coordinates)
if y <= 15 and (x == 11 or x == 10 or x == 14):
    print("State: Outside Mansion. Walking to door at (6, 3)...")
    step_to(6, 12)
    step_to(6, 4)
    press_buttons_safe(["Up"]) # enter Mansion
    time.sleep(1.5)
    print("Entered Mansion! Current pos:", mgba.get_coordinates())
    exit(0)

# Inside Mansion 1F (where y >= 16)
# Wait, 1F has y values up to 27 (landing is at (5, 27))
if y >= 20 and x == 5:
    print("State: Mansion 1F. Walking to stairs at (7, 10)...")
    # Walk Up column 5 to row 11
    for ty in range(26, 10, -1):
        if button_count > 65:
            print("Nearing button limit. Exiting early.")
            exit(0)
        step_to(5, ty)
    step_to(7, 11)
    print("Ascending to 2F...")
    press_buttons_safe(["Up"]) # warp to 2F
    time.sleep(1.5)
    print("Landed on 2F:", mgba.get_coordinates())
    exit(0)

# On 2F: we land at (7, 11)
if y == 11 and x == 7:
    print("State: Mansion 2F (State A). Walking to east switch at (12, 11)...")
    # Let's walk Right to (11, 11)
    for tx in range(8, 12):
        if button_count > 60:
            print("Nearing button limit. Exiting early.")
            exit(0)
        step_to(tx, 11)
    
    # Toggle switch to State B!
    print("At (11, 11). Facing Right and toggling switch at (12, 11)...")
    press_buttons_safe(["Right", "sleep 250", "A", "sleep 1500", "A", "sleep 1500", "B"])
    time.sleep(3.0)
    print("Switch toggled. Position:", mgba.get_coordinates())
    exit(0)

# On 2F (State B): after toggling, we are at (11, 11).
# We need to walk back Left to (7, 10) to descend to 1F.
if y == 11 and x == 11:
    print("State: Mansion 2F (State B). Walking Left to stairs at (7, 10)...")
    for tx in range(10, 6, -1):
        if button_count > 65:
            print("Nearing button limit. Exiting early.")
            exit(0)
        step_to(tx, 11)
    print("Descending to 1F...")
    press_buttons_safe(["Up"]) # warp to 1F
    time.sleep(1.5)
    print("Landed on 1F:", mgba.get_coordinates())
    exit(0)

# If we are in another position, let's print it and wait
print("Position is not in standard initial states. Stand still.")
