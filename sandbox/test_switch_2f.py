import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Testing 2F Mewtwo switch from FRONT (13, 12) facing UP...")

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

# Clear "Got away safely!" textbox
mgba.press_buttons(["B"])
time.sleep(0.3)

# 1. Walk from (21, 15) on 3F to the stairs at (15, 11)
waypoints_to_stairs = [
    (21, 11),
    (16, 11),
    (15, 11) # Stairs
]

success_stairs = True
for (wx, wy) in waypoints_to_stairs:
    if not step_to_closed_loop(wx, wy):
        success_stairs = False
        break

if success_stairs:
    print("Reached (15, 11) on 3F. Warping down to 2F...")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    print("Landed on 2F. Current pos:", get_pos())
    
    # 2. Walk to (13, 12) on 2F
    waypoints_to_front = [
        (16, 9), (16, 7),
        (12, 7), (12, 12),
        (13, 12)
    ]
    success_front = True
    for (wx, wy) in waypoints_to_front:
        if not step_to_closed_loop(wx, wy):
            success_front = False
            break
            
    if success_front:
        print("Reached front position (13, 12). Facing UP...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        # Press A
        print("Pressing A...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Take a screenshot to inspect if textbox opened
        screenshot_file = mgba.take_screenshot()
        print("Screenshot taken after A at (13, 12) facing UP:", screenshot_file)
    else:
        print("Failed to reach (13, 12) on 2F.")
else:
    print("Failed to reach 3F stairs.")
