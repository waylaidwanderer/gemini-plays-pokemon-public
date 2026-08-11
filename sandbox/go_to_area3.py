import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Attempting to run away from battle...")
    # Clear any battle start text first
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
    # Press Down, Right, A to select RUN
    bridge.press_buttons(["Down", "Right", "A", "sleep 500"])

def walk_step(direction):
    # Press direction button
    bridge.press_buttons([direction, "sleep 300"])

def navigate_path(path):
    for target in path:
        tx, ty = target
        print(f"Navigating to target: ({tx}, {ty})")
        while True:
            pos = get_pos()
            if pos is None:
                run_away()
                continue
            
            cx, cy = pos
            if cx == tx and cy == ty:
                print(f"Arrived at ({tx}, {ty})")
                break
                
            dx = tx - cx
            dy = ty - cy
            
            if dx > 0:
                dir_btn = "Right"
            elif dx < 0:
                dir_btn = "Left"
            elif dy > 0:
                dir_btn = "Down"
            elif dy < 0:
                dir_btn = "Up"
            else:
                break
                
            walk_step(dir_btn)
            
            new_pos = get_pos()
            if new_pos is None:
                run_away()
                continue
                
            ncx, ncy = new_pos
            if ncx == cx and ncy == cy:
                print("Coordinates did not change. Possible battle or block. Attempting to run/clear...")
                run_away()
                after_run_pos = get_pos()
                if after_run_pos == pos:
                    print(f"BLOCKED! Stalled at ({cx}, {cy}) trying to go {dir_btn}")
                    return False
    return True

def run_safari_speedrun():
    print("Starting Safari Speedrun from Center to Area 3 (West)...")
    
    # 1. PATH 1: Center to Area 1 (East)
    path1 = [(15, 16), (29, 16), (29, 11)]
    if not navigate_path(path1):
        print("Failed on Path 1.")
        return False
    
    # Take 1 extra step Right to transition into Area 1 (East)
    print("Transitioning into Area 1 (East)...")
    walk_step("Right")
    time.sleep(1.0) # Wait for map transition
    
    # Verify we are in Area 1 (East)
    pos = get_pos()
    print(f"Area 1 Position: {pos}")
    if pos is None or pos[0] > 5:
        print("Transition failed or unexpected coordinates. Trying to realign...")
        # If we got blocked or are not at (0, 23), handle it
    
    # 2. PATH 2: Area 1 (East) to Area 2 (North)
    path2 = [(20, 23), (20, 3), (7, 3), (7, 5), (0, 5)]
    if not navigate_path(path2):
        print("Failed on Path 2.")
        return False
        
    # Take 1 extra step Left to transition into Area 2 (North)
    print("Transitioning into Area 2 (North)...")
    walk_step("Left")
    time.sleep(1.0) # Wait for map transition
    
    # Verify we are in Area 2 (North)
    pos = get_pos()
    print(f"Area 2 Position: {pos}")
    
    # 3. PATH 3: Area 2 (North) to Area 3 (West)
    path3 = [
        (22, 31), (22, 23), (22, 22), (16, 22), (16, 27), (16, 28), 
        (12, 28), (12, 33), (8, 33), (4, 33), (4, 35)
    ]
    if not navigate_path(path3):
        print("Failed on Path 3.")
        return False
        
    # Take 1 extra step Down to transition into Area 3 (West)
    print("Transitioning into Area 3 (West)...")
    walk_step("Down")
    time.sleep(1.0) # Wait for map transition
    
    pos = get_pos()
    print(f"Arrived in Area 3 (West)! Position: {pos}")
    return True

run_safari_speedrun()
