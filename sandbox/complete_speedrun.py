import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    # Escape from battle using standard B-mashing and Run selection
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
    bridge.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 300"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 350"])

def navigate_to_target(tx, ty, is_teeth=False):
    print(f"Navigating to target: ({tx}, {ty})")
    stuck_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            run_away()
            continue
            
        cx, cy = pos
        if cx == tx and cy == ty:
            print(f"Arrived at target: ({tx}, {ty})")
            return True
            
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
            # We didn't move!
            if is_teeth and tx == 19 and ty == 25 and cx == 19 and cy == 26:
                print("We are standing below the Gold Teeth and cannot walk onto it. Trying to pick it up...")
                bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
                # After picking up, the tile should be walkable now or we can proceed
                # Let's see if the tile becomes walkable
                walk_step("Up")
                after_pickup_pos = get_pos()
                if after_pickup_pos is not None and after_pickup_pos[0] == 19 and after_pickup_pos[1] == 25:
                    print("Successfully walked onto the Gold Teeth tile after picking it up!")
                    return True
            
            stuck_count += 1
            print(f"Stuck count: {stuck_count}")
            if stuck_count > 5:
                print("Stuck too many times. Running RUN sequence to clear potential interaction/battle.")
                run_away()
                stuck_count = 0
                time.sleep(1.0)

def run_speedrun():
    print("Starting Complete Safari Zone Speedrun...")
    
    # 1. Start up path from current position (28, 24) to (27, 26)
    startup = [(27, 24), (27, 26)]
    for tx, ty in startup:
        navigate_to_target(tx, ty)
        
    # 2. Path in Safari Zone Center to transition to Area 1 (East)
    center_to_area1 = [(30, 26), (30, 10)]
    for tx, ty in center_to_area1:
        navigate_to_target(tx, ty)
        
    print("Transitioning to Area 1 (East)...")
    walk_step("Right")
    time.sleep(1.5)
    
    # 3. Path in Area 1 (East) to transition to Area 2 (North)
    area1_to_area2 = [
        (0, 24), (20, 24), (20, 20), (12, 20), (12, 22), (8, 22),
        (8, 8), (12, 8), (12, 6), (17, 6), (17, 8), (20, 8),
        (20, 3), (7, 3), (7, 5), (0, 5)
    ]
    for tx, ty in area1_to_area2:
        navigate_to_target(tx, ty)
        
    print("Transitioning to Area 2 (North)...")
    walk_step("Left")
    time.sleep(1.5)
    
    # 4. Path in Area 2 (North) to transition to Area 3 (West)
    area2_to_area3 = [
        (22, 31), (22, 22), (16, 22), (16, 28), (16, 33), (9, 33), (9, 36)
    ]
    for tx, ty in area2_to_area3:
        navigate_to_target(tx, ty)
        
    print("Transitioning to Area 3 (West)...")
    walk_step("Down")
    time.sleep(1.5)
    
    # 5. Path in Area 3 (West) to transition to Safari Zone Center
    area3_to_center = [
        (9, 13), (0, 13)
    ]
    for tx, ty in area3_to_center:
        navigate_to_target(tx, ty)
        
    print("Transitioning back to Safari Zone Center...")
    walk_step("Left")
    time.sleep(1.5)
    
    # 6. Path in Safari Zone Center (East Compartment) to Gold Teeth
    center_to_teeth = [
        (29, 26), (19, 26), (19, 25)
    ]
    for tx, ty in center_to_teeth:
        if tx == 19 and ty == 25:
            navigate_to_target(tx, ty, is_teeth=True)
        else:
            navigate_to_target(tx, ty)
            
    print("Gold Teeth obtained! Proceeding to the Secret House...")
    
    # 7. Step back down to Row 26
    navigate_to_target(19, 26)
    
    # 8. Path to the Secret House
    teeth_to_house = [
        (5, 26), (5, 14), (0, 14), (0, 8), (3, 8)
    ]
    for tx, ty in teeth_to_house:
        navigate_to_target(tx, ty)
        
    print("Arrived at the Secret House door at (3, 8)! Entering...")
    walk_step("Up")
    time.sleep(1.5)
    
    # Check final position
    pos = get_pos()
    print(f"Speedrun finished! Current position: {pos}")

if __name__ == "__main__":
    run_speedrun()
