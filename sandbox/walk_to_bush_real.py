# Script to walk from (1, 21) to (26, 12) in Fuchsia City to cut the bush
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

PATH_TO_BUSH = [
    # Walk Right along Row 21 to Column 24
    "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right",
    "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right",
    "Right", "Right", "Right", # to (24, 21)
    
    # Walk Up Column 24 to Row 16
    "Up", "Up", "Up", "Up", "Up", # to (24, 16)
    
    # Walk Left to Column 22
    "Left", "Left", # to (22, 16)
    
    # Walk Up Column 22 to Row 14
    "Up", "Up", # to (22, 14)
    
    # Walk Right along Row 14 to Column 26
    "Right", "Right", "Right", "Right", # to (26, 14)
    
    # Walk Up Column 26 to Row 12 (below bush at 26, 13)
    "Up", "Up" # to (26, 12)
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
    pos = get_pos()
    print("Starting at:", pos)
    
    if pos == (1, 21):
        run_path(PATH_TO_BUSH)
        time.sleep(2.0)
        
    pos = get_pos()
    print("Final Position:", pos)

if __name__ == "__main__":
    main()
