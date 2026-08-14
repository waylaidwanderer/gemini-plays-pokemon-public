# Script to cut the bush and walk to the PC
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

PATH_TO_PC = [
    "Left", "Left", "Left", # to (23, 14)
    "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", # to (23, 28)
    "Left", "Left", "Left", "Left", # to (19, 28)
    "Up" # enter PC
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

def use_cut():
    print("Using CUT on bush...")
    # Open menu
    bridge.press_buttons(["Start", "sleep 450"])
    # Reset menu position to POKEDEX
    bridge.press_buttons(["Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150", "Up", "sleep 150"])
    # Move to POKEMON and select
    bridge.press_buttons(["Down", "sleep 150", "A", "sleep 800"])
    # Move to TRUFFLE (slot 2) and select
    bridge.press_buttons(["Down", "sleep 200", "A", "sleep 800"])
    # Move to CUT (3rd option) and select
    bridge.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "A", "sleep 2500"])
    # Press B to clear remaining boxes
    bridge.press_buttons(["B", "sleep 400", "B", "sleep 400"])

def main():
    pos = get_pos()
    print("Current Position:", pos)
    
    if pos == (26, 12):
        use_cut()
        # Move down to (26, 13) after cut
        run_path(["Down"])
        
    pos = get_pos()
    print("Moved past bush:", pos)
    
    if pos == (26, 13):
        run_path(["Down"])
        
    pos = get_pos()
    print("At (26, 14):", pos)
    
    if pos == (26, 14):
        run_path(PATH_TO_PC, check_warp=True)
        time.sleep(2.0)
        
    pos = get_pos()
    print("Position at the end:", pos)

if __name__ == "__main__":
    main()
