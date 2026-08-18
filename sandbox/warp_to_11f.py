import mgba
import time

def move_to(target_x, target_y):
    current = mgba.get_coordinates()
    print(f"Moving from {current} to ({target_x}, {target_y})")
    
    while current['x'] != target_x or current['y'] != target_y:
        dx = target_x - current['x']
        dy = target_y - current['y']
        
        button = None
        if dy < 0:
            button = "Up"
        elif dy > 0:
            button = "Down"
        elif dx < 0:
            button = "Left"
        elif dx > 0:
            button = "Right"
            
        if not button:
            break
            
        mgba.press_buttons([button])
        time.sleep(0.3)
        
        next_pos = mgba.get_coordinates()
        if next_pos == current:
            print(f"ERROR: Stuck at ({current['x']}, {current['y']}) trying to move {button}!")
            mgba.take_screenshot()
            return False
        current = next_pos
        
    return True

print("Step 1: Stepping off and back onto teleporter at (9, 15) on 5F to return to 3F...")
mgba.press_buttons(["Down"])
time.sleep(0.3)
print(f"Position after stepping down: {mgba.get_coordinates()}")

mgba.press_buttons(["Up"])
time.sleep(0.5)

# Wait for map transition to 3F (x == 17, y == 15)
retries = 10
success_3f = False
while retries > 0:
    pos = mgba.get_coordinates()
    if pos['x'] == 17 and pos['y'] == 15:
        print(f"Successfully returned to 3F at {pos}!")
        success_3f = True
        break
    print(f"Waiting for 3F warp transition... current pos: {pos}")
    time.sleep(0.3)
    retries -= 1

if success_3f:
    # 2. Walk on 3F to teleporter at (11, 11) via Column 18 (safe path)
    waypoints_3f = [
        (17, 16),
        (18, 16),
        (18, 8),
        (17, 8),
        (11, 8),
        (11, 11)
    ]
    
    print("Navigating Saffron Silph Co. 3F via safe Column 18 path...")
    success_nav = True
    for wp in waypoints_3f:
        if not move_to(wp[0], wp[1]):
            success_nav = False
            break
            
    if success_nav:
        print("Reached teleporter at (11, 11) on 3F! Warping to 7F...")
        time.sleep(1.0)
        pos_7f = mgba.get_coordinates()
        print(f"Landed on 7F at {pos_7f}")
        
        # 3. 7F Navigation: (5, 3) -> (3, 3) -> (3, 7) -> (5, 7)
        waypoints_7f = [
            (3, 3),
            (3, 7),
            (5, 7)
        ]
        
        success_7f = True
        for wp in waypoints_7f:
            if not move_to(wp[0], wp[1]):
                success_7f = False
                break
                
        if success_7f:
            print("Reached warp at (5, 7) on 7F! Warping to 11F...")
            time.sleep(1.0)
            pos_11f = mgba.get_coordinates()
            print(f"Landed on 11F at {pos_11f}")
            mgba.take_screenshot()
        else:
            print("ERROR: Failed 7F navigation.")
            mgba.take_screenshot()
    else:
        print("ERROR: Failed 3F navigation.")
        mgba.take_screenshot()
else:
    print("ERROR: Failed to warp back to 3F.")
    mgba.take_screenshot()
