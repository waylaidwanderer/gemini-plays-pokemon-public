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
    
    # 1. Check if we are in Safari Zone Center
    if pos == (15, 25):
        path_center = [
            "Up", "Up", "Up", "Up",                               # to (15, 21)
            "Right", "Right", "Right", "Right", "Right", "Right", 
            "Right", "Right", "Right", "Right", "Right", "Right", "Right", # to (28, 21) (13 steps Right)
            "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up",   # to (28, 11) (10 steps Up)
            "Right", "Right", "Right"                              # to Area 1 warp!
        ]
    elif pos[1] == 21 and pos[0] >= 15 and pos[0] <= 28:
        print(f"Resuming Center navigation from Row 21: {pos}")
        remaining_right = 28 - pos[0]
        path_center.extend(["Right"] * remaining_right)
        path_center.extend(["Up"] * 10)
        path_center.extend(["Right"] * 3)
    elif pos[0] == 28 and pos[1] <= 21 and pos[1] >= 11:
        print(f"Resuming Center navigation from Column 28: {pos}")
        remaining_up = pos[1] - 11
        path_center.extend(["Up"] * remaining_up)
        path_center.extend(["Right"] * 3)
        
    if len(path_center) > 0:
        print("Walking across Center to Area 1 (East)...")
        if not run_path(path_center, check_warp=True):
            print("Failed to reach Area 1!")
            return False
        time.sleep(1.0)
        pos = get_pos()
        print("Position inside Area 1 (East):", pos)
        
    # 2. Check if we are in Area 1 (East)
    # We are in Area 1 if we are on Row 22/23/24 with X <= 20, or Row 5, etc.
    # Let's detect based on coordinates
    if pos is not None:
        is_area1 = False
        if pos[1] == 23 and pos[0] <= 20:
            is_area1 = True
            print(f"Resuming Area 1 navigation from Row 23: {pos}")
            # Detour down to Row 24 first
            path_area1.append("Down")
            remaining_right = 20 - pos[0]
            path_area1.extend(["Right"] * remaining_right)
            path_area1.extend(["Up"] * 19) # to (20, 5)
            path_area1.extend(["Left"] * 20) # to (0, 5) (warp)
        elif pos[1] == 24 and pos[0] <= 20:
            is_area1 = True
            print(f"Resuming Area 1 navigation from Row 24: {pos}")
            remaining_right = 20 - pos[0]
            path_area1.extend(["Right"] * remaining_right)
            path_area1.extend(["Up"] * 19) # to (20, 5)
            path_area1.extend(["Left"] * 20) # to (0, 5) (warp)
        elif pos[0] == 20 and pos[1] <= 24 and pos[1] >= 5:
            is_area1 = True
            print(f"Resuming Area 1 navigation from Column 20: {pos}")
            if pos[1] >= 11:
                # Bypass the NPC at (20, 17) by walking Right to Column 21, Up, Left!
                path_area1.append("Right") # to (21, pos[1])
                remaining_up = pos[1] - 5
                path_area1.extend(["Up"] * remaining_up) # to (21, 5)
                path_area1.append("Left") # to (20, 5)
                path_area1.extend(["Left"] * 20) # to (0, 5)
            else:
                remaining_up = pos[1] - 5
                path_area1.extend(["Up"] * remaining_up)
                path_area1.extend(["Left"] * 20)
        elif pos == (20, 12):
            is_area1 = True
            print("Resuming Area 1 navigation from (20, 12)...")
            path_area1.append("Right") # to (21, 12)
            path_area1.extend(["Up"] * 7) # to (21, 5)
            path_area1.extend(["Left"] * 21) # to (0, 5)
        elif pos == (21, 12):
            is_area1 = True
            print("Resuming Area 1 navigation from (21, 12)...")
            path_area1.append("Left") # to (20, 12)
            path_area1.extend(["Up"] * 7) # to (20, 5)
            path_area1.extend(["Left"] * 20) # to (0, 5)
        elif pos[1] == 5 and pos[0] <= 20:
            is_area1 = True
            print(f"Resuming Area 1 navigation from Row 5: {pos}")
            path_area1.extend(["Left"] * pos[0])
            
    if len(path_area1) > 0:
        print("Walking across Area 1 (East) to Area 2 (North)...")
        if not run_path(path_area1, check_warp=True):
            print("Failed to reach Area 2!")
            return False
        time.sleep(1.0)
        pos = get_pos()
        print("Position inside Area 2 (North):", pos)
        
    # 3. Check if we are in Area 2 (North)
    if pos is not None and pos[0] == 39 and pos[1] == 31:
        path_area2 = [
            "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
            "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
            "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
            "Left", "Left", "Left",                                           # to (12, 31) (27 steps Left)
            "Down", "Down",                                                   # to (12, 33) (2 steps Down)
            "Left", "Left", "Left", "Left",                                   # to (8, 33) (4 steps Left)
            "Down", "Down", "Down"                                            # to Area 3 warp!
        ]
        
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
