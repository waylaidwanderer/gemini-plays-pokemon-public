import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting Victory Drop Script. Current pos:", get_pos())

def handle_battle():
    print("  Battle/Dialogue detected! Handling...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.2)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)

def step_to_closed_loop(tx, ty):
    print(f"Navigating to ({tx}, {ty})...")
    for attempt in range(15):
        c = get_pos()
        if c['x'] == tx and c['y'] == ty:
            print(f"Reached: ({tx}, {ty})")
            return True
            
        dx = tx - c['x']
        dy = ty - c['y']
        
        btn = None
        if abs(dx) >= abs(dy):
            if dx > 0: btn = "Right"
            else: btn = "Left"
        else:
            if dy > 0: btn = "Down"
            else: btn = "Up"
            
        print(f"  Attempt {attempt+1}/15. Pos: {c}. Pressing {btn}")
        mgba.press_buttons([btn])
        time.sleep(0.4)
        
        after = get_pos()
        if after == c:
            print("  Blocked! Checking for battle/dialogue...")
            handle_battle()
            after_retry = get_pos()
            print(f"  After retry, pos is: {after_retry}")
            
    c_final = get_pos()
    if c_final['x'] == tx and c_final['y'] == ty:
        return True
    return False

# Clear menus
mgba.press_buttons(["B"])
time.sleep(0.3)

# Waypoints to navigate to the balcony drop in State B from current position (13, 12)
waypoints = [
    (12, 12),
    (12, 6),
    (26, 6),
    (26, 12),
    (25, 12),
    (25, 14),
    (22, 14),
    (21, 14),
    (21, 15),
    (20, 15)
]

success = True
for (wx, wy) in waypoints:
    if not step_to_closed_loop(wx, wy):
        success = False
        print(f"Failed to reach waypoint ({wx}, {wy})")
        break

if success:
    print("Reached balcony landing (20, 15) in State B! Dropping to B1F...")
    mgba.press_buttons([
        "Down", "sleep 400",
        "Down", "sleep 400",
        "Down", "sleep 400",
        "Left"
    ])
    time.sleep(3.0)
    print("Dropped! Current position on B1F:", get_pos())
    mgba.take_screenshot()
else:
    print("Failed to navigate to balcony landing.")
