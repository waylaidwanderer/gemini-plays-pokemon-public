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

# Stage 4 from (14, 0) Ascent and Descent (56 steps)
path_stage4 = [
    "Down", # (14, 0) -> (14, 1) (1 step)
    "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", # (14, 1) -> (23, 1) (9 steps)
    "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", # (23, 1) -> (23, 18) (17 steps)
    "Left", "Left", # (23, 18) -> (21, 18) (2 steps)
    "Up", # (21, 18) -> (21, 17) (East Stairs) (1 step)
    "Up", "Up", "Up", # (21, 17) -> (21, 14) (3 steps)
    "Left", "Left", "Left", "Left", "Left", "Left", # (21, 14) -> (15, 14) (6 steps)
    "Down", "Down", # (15, 14) -> (15, 16) (2 steps)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # (15, 16) -> (5, 16) (10 steps)
    "Right", # (5, 16) -> (6, 16) (1 step)
    "Down", "Down", "Down", # (6, 16) -> (6, 19) (West Stairs) (3 steps)
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

def run_stage4():
    print("=== STARTING STAGE 4 (REVISED): Ascent and Descent from (14, 0) ===")
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
    run_stage4()
