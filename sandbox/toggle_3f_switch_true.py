import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting robust toggle sequence from:", get_pos())

def handle_battle():
    # Press B a few times to clear text if we are in transition or battle
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    # Check if we are in battle and select RUN
    # FIGHT (0,0), PKMN (1,0)
    # ITEM (0,1), RUN (1,1)
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
        if abs(dx) > abs(dy):
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

# Clear "Got away safely!" textbox first
mgba.press_buttons(["B"])
time.sleep(0.3)

waypoints = [
    (11, 6),   # Corridor column 11 row 6
    (11, 11),  # Down corridor
    (3, 11),   # Left through open gate
    (3, 12),   # Down to bypass statue
    (1, 12),   # Left to column 1
    (1, 11)    # Up to switch position
]

success = True
for (wx, wy) in waypoints:
    if not step_to_closed_loop(wx, wy):
        success = False
        break

if success:
    print("Reached switch station (1, 11). Turning Right...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    print("Interacting with Switch...")
    mgba.press_buttons(["A"])
    time.sleep(0.6)
    mgba.press_buttons(["A"]) # Choose YES
    time.sleep(0.6)
    # Clear text
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    print("Mansion switch toggled to State B! Current pos:", get_pos())
    mgba.take_screenshot()
else:
    print("Failed to reach switch station.")
