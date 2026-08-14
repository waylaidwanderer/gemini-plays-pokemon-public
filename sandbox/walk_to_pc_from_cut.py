# Script to exit the PC, exit the Pokemon Center, and walk back to the Safari Gatehouse
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

# Path from (19, 28) outside Pokemon Center to (26, 12) in Fuchsia City
PATH_TO_BUSH = [
    # Walk Left to Column 8
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # to (8, 28)
    # Walk Down to Row 32 (ledge jump at (8, 31/32))
    "Down", "Down", "Down", "Down", # to (8, 32)
    # Walk Left to Column 1
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", # to (1, 32)
    # Walk Up Column 1 to Row 21
    "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", # to (1, 21)
    # Walk Right along Row 21 to Column 24
    "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right",
    "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right",
    "Right", "Right", "Right", # to (24, 21)
    # Walk Up Column 24 to Row 16 (below the Rhydon statue at 24, 15)
    "Up", "Up", "Up", "Up", "Up", # to (24, 16)
    # Walk Left to Column 22
    "Left", "Left", # to (22, 16)
    # Walk Up Column 22 to Row 14
    "Up", "Up", # to (22, 14)
    # Walk Right along Row 14 to Column 26
    "Right", "Right", "Right", "Right", # to (26, 14)
    # Walk Up Column 26 to Row 12 (below the bush at 26, 13)
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
    # 1. Exit PC
    print("Exiting PC...")
    bridge.press_buttons(["B", "sleep 1000"])
    
    # 2. Walk to door mat (3, 7)
    pos = get_pos()
    print("PC Exit complete. Position:", pos)
    
    # Walk to (3, 7)
    path_to_mat = [
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # Left 10 to column 3
        "Down", "Down", "Down" # Down 3 to row 7
    ]
    if not run_path(path_to_mat):
        return
        
    # Exit Pokémon Center
    print("Exiting Pokemon Center...")
    bridge.press_buttons(["Down", "sleep 2000"]) # transition out
    
    pos = get_pos()
    print("Emerged in Fuchsia City:", pos)
    
    # We should be at (19, 28) in Fuchsia City!
    # Let's chunk the path to avoid 100 button sequence limit
    if pos == (19, 28):
        # We will walk the first 30 steps of PATH_TO_BUSH to reach (1, 21) or similar
        print("Walking Phase 1 of path...")
        part1 = PATH_TO_BUSH[:33] # Up to (1, 21)
        if run_path(part1):
            print("Successfully reached (1, 21)!")
            
    pos = get_pos()
    print("End of script. Position reached:", pos)

if __name__ == "__main__":
    main()
