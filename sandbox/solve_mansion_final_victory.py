import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Running final victory script from 2F to B1F. Current pos:", get_pos())

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

# 1. Walk from (16, 10) to (16, 11) on 2F
if step_to_closed_loop(16, 11):
    print("Reached (16, 11). Warping UP to 3F...")
    mgba.press_buttons(["Left"]) # Step Left onto the stairs at (15, 11) to warp up
    time.sleep(1.5)
    print("Landed on 3F in State A! Current pos:", get_pos())
    
    # 2. Walk to the balcony drop on 3F in State A
    waypoints_to_drop = [
        (20, 11),
        (20, 15),
        (20, 18), # In State A, both row 16 gate and row 17 gate are open!
        (19, 18)  # Step Left to drop!
    ]
    success_drop = True
    for (wx, wy) in waypoints_to_drop:
        if not step_to_closed_loop(wx, wy):
            success_drop = False
            break
            
    if success_drop:
        print("Mansion 3F Balcony Drop complete! Current pos on B1F:", get_pos())
        mgba.take_screenshot()
    else:
        print("Failed to complete balcony drop on 3F.")
else:
    print("Failed to reach stairs on 2F.")
