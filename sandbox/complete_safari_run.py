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
    
    # 1. Start at (15, 25) in Center
    pos = get_pos()
    print("Starting position:", pos)
    if pos != (15, 25):
        print("Expected starting position (15, 25) in Center!")
        if pos is None:
            handle_battle()
            pos = get_pos()
            if pos != (15, 25):
                return False
        else:
            return False
            
    # Center map to Area 1 (East)
    path_center = [
        "Up", "Up", "Up", "Up",                               # to (15, 21)
        "Right", "Right", "Right", "Right", "Right", "Right", 
        "Right", "Right", "Right", "Right", "Right", "Right", "Right", # to (28, 21) (13 steps Right)
        "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up",   # to (28, 11) (10 steps Up)
        "Right", "Right", "Right"                              # to Area 1 warp!
    ]
    print("Walking across Center to Area 1 (East)...")
    if not run_path(path_center, check_warp=True):
        print("Failed to reach Area 1!")
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Position inside Area 1 (East):", pos)
    
    # Area 1 (East) to Area 2 (North)
    path_area1 = [
        "Right", "Right", "Right", "Right", "Right", "Right", 
        "Right", "Right", "Right", "Right", "Right", "Right", 
        "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", # to (20, 22)
        "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up",
        "Up", "Up", "Up", "Up", "Up", "Up", "Up",                         # to (20, 5)
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
        "Left", "Left", "Left", "Left"                                    # to (0, 5) (warp!)
    ]
    print("Walking across Area 1 (East) to Area 2 (North)...")
    if not run_path(path_area1, check_warp=True):
        print("Failed to reach Area 2!")
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Position inside Area 2 (North):", pos)
    
    # Area 2 (North) to Area 3 (West)
    path_area2 = [
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
        "Left", "Left", "Left",                                           # to (12, 31) (27 steps Left)
        "Down", "Down",                                                   # to (12, 33) (2 steps Down)
        "Left", "Left", "Left", "Left",                                   # to (8, 33) (4 steps Left)
        "Down", "Down", "Down"                                            # to Area 3 warp!
    ]
    print("Walking across Area 2 (North) to Area 3 (West)...")
    if not run_path(path_area2, check_warp=True):
        print("Failed to reach Area 3!")
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Position inside Area 3 (West):", pos)
    
    # Area 3 (West) to (21, 18) (East Stairs)
    path_area3 = [
        "Down", "Down", "Down",                                           # to (26, 3)
        "Left",                                                           # to (25, 3)
        "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
        "Down", "Down", "Down", "Down", "Down", "Down", "Down",           # to (25, 18) (15 steps Down)
        "Left", "Left", "Left", "Left"                                    # to (21, 18) (East Stairs)
    ]
    print("Walking to East Stairs in Area 3 (West) at (21, 18)...")
    if not run_path(path_area3, check_warp=False):
        print("Failed to reach East Stairs!")
        return False
        
    print("=== CAMPAIGN SUCCESS! ARRIVED AT (21, 18) IN AREA 3 ===")
    return True

if __name__ == "__main__":
    run_campaign_to_area3()
