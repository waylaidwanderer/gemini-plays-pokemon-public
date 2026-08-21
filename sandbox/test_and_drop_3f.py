import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting balcony drop test. Current pos:", get_pos())

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

# Clear any lingering menus
mgba.press_buttons(["B"])
time.sleep(0.3)

# Waypoints to balcony landing (20, 15) on 3F
waypoints = [
    (18, 11),
    (18, 14),
    (20, 14),
    (20, 15)
]

success = True
for (wx, wy) in waypoints:
    if not step_to_closed_loop(wx, wy):
        success = False
        print(f"Failed to reach waypoint ({wx}, {wy})")
        break

if success:
    print("Reached balcony landing (20, 15) successfully! Checking gate at (20, 17)...")
    # Take screenshot at landing
    mgba.take_screenshot()
    
    # Try to walk down to the drop zone
    # If the gate is closed, we will be blocked at (20, 16) or (20, 17).
    print("Attempting to walk Down through the gate to (20, 18)...")
    step_to_closed_loop(20, 18)
    
    current = get_pos()
    if current['x'] == 20 and current['y'] == 18:
        print("Gate is OPEN! We are at (20, 18). Stepping Left to drop to B1F...")
        mgba.press_buttons(["Left"])
        time.sleep(2.0) # wait for fall animation
        print("Dropped! Current position on B1F:", get_pos())
        mgba.take_screenshot()
    else:
        print("Blocked! Gate at (20, 17) is CLOSED in State A.")
        mgba.take_screenshot()
else:
    print("Failed to reach balcony landing.")
