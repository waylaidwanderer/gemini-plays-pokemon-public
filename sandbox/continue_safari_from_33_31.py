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

# Area 2 (North) at (33, 31) to Area 3 (West) warp (20, 36)
path_stage1 = [
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
    "Down", "Down",
    "Left", "Left",
    "Down", "Down", "Down"
]

# Area 3 (West) - Climb Plateau and reach West Side (6, 20)
path_stage2 = [
    "Down",
    "Right", "Right", "Right", "Right", "Right", "Right", "Right",
    "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
    "Up",
    "Up", "Up", "Up",
    "Left", "Left", "Left", "Left", "Left", "Left",
    "Down", "Down",
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
    "Right",
    "Down", "Down", "Down",
    "Down"
]

def run_remaining():
    print("=== STARTING STAGE 1 (Area 2 to Area 3) ===")
    if not run_path(path_stage1, check_warp=True):
        return False
        
    print("=== STARTING STAGE 2 (Area 3 Plateau Ascent & Descent) ===")
    if not run_path(path_stage2, check_warp=False):
        return False
        
    print("Stage 1 and Stage 2 complete! Coordinates:", get_pos())
    return True

if __name__ == "__main__":
    run_remaining()
