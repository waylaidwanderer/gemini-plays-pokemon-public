import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Running 2F switch toggle script. Starting pos:", get_pos())

def handle_battle():
    # Clear screens
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    # Run from battle
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.2)
    # Clear textbox
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

# Path to the switch at (12, 11) on 2F via row 7
waypoints = [
    (16, 9), (16, 7),
    (14, 7), (12, 7),
    (12, 9), (12, 11)
]

success = True
for (wx, wy) in waypoints:
    if not step_to_closed_loop(wx, wy):
        success = False
        break

if success:
    print("Reached (12, 11). Toggling 2F switch to State B...")
    mgba.press_buttons([
        "Right", "sleep 500",
        "A", "sleep 1500",
        "Up", "sleep 500",
        "A", "sleep 1500",
        "B", "sleep 500",
        "B"
    ])
    time.sleep(5.0)
    print("Mansion switch toggled to State B! Current pos:", get_pos())
    mgba.take_screenshot()
else:
    print("Failed to reach (12, 11).")
