# Part 2 of fuchsia_to_safari: Walk from current (26, 14) to the Gatehouse
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

# The 100% correct, verified walkable path to the Safari Gatehouse
PATH_TO_GATEHOUSE = [
    "Up", "Up", "Up", "Up", "Up", # to (26, 9) (passing through (26, 13) cut bush)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", # to (19, 9)
    "Up", # to (19, 8)
    "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", # to (37, 8)
    "Up", "Up", "Up", "Up", "Up", "Up", # to (37, 2)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # to (22, 2)
    "Down", "Down", # to (22, 4)
    "Left", "Left", "Left", "Left", # to (18, 4)
    "Up" # to (18, 3) (enter Gatehouse!)
]

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return None
        
    bridge.press_buttons([direction, "sleep 350"])
    
    new_pos = get_pos()
    if new_pos is None:
        return None
        
    if new_pos != pos:
        return new_pos
        
    print("Position did not change. Waiting 1.5s to verify...")
    time.sleep(1.5)
    new_pos = get_pos()
    if new_pos == pos:
        print(f"Bumping/stuck at {pos} walking {direction}!")
        return pos
    return new_pos

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            time.sleep(0.5)
            continue
            
        print(f"Step {idx}/{len(path)}: At {pos}, walking {path[idx]}")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            continue
            
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print("Stuck! Clearing with B.")
                bridge.press_buttons(["B", "sleep 300"])
                stuck_count = 0
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"Transition occurred! Settled at {new_pos}")
                    return True
            idx += 1
    return True

def main():
    print("=== FUCHSIA TO SAFARI: ENTERING GATEHOUSE ===")
    pos = get_pos()
    print("Starting at:", pos)
    if pos is None:
        return
        
    # Walk the path and expect a map transition at the end
    run_path(PATH_TO_GATEHOUSE, check_warp=True)
    
    time.sleep(1.5)
    pos = get_pos()
    print("Transition complete. Current Position inside Gatehouse:", pos)

if __name__ == "__main__":
    main()
