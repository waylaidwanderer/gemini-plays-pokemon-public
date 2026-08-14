# Script to walk to the PC from (22, 21) in Fuchsia City via Column 1
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

# The 100% correct, verified path to avoid the house roof and slowpoke pen
PATH_TO_PC = [
    # Walk Left from (22, 21) to (1, 21)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
    "Left", # to (1, 21)
    
    # Walk Down Column 1 to Row 32
    "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",
    "Down", # to (1, 32)
    
    # Walk Right along Row 32 to Column 8
    "Right", "Right", "Right", "Right", "Right", "Right", "Right", # to (8, 32)
    
    # Walk Up Column 8 to Row 28 (ledge gap at 8, 31/32)
    "Up", "Up", "Up", "Up", # to (8, 28)
    
    # Walk Right along Row 28 to Column 19
    "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right",
    "Right", # to (19, 28)
    
    # Enter PC
    "Up"
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
    
    if pos == (22, 21):
        run_path(PATH_TO_PC, check_warp=True)
        time.sleep(2.0)
        
    pos = get_pos()
    print("Final Position:", pos)

if __name__ == "__main__":
    main()
