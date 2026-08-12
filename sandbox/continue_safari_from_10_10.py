import bridge
import time
import sys

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    # First press B multiple times to dismiss text
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
    # Move to RUN and select (Safari Zone escape)
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
                # Check for warp
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"Transition occurred! Jumped to {new_pos}")
                    break
    return True

# Definition of the remaining paths:
# Phase 2 remaining: Area 1 (East) at (10, 10) to Area 2 (North)
path_area1_from_10_10 = [
    "Up", "Up",                     # (10, 10) -> (10, 8)
    "Right", "Right",               # (10, 8) -> (12, 8)
    "Up", "Up",                     # (12, 8) -> (12, 6) (stairs)
    "Right", "Right", "Right", "Right", "Right",  # (12, 6) -> (17, 6) (5 steps)
    "Down", "Down",                 # (17, 6) -> (17, 8) (stairs)
    "Right", "Right", "Right",      # (17, 8) -> (20, 8)
    "Up", "Up", "Up", "Up", "Up",   # (20, 8) -> (20, 3) (5 steps)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # (20, 3) -> (7, 3) (13 steps)
    "Down", "Down",                 # (7, 3) -> (7, 5)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left" # (7, 5) -> warp (8 steps)
]

# Phase 3: Area 2 (North) to Area 3 (West) at (14, 0) via (20, 36)
path_area2 = [
    # Warp in at (39, 31). Walk Left to (22, 31) (17 steps Left)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
    # Walk Down to (22, 33) (2 steps Down)
    "Down", "Down",
    # Walk Left to (20, 33) (2 steps Left)
    "Left", "Left",
    # Walk Down to (20, 36) (3 steps Down - Warp!)
    "Down", "Down", "Down"
]

# Phase 4: Area 3 (West) - Climb Plateau and reach West Side
path_area3_ascent = [
    # Warp in at (14, 0). Walk Down to (14, 1)
    "Down",
    # Walk Right to (21, 1) (7 steps Right)
    "Right", "Right", "Right", "Right", "Right", "Right", "Right",
    # Walk Down Column 21 to (21, 18) (17 steps Down)
    "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
    # Walk UP to (21, 17) (climb East Stairs onto Plateau!)
    "Up",
    # Walk UP to (21, 14) (3 steps Up)
    "Up", "Up", "Up",
    # Walk Left to (15, 14) (6 steps Left)
    "Left", "Left", "Left", "Left", "Left", "Left",
    # Walk Down to (15, 16) (2 steps Down)
    "Down", "Down",
    # Walk Left to (5, 16) (10 steps Left)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
    # Walk Right to (6, 16) (1 step Right)
    "Right",
    # Walk Down to (6, 19) (3 steps Down, stairs)
    "Down", "Down", "Down",
    # Walk Down to (6, 20) (descend to western ground level!)
    "Down"
]

# Phase 5: Retrieve the Gold Teeth
path_to_teeth = [
    # Walk Left to (0, 20) (6 steps Left)
    "Left", "Left", "Left", "Left", "Left", "Left",
    # Walk Up Column 0 to Row 13 (7 steps Up - Transition!)
    "Up", "Up", "Up", "Up", "Up", "Up", "Up"
]

path_center_teeth = [
    "Down", # To Row 26 (29, 26)
    # Walk Left to Column 19 (10 steps Left)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left"
]

path_back_to_warp = [
    # Walk Right to Column 29 (10 steps Right)
    "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right",
    "Up" # To warp (29, 25) -> transitions back to Area 3 (West) at (0, 13)
]

# Phase 6: Retrieve Surf
path_to_house = [
    # Walk Up Column 0 to Row 8 (5 steps Up)
    "Up", "Up", "Up", "Up", "Up",
    # Walk Right to Column 3 (3 steps Right)
    "Right", "Right", "Right",
    # Walk Up to (3, 8) (enter Secret House!)
    "Up"
]

def run_remaining():
    print("=== STARTING REMAINING SAFARI RUN FROM AREA 1 (EAST) (10, 10) ===")
    
    print("=== PHASE 2 (FIXED): Area 1 (East) to Area 2 (North) ===")
    if not run_path(path_area1_from_10_10, check_warp=True):
        return False

    print("=== PHASE 3: Area 2 (North) to Area 3 (West) ===")
    if not run_path(path_area2, check_warp=True):
        return False

    print("=== PHASE 4: Area 3 (West) Ascent and Descent ===")
    if not run_path(path_area3_ascent, check_warp=False):
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
    walk_step("Up") # Bumps into item, facing us UP
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
    run_remaining()
