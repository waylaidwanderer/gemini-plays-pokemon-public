import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Running solve_mansion_row3.py. Starting pos:", get_pos())

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

# Clear "Got away safely!" textbox first
mgba.press_buttons(["B"])
time.sleep(0.3)

# 1. Walk to the switch at (12, 11)
waypoints_to_switch = [
    (17, 7),
    (12, 7),
    (12, 11)
]

success_to = True
for (wx, wy) in waypoints_to_switch:
    if not step_to_closed_loop(wx, wy):
        success_to = False
        break

if success_to:
    print("Successfully reached switch station (12, 11). Toggling switch to State B...")
    mgba.press_buttons([
        "Right", "sleep 500",
        "A", "sleep 1500",
        "Up", "sleep 500",
        "A", "sleep 1500",
        "B", "sleep 500",
        "B"
    ])
    time.sleep(5.0)
    print("Mansion switch toggled! Checking pos:", get_pos())
    
    # 2. Walk back to the stairs at (16, 11)
    waypoints_back = [
        (12, 7),
        (16, 7),
        (16, 11)
    ]
    
    success_back = True
    for (wx, wy) in waypoints_back:
        if not step_to_closed_loop(wx, wy):
            success_back = False
            break
            
    if success_back:
        print("Reached (16, 11). Warping back UP to 3F...")
        mgba.press_buttons(["Left"]) # Step Left onto the stairs at (15, 11)
        time.sleep(1.5)
        print("Landed on 3F! Current pos:", get_pos())
        mgba.take_screenshot()
    else:
        print("Failed to walk back to the stairs.")
else:
    print("Failed to reach the switch.")
