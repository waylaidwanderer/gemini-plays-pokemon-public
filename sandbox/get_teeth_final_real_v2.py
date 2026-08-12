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
    print("Wild battle detected! Escaping...")
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
    
    # Wait for position to change
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is None:
            time.sleep(1.0)
            new_pos = get_pos()
            if new_pos is None:
                handle_battle()
                return None
            else:
                return new_pos
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
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(1.0)
            new_pos = get_pos()
            if new_pos is None:
                handle_battle()
                continue
            else:
                if check_warp and idx == len(path) - 1:
                    print("Transition occurred on last step!")
                    return True
                idx += 1
                continue
            
        if new_pos == pos:
            time.sleep(0.5)
            check_pos = get_pos()
            if check_pos is None:
                print("Battle transition detected during stuck check! Handling battle...")
                handle_battle()
                stuck_count = 0
                continue
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Path blocked. Exiting path.")
                return False
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"SUCCESS! Transitioned to coordinates: {new_pos}")
                    break
            idx += 1
    return True

def get_center_path(pos):
    path = []
    # If we are on row 21
    if pos[1] == 21:
        if pos[0] < 28:
            path.extend(["Right"] * (28 - pos[0]))
        elif pos[0] > 28:
            path.extend(["Left"] * (pos[0] - 28))
    # If we are on row 23 (e.g. starting position)
    elif pos[1] == 23:
        if pos[0] == 15:
            path.extend(["Up"] * 2)
            path.extend(["Right"] * 13)
        else:
            if pos[0] < 28:
                path.extend(["Right"] * (28 - pos[0]))
            path.extend(["Up"] * (pos[1] - 21))
    else:
        # Generic fallback
        if pos[1] > 21:
            path.extend(["Up"] * (pos[1] - 21))
        elif pos[1] < 21:
            path.extend(["Down"] * (21 - pos[1]))
        if pos[0] < 28:
            path.extend(["Right"] * (28 - pos[0]))
            
    # Once we are at (28, 21), we go to (28, 11) and then transition
    path.extend(["Up"] * 10)
    path.extend(["Right"] * 3)
    return path

def get_area1_path(pos):
    path = []
    if pos[0] == 0 and (pos[1] == 22 or pos[1] == 23):
        path.append("Down") # to (0, 24)
        path.extend(["Right"] * 20) # to (20, 24)
        path.extend(["Up"] * 3)            # to (20, 21)
        path.append("Up")                  # to (20, 20) (climb stairs)
        path.extend(["Left"] * 8)          # to (12, 20)
    else:
        # Fallback if we ended up elsewhere
        if pos[1] < 24:
            path.extend(["Down"] * (24 - pos[1]))
        elif pos[1] > 24:
            path.extend(["Up"] * (pos[1] - 24))
        if pos[0] < 20:
            path.extend(["Right"] * (20 - pos[0]))
        elif pos[0] > 20:
            path.extend(["Left"] * (pos[0] - 20))
        path.extend(["Up"] * 3)
        path.append("Up")
        path.extend(["Left"] * 8)
            
    path.extend(["Down"] * 2)          # to (12, 22) (descends stairs)
    path.extend(["Left"] * 3)          # to (9, 22)
    path.extend(["Up"] * 14)           # to (9, 8)
    path.extend(["Right"] * 3)         # to (12, 8)
    path.extend(["Up"] * 2)            # to (12, 6) (climbs stairs)
    path.extend(["Right"] * 5)         # to (17, 6)
    path.extend(["Down"] * 2)          # to (17, 8) (descends stairs)
    path.extend(["Right"] * 3)         # to (20, 8)
    path.extend(["Up"] * 5)            # to (20, 3)
    path.extend(["Left"] * 13)         # to (7, 3)
    path.extend(["Down"] * 2)          # to (7, 5)
    path.extend(["Left"] * 7)          # to (0, 5) (warp!)
    return path

def get_area2_path(pos):
    path = []
    if pos[0] >= 18:
        if pos[0] != 22:
            if pos[1] < 31:
                path.extend(["Down"] * (31 - pos[1]))
            elif pos[1] > 31:
                path.extend(["Up"] * (pos[1] - 31))
            if pos[0] < 22:
                path.extend(["Right"] * (22 - pos[0]))
            elif pos[0] > 22:
                path.extend(["Left"] * (pos[0] - 22))
        else:
            if pos[1] < 24:
                path.extend(["Down"] * (24 - pos[1]))
            elif pos[1] > 24:
                path.extend(["Up"] * (pos[1] - 24))
            
        path.extend(["Up"] * 2)            # to (22, 22) (climbs stairs)
        path.extend(["Left"] * 6)          # to (16, 22)
        path.extend(["Down"] * 6)          # to (16, 28) (descends stairs)
        path.extend(["Left"] * 4)          # to (12, 28)
        path.extend(["Down"] * 5)          # to (12, 33)
        path.extend(["Left"] * 4)          # to (8, 33)
        path.extend(["Down"] * 3)          # to Area 3 warp!
    else:
        if pos[1] < 33:
            path.extend(["Down"] * (33 - pos[1]))
        elif pos[1] > 33:
            path.extend(["Up"] * (pos[1] - 33))
        if pos[0] > 12:
            path.extend(["Left"] * (pos[0] - 12))
        elif pos[0] < 12:
            path.extend(["Right"] * (12 - pos[0]))
        path.extend(["Left"] * 4)          # to (8, 33)
        path.extend(["Down"] * 3)          # to Area 3 warp!
    return path

def main():
    print("=== EXECUTING COMPLETE SAFARI GOLD TEETH RUN V2 ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            print("Failed to get starting position!")
            return
            
    # Check if we are in Safari Zone Center based on some overworld facts (e.g. initial x <= 30 and y >= 11 and we know we started here)
    # Since we are running the script right now, if we are at (23, 21) or (15, 23) we are in Center
    is_center = (pos[1] == 21 or pos[1] == 23) and pos[0] <= 30
    
    # Segment 1: Safari Zone Center to Area 1 (East)
    if is_center:
        path_center = get_center_path(pos)
        print("Walking from Center to Area 1 (East)...")
        if not run_path(path_center, check_warp=True):
            print("Failed to reach Area 1!")
            return
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived in Area 1:", pos)
        
    # Segment 2: Area 1 (East) to Area 2 (North)
    if pos is not None and pos[0] <= 38 and pos[1] <= 24 and not (pos[0] == 26 and pos[1] == 0):
        path_area1 = get_area1_path(pos)
        print("Walking from Area 1 (East) to Area 2 (North)...")
        if not run_path(path_area1, check_warp=True):
            print("Failed to reach Area 2!")
            return
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived in Area 2:", pos)
        
    # Segment 3: Area 2 (North) to Area 3 (West)
    if pos is not None and not (pos[0] == 26 and pos[1] == 0):
        path_area2 = get_area2_path(pos)
        print("Walking from Area 2 (North) to Area 3 (West)...")
        if not run_path(path_area2, check_warp=True):
            print("Failed to reach Area 3!")
            return
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived in Area 3:", pos)
        
    # Segment 4: Area 3 (West) to Gold Teeth
    if pos is not None and pos[0] == 26 and pos[1] == 0:
        # 4a. Walk to East Stairs
        path_to_stairs = [
            "Down", "Down", "Down",                                           # to (26, 3)
            "Left",                                                           # to (25, 3)
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
            "Down", "Down", "Down", "Down", "Down", "Down", "Down",           # to (25, 18)
            "Left", "Left", "Left", "Left"                                    # to (21, 18) (East Stairs)
        ]
        print("Walking to East Stairs...")
        if not run_path(path_to_stairs, check_warp=False):
            print("Failed to reach East Stairs!")
            return
            
        # 4b. Climb plateau and descend West Stairs
        path_across_plateau = [
            "Up", "Up",                                                       # climb stairs to (21, 16)
            "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
            "Left", "Left", "Left", "Left", "Left", "Left", "Left",           # across plateau to (6, 16)
            "Down", "Down", "Down",                                           # to (6, 19)
            "Down", "Down",                                                   # descend stairs to (6, 21) ground
            "Left", "Left", "Left", "Left",                                   # to (2, 21)
            "Down"                                                            # to (2, 20)
        ]
        print("Navigating plateau...")
        if not run_path(path_across_plateau, check_warp=False):
            print("Failed to navigate plateau!")
            return
            
        # 4c. Walk via Southern Ground level to Gold Teeth
        path_to_teeth = [
            "Right", "Right", "Right", "Right", "Right", "Right", "Right",
            "Right", "Right", "Right", "Right", "Right", "Right", "Right",
            "Right", "Right", "Right", "Right", "Right",                      # to (21, 20)
            "Down", "Down", "Down", "Down", "Down", "Down",                   # to (21, 26)
            "Left", "Left"                                                    # to (19, 26)
        ]
        print("Walking to Gold Teeth...")
        if not run_path(path_to_teeth, check_warp=False):
            print("Failed to reach Gold Teeth location!")
            return
            
        # 4d. Face UP and pick up teeth
        print("Interacting with Gold Teeth overworld ball...")
        walk_step_robust("Up")
        time.sleep(0.5)
        bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
        print("=== GOLD TEETH ACQUIRED SUCCESSFULLY ===")
        
if __name__ == "__main__":
    main()

