import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting warp and switch run. Current pos:", get_pos())

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

# 1. Walk from (20, 15) to (16, 11) on 3F
waypoints_3f = [
    (21, 15),
    (21, 14),
    (18, 14),
    (18, 11),
    (16, 11)
]

success_3f = True
for (wx, wy) in waypoints_3f:
    if not step_to_closed_loop(wx, wy):
        success_3f = False
        print(f"Failed to reach 3F waypoint ({wx}, {wy})")
        break

if success_3f:
    print("Reached stairs landing (16, 11) on 3F. Stepping Left to warp to 2F...")
    mgba.press_buttons(["Left"])
    time.sleep(2.0)
    print("Warp complete. Current pos (should be on 2F):", get_pos())
    
    # 2. Walk on 2F to (12, 11)
    waypoints_2f = [
        (16, 7),
        (12, 7),
        (12, 11)
    ]
    
    success_2f = True
    for (wx, wy) in waypoints_2f:
        if not step_to_closed_loop(wx, wy):
            success_2f = False
            print(f"Failed to reach 2F waypoint ({wx}, {wy})")
            break
            
    if success_2f:
        print("Successfully reached switch station (12, 11) on 2F!")
        mgba.take_screenshot()
    else:
        print("Failed to navigate 2F.")
else:
    print("Failed to navigate 3F back to stairs.")
