import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
    bridge.press_buttons(["Right", "sleep 250", "Down", "sleep 250", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 400"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 400"])

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            run_away()
            continue
            
        print(f"Path step {idx}: At {pos}, sending {path[idx]}")
        walk_step(path[idx])
        
        new_pos = get_pos()
        if new_pos is None:
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                run_away()
                continue
                
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Blocked. Exiting path.")
                return False
        else:
            stuck_count = 0
            idx += 1
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"Transition occurred! Jumped to {new_pos}")
                    break
    return True

# 1. From (28, 2) to (6, 20) via Column 23 (50 steps)
path_to_ground = [
    "Left", "Left", "Left", "Left", "Left", # 5 steps Left to (23, 2)
    "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", # 16 steps Down to (23, 18)
    "Left", "Left", # 2 steps Left to (21, 18)
    "Up", # 1 step Up to (21, 17) (East Stairs)
    "Up", "Up", "Up", # 3 steps Up to (21, 14)
    "Left", "Left", "Left", "Left", "Left", "Left", # 6 steps Left to (15, 14)
    "Down", "Down", # 2 steps Down to (15, 16)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # 10 steps Left to (5, 16)
    "Right", # 1 step Right to (6, 16)
    "Down", "Down", "Down", # 3 steps Down to (6, 19) (West Stairs)
    "Down" # 1 step Down to (6, 20)
]

# 2. From (6, 20) to Gold Teeth Warp (13 steps)
path_to_teeth = [
    "Left", "Left", "Left", "Left", "Left", "Left",
    "Up", "Up", "Up", "Up", "Up", "Up", "Up"
]

# 3. From (29, 25) in Center to (19, 26) (11 steps)
path_center_teeth = [
    "Down",
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left"
]

# 4. From (19, 26) back to Warp (29, 25) (11 steps)
path_back_to_warp = [
    "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right",
    "Up"
]

# 5. From (0, 13) to Secret House (3, 8) (9 steps)
path_to_house = [
    "Up", "Up", "Up", "Up", "Up",
    "Right", "Right", "Right",
    "Up"
]

def run_all():
    print("=== STARTING THE ULTIMATE RETRIEVAL FROM (28, 2) ===")
    
    print("=== PHASE 4: Ascent & Descent via Column 23 ===")
    if not run_path(path_to_ground, check_warp=False):
        return False
        
    print("=== PHASE 5: Walk to Gold Teeth Warp ===")
    if not run_path(path_to_teeth, check_warp=True):
        return False
        
    print("=== PHASE 5b: Picking up Gold Teeth inside Center ===")
    if not run_path(path_center_teeth, check_warp=False):
        return False
        
    # Stand below Gold Teeth and interact
    pos = get_pos()
    print(f"Standing below Gold Teeth at {pos}. Interacting...")
    walk_step("Up") # Bumps into item, turning us UP
    time.sleep(0.5)
    bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
    print("Gold Teeth picked up!")
    
    print("=== PHASE 5c: Walking back to warp to Area 3 (West) ===")
    if not run_path(path_back_to_warp, check_warp=True):
        return False
        
    print("=== PHASE 6: Walking to Secret House ===")
    if not run_path(path_to_house, check_warp=True):
        return False
        
    print("Arrived inside Secret House! Coordinates:", get_pos())
    return True

if __name__ == "__main__":
    run_all()
