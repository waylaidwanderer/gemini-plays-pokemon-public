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

# Stage 2a from (15, 24) to (8, 22) (23 steps)
path_stage2a = [
    "Right", "Right", "Right", "Right", "Right", # (15, 24) -> (20, 24) (5 steps)
    "Up", "Up", "Up", # (20, 24) -> (20, 21) (3 steps)
    "Up", # (20, 21) -> (20, 20) (climb Southern Plateau) (1 step)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # (20, 20) -> (12, 20) (8 steps)
    "Down", "Down", # descend stairs to (12, 22) (2 steps)
    "Left", "Left", "Left", "Left" # (12, 22) -> (8, 22) (4 steps)
]

# Stage 2b: Area 1 (East) Northern Plateau Crossing (27 steps)
path_stage2b = [
    "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", # (8, 22) -> (8, 7) (15 steps)
    "Right", "Right", "Right", "Right", # (8, 7) -> (12, 7) (4 steps)
    "Up", # climb stairs to (12, 6)
    "Right", "Right", "Right", "Right", "Right", # (12, 6) -> (17, 6) (5 steps)
    "Down", "Down" # descend stairs to (17, 8) (2 steps)
]

# Stage 2c: Area 1 (East) to Area 2 (North) transition (31 steps)
path_stage2c = [
    "Right", "Right", "Right", # (17, 8) -> (20, 8) (3 steps)
    "Up", "Up", "Up", "Up", "Up", # (20, 8) -> (20, 3) (5 steps)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # (20, 3) -> (7, 3) (13 steps)
    "Down", "Down", # (7, 3) -> (7, 5) (2 steps)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left" # (7, 5) -> warp (8 steps)
]

# Stage 3: Area 2 (North) to Area 3 (West) at (27, 0) via (9, 36) (35 steps)
path_stage3 = [
    # Warp in at (39, 31). Walk Left to (22, 31) (17 steps Left)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
    # Walk Down to (22, 33) (2 steps Down)
    "Down", "Down",
    # Walk Left to (9, 33) (13 steps Left)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
    # Walk Down to (9, 36) (3 steps Down - Warp to (27, 0) in Area 3!)
    "Down", "Down", "Down"
]

# Stage 4: Area 3 (West) Ascent and Descent (54 steps)
path_stage4 = [
    "Right", "Right", # (27, 0) -> (29, 0) (2 steps)
    "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", # (29, 0) -> (29, 11) (11 steps)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", # (29, 11) -> (22, 11) (7 steps)
    "Down", "Down", "Down", "Down", "Down", "Down", "Down", # (22, 11) -> (22, 18) (7 steps)
    "Left", # (22, 18) -> (21, 18) (1 step)
    "Up", # (21, 18) -> (21, 17) (East Stairs)
    "Up", "Up", "Up", # (21, 17) -> (21, 14) (3 steps)
    "Left", "Left", "Left", "Left", "Left", "Left", # (21, 14) -> (15, 14) (6 steps)
    "Down", "Down", # (15, 14) -> (15, 16) (2 steps)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # (15, 16) -> (5, 16) (10 steps)
    "Right", # (5, 16) -> (6, 16) (1 step)
    "Down", "Down", "Down", # (6, 16) -> (6, 19) (West Stairs)
    "Down" # (6, 19) -> (6, 20) (1 step)
]

# Stage 5: Retrieve the Gold Teeth (35 steps)
path_stage5_to_teeth = [
    # Walk Left to (0, 20) (6 steps Left)
    "Left", "Left", "Left", "Left", "Left", "Left",
    # Walk Up Column 0 to Row 13 (7 steps Up - Warp to Center!)
    "Up", "Up", "Up", "Up", "Up", "Up", "Up"
]

path_stage5_center = [
    "Down", # To Row 26 (29, 26)
    # Walk Left to Column 19 (10 steps Left)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left"
]

path_stage5_back = [
    # Walk Right to Column 29 (10 steps Right)
    "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right",
    "Up" # To warp (29, 25) -> transitions back to Area 3 (West) at (0, 13)
]

# Stage 6: Retrieve Surf (9 steps)
path_stage6 = [
    # Walk Up Column 0 to Row 8 (5 steps Up)
    "Up", "Up", "Up", "Up", "Up",
    # Walk Right to Column 3 (3 steps Right)
    "Right", "Right", "Right",
    # Walk Up to (3, 8) (enter Secret House!)
    "Up"
]

def run_stage1():
    print("=== STARTING STAGE 1: Center to Area 1 (East) ===")
    return run_path(path_stage1, check_warp=True)

def run_stage2a():
    print("=== STARTING STAGE 2a: Southern Plateau Crossing ===")
    return run_path(path_stage2a, check_warp=False)

def run_stage2b():
    print("=== STARTING STAGE 2b: Northern Plateau Crossing ===")
    return run_path(path_stage2b, check_warp=False)

def run_stage2c():
    print("=== STARTING STAGE 2c: Area 1 (East) to Area 2 (North) ===")
    return run_path(path_stage2c, check_warp=True)

def run_stage3():
    print("=== STARTING STAGE 3: Area 2 (North) to Area 3 (West) ===")
    return run_path(path_stage3, check_warp=True)

def run_stage4():
    print("=== STARTING STAGE 4: Area 3 (West) Ascent and Descent ===")
    return run_path(path_stage4, check_warp=False)

def run_stage5():
    print("=== STARTING STAGE 5: Walk to Gold Teeth Warp ===")
    if not run_path(path_stage5_to_teeth, check_warp=True):
        return False
        
    print("=== STARTING STAGE 5b: Picking up Gold Teeth inside Center ===")
    if not run_path(path_stage5_center, check_warp=False):
        return False
        
    # Stand below Gold Teeth and interact
    pos = get_pos()
    print(f"Standing below Gold Teeth at {pos}. Interacting...")
    walk_step("Up") # Bumps into item, turning us UP
    time.sleep(0.5)
    bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
    print("Gold Teeth picked up!")
    
    print("=== STARTING STAGE 5c: Walking back to warp to Area 3 (West) ===")
    return run_path(path_stage5_back, check_warp=True)

def run_stage6():
    print("=== STARTING STAGE 6: Walking to Secret House ===")
    return run_path(path_stage6, check_warp=True)

if __name__ == "__main__":
    # Default execution
    run_stage2a()
