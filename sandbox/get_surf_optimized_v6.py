import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        time.sleep(0.1)
    return None

def handle_battle():
    print("Wild battle/interaction detected! Escaping...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 250"])
    bridge.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1200"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction])
    
    # Wait for position to change (up to 750 ms)
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is None:
            return None
        if new_pos != pos:
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        print(f"Path step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                if check_warp:
                    print("SUCCESS! Transition occurred!")
                    return True
                handle_battle()
                continue
                
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Path blocked. Exiting path.")
                return False
        else:
            stuck_count = 0
            idx += 1
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"SUCCESS! Transitioned to coordinates: {new_pos}")
                    break
    return True

def run_surf_campaign():
    pos = get_pos()
    print("Starting campaign from position:", pos)
    
    # Check if we are still in the Gatehouse
    if pos is not None and pos[0] == 4 and pos[1] == 2:
        print("=== STAGE 1: Progressing Dialogue to Enter Safari Zone ===")
        warped = False
        for i in range(15):
            pos = get_pos()
            if pos is not None and pos[0] == 15 and pos[1] == 25:
                print("Successfully entered Safari Zone Center!")
                warped = True
                break
            print(f"Dialogue Progress Press {i+1}...")
            bridge.press_buttons(["A", "sleep 1200"])
            
        if not warped:
            pos = get_pos()
            if pos is not None and pos[0] == 15 and pos[1] == 25:
                print("Successfully entered Safari Zone Center!")
            else:
                print(f"Error: Did not enter Safari Zone. Coordinates are: {pos}")
                return False
                
    pos = get_pos()
    path_center = []
    
    # If we are at the entrance of Center
    if pos is not None and pos[0] == 15 and pos[1] == 25:
        path_center.extend(["Up"] * 2)               # to (15, 23)
        path_center.extend(["Right"] * 12)           # to (27, 23) (using Row 23 highway to bypass signposts!)
        path_center.extend(["Down"] * 3)             # to (27, 26)
        path_center.extend(["Right"] * 3)            # to (30, 26)
        path_center.extend(["Up"] * 15)              # to (30, 11)
        path_center.append("Left")                   # to (29, 11)
        path_center.append("Right")                  # transition to Area 1 (East)
    # If we are currently at (21, 24)
    elif pos is not None and pos[0] == 21 and pos[1] == 24:
        path_center.append("Up")                     # to (21, 23)
        path_center.extend(["Right"] * 6)            # to (27, 23)
        path_center.extend(["Down"] * 3)             # to (27, 26)
        path_center.extend(["Right"] * 3)            # to (30, 26)
        path_center.extend(["Up"] * 15)              # to (30, 11)
        path_center.append("Left")                   # to (29, 11)
        path_center.append("Right")                  # transition to Area 1 (East)
    else:
        print(f"Unknown starting position: {pos}")
        return False
        
    print("=== STAGE 2: Walking Safari Zone Center to Area 1 ===")
    if not run_path(path_center, check_warp=True):
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Coordinates in Area 1 East:", pos)
    
    # 3. Path in Area 1 (East) to Area 2 (North)
    path_area1 = [
        "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right",
        "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", # (0, 23) -> (20, 23)
        "Up", "Up",               # (20, 23) -> (20, 21) (climb Southern Plateau)
        "Up",                     # (20, 21) -> (20, 20) (onto Southern Plateau)
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # (20, 20) -> (12, 20)
        "Down", "Down",           # (12, 20) -> (12, 22) (descend plateau)
        "Left", "Left", "Left",   # (12, 22) -> (9, 22)
        "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", # (9, 22) -> (9, 8)
        "Right", "Right", "Right", # (9, 8) -> (12, 8)
        "Up", "Up",               # (12, 8) -> (12, 6) (climb Northern Plateau)
        "Right", "Right", "Right", "Right", "Right", # (12, 6) -> (17, 6)
        "Down", "Down",           # (17, 6) -> (17, 8) (descend Northern Plateau)
        "Right", "Right", "Right", # (17, 8) -> (20, 8)
        "Up", "Up", "Up",         # (20, 8) -> (20, 5)
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left"  # (20, 5) -> (0, 5) (warp!)
    ]
    
    print("=== STAGE 3: Walking Area 1 to Area 2 ===")
    if not run_path(path_area1, check_warp=True):
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Coordinates in Area 2 North:", pos)
    
    # 4. Path in Area 2 (North) using Column 25 and Row 9 ground-level route
    path_area2 = [
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
        "Left", "Left", "Left", "Left", # (39, 31) -> (25, 31) (14 steps Left)
        "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up",
        "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up",
        "Up", "Up",                     # (25, 31) -> (25, 9) (22 steps Up)
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
        "Left",                         # (25, 9) -> (4, 9) (21 steps Left)
        "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
        "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
        "Down", "Down", "Down", "Down", "Down", "Down", "Down" # (4, 9) -> (4, 36) (27 steps Down, warp!)
    ]
    
    print("=== STAGE 4: Walking Area 2 to Southwest Transition ===")
    if not run_path(path_area2, check_warp=True):
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Coordinates in Area 3 West northwest ground:", pos)
    
    # 5. Path inside Area 3 (West) northwest ground to Secret House
    path_area3 = []
    if pos is not None and pos[0] == 2:
        path_area3.append("Right")
    elif pos is not None and pos[0] == 4:
        path_area3.append("Left")
        
    path_area3.extend(["Down"] * 8)   # to (3, 8)
    path_area3.append("Up")           # enter Secret House!
    
    print("=== STAGE 5: Walking to Secret House ===")
    if not run_path(path_area3, check_warp=True):
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Coordinates inside Secret House:", pos)
    
    # 6. Interact with NPC at (2, 7)
    path_inside = [
        "Up", "Up", "Up"  # stand in front of NPC at (2, 7) or similar
    ]
    print("=== STAGE 6: Walking to NPC inside Secret House ===")
    run_path(path_inside)
    
    print("Talking to NPC to obtain Surf...")
    bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
    print("=== CAMPAIGN COMPLETE! SURF SHOULD BE OBTAINED ===")
    return True

if __name__ == "__main__":
    run_surf_campaign()
