import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting corrected robust balcony route from:", get_pos())

def handle_battle():
    # Press B a few times to clear text if we are in transition or battle
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    # Check if we are in battle and select RUN
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.2)
    # Clear "Got away safely!" text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)

def step_to_closed_loop(tx, ty):
    print(f"Navigating to waypoint ({tx}, {ty})...")
    for attempt in range(15):
        c = get_pos()
        if c['x'] == tx and c['y'] == ty:
            print(f"Reached waypoint: ({tx}, {ty})")
            return True
            
        dx = tx - c['x']
        dy = ty - c['y']
        
        btn = None
        # Manhattan-based routing to waypoint
        # We use >= to prefer horizontal movement (Left/Right) over vertical (Up/Down) when magnitude is equal.
        # This prevents getting stuck against vertical obstacles like the column 22 rubble at (22, 5).
        if abs(dx) >= abs(dy):
            if dx > 0:
                btn = "Right"
            else:
                btn = "Left"
        else:
            if dy > 0:
                btn = "Down"
            else:
                btn = "Up"
                
        print(f"  Attempt {attempt+1}/15. Pos: {c}. Pressing {btn}")
        mgba.press_buttons([btn])
        time.sleep(0.4)
        
        after = get_pos()
        if after == c:
            print("  Blocked! Handling potential battle/dialogue...")
            handle_battle()
            after_retry = get_pos()
            print(f"  After handle_battle, pos is: {after_retry}")
            
    c_final = get_pos()
    if c_final['x'] == tx and c_final['y'] == ty:
        return True
    print(f"FAILED to reach waypoint ({tx}, {ty}). Final pos: {c_final}")
    return False

# Path from current position (22, 7) to B1F balcony drop
waypoints = [
    (21, 5),   # Gate is open in State B
    (21, 3),
    (26, 3),
    (26, 5),
    (24, 5),
    (24, 7),
    (26, 7),
    (26, 12),
    (25, 12),
    (25, 14),
    (22, 14),
    (21, 14),
    (21, 15),
    (20, 15),
    (20, 18),
    (19, 18)   # Balcony drop!
]

success = True
for (wx, wy) in waypoints:
    if not step_to_closed_loop(wx, wy):
        success = False
        break

if success:
    print("Mansion 3F Balcony Drop complete! Current pos on B1F:", get_pos())
    mgba.take_screenshot()
else:
    print("Failed to complete balcony drop route.")
