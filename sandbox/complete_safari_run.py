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
            # Transition occurred or battle
            time.sleep(1.0)
            new_pos = get_pos()
            if new_pos is None:
                handle_battle()
                continue
            else:
                if check_warp:
                    dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                    if dist > 5:
                        print(f"SUCCESS! Transitioned to coordinates: {new_pos}")
                        break
                idx += 1
                continue
            
        if new_pos == pos:
            # Let's wait a moment and check if we are actually in a battle transition
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

def get_area1_path(pos):
    path = []
    # If we are at the very start (0, 22) or (0, 23)
    if pos[0] == 0 and (pos[1] == 22 or pos[1] == 23):
        path.append("Down") # to (0, 24)
        path.extend(["Right"] * 20) # to (20, 24)
        path.extend(["Up"] * 3)            # to (20, 21)
        path.append("Up")                  # to (20, 20) (climb stairs)
        path.extend(["Left"] * 8)          # to (12, 20)
    elif pos[1] <= 20 and pos[0] >= 12:
        # We are already on the Eastern Plateau!
        # Walk to (12, 20)
        if pos[1] < 20:
            path.extend(["Down"] * (20 - pos[1]))
        elif pos[1] > 20:
            path.extend(["Up"] * (pos[1] - 20))
        if pos[0] > 12:
            path.extend(["Left"] * (pos[0] - 12))
        elif pos[0] < 12:
            path.extend(["Right"] * (12 - pos[0]))
    else:
        # Intermediate on the lower ground
        if pos[1] < 24:
            path.extend(["Down"] * (24 - pos[1]))
        elif pos[1] > 24:
            path.extend(["Up"] * (pos[1] - 24))
        if pos[0] < 20:
            path.extend(["Right"] * (20 - pos[0]))
        elif pos[0] > 20:
            path.extend(["Left"] * (pos[0] - 20))
        path.extend(["Up"] * 3)            # to (20, 21)
        path.append("Up")                  # to (20, 20) (climb stairs)
        path.extend(["Left"] * 8)          # to (12, 20)
            
    # Now we are at (12, 20) on the Plateau. Descend and do the rest!
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
    # If we are on the east side of Column 17 (meaning X >= 18)
    if pos[0] >= 18:
        # If we are not yet on Column 22, walk horizontally to Column 22 first
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
            # We are already on Column 22! Just walk to Row 24 directly
            if pos[1] < 24:
                path.extend(["Down"] * (24 - pos[1]))
            elif pos[1] > 24:
                path.extend(["Up"] * (pos[1] - 24))
            
        # Now we are at (22, 24). Climb the plateau!
        path.extend(["Up"] * 2)            # to (22, 22) (climbs stairs)
        path.extend(["Left"] * 6)          # to (16, 22)
        path.extend(["Down"] * 6)          # to (16, 28) (descends stairs)
        path.extend(["Left"] * 4)          # to (12, 28)
        path.extend(["Down"] * 5)          # to (12, 33)
        path.extend(["Left"] * 4)          # to (8, 33)
        path.extend(["Down"] * 3)          # to Area 3 warp!
    else:
        # We are already on the west side of Column 17 (meaning X < 18)
        # Walk to (12, 33)
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

def run_campaign_to_area3():
    print("=== EXECUTING MASTER SPEEDRUN TO AREA 3 (WEST) ===")
    
    pos = get_pos()
    print("Starting position:", pos)
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return False
            
    # Determine where we are and set up paths dynamically!
    path_center = []
    path_area1 = []
    path_area2 = []
    path_area3 = []
    
    # 1. Check if we are in Safari Zone Center (only if start at (15,25))
    if pos == (15, 25):
        path_center = [
            "Up", "Up", "Up", "Up",                               # to (15, 21)
            "Right", "Right", "Right", "Right", "Right", "Right", 
            "Right", "Right", "Right", "Right", "Right", "Right", "Right", # to (28, 21) (13 steps Right)
            "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up",   # to (28, 11) (10 steps Up)
            "Right", "Right", "Right"                              # to Area 1 warp!
        ]
        
    if len(path_center) > 0:
        print("Walking across Center to Area 1 (East)...")
        if not run_path(path_center, check_warp=True):
            print("Failed to reach Area 1!")
            return False
        time.sleep(1.0)
        pos = get_pos()
        print("Position inside Area 1 (East):", pos)
        
    # 2. Check if we are in Area 1 (East)
    if pos is not None and pos[0] <= 38 and pos[1] <= 24:
        print("Using dynamic spiral generator for Area 1 (East)...")
        path_area1 = get_area1_path(pos)
            
    if len(path_area1) > 0:
        print("Walking across Area 1 (East) to Area 2 (North)...")
        if not run_path(path_area1, check_warp=True):
            print("Failed to reach Area 2!")
            return False
        time.sleep(1.0)
        pos = get_pos()
        print("Position inside Area 2 (North):", pos)
        
    # 3. Check if we are in Area 2 (North)
    # Detect based on typical coordinates in Area 2 (North)
    # Area 2 is generally x >= 0 with y <= 36. If we have not transitioned to Area 3 yet, we are in Area 2.
    # Area 3 starts at (26, 0)
    if pos is not None and not (pos[0] == 26 and pos[1] == 0):
        print("Using dynamic path generator for Area 2 (North)...")
        path_area2 = get_area2_path(pos)
        
    if len(path_area2) > 0:
        print("Walking across Area 2 (North) to Area 3 (West)...")
        if not run_path(path_area2, check_warp=True):
            print("Failed to reach Area 3!")
            return False
        time.sleep(1.0)
        pos = get_pos()
        print("Position inside Area 3 (West):", pos)
        
    # 4. Check if we are in Area 3 (West) starting at (26, 0)
    if pos is not None and pos[0] == 26 and pos[1] == 0:
        path_area3 = [
            "Down", "Down", "Down",                                           # to (26, 3)
            "Left",                                                           # to (25, 3)
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
            "Down", "Down", "Down", "Down", "Down", "Down", "Down",           # to (25, 18) (15 steps Down)
            "Left", "Left", "Left", "Left"                                    # to (21, 18) (East Stairs)
        ]
        
    if len(path_area3) > 0:
        print("Walking to East Stairs in Area 3 (West) at (21, 18)...")
        if not run_path(path_area3, check_warp=False):
            print("Failed to reach East Stairs!")
            return False
            
    print("=== CAMPAIGN SUCCESS! ARRIVED AT (21, 18) IN AREA 3 ===")
    return True

if __name__ == "__main__":
    run_campaign_to_area3()
