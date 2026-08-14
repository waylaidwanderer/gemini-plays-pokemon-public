# Corrected Part 2A of fuchsia_to_safari: Walk from current (24, 16) to (19, 8)
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

# Coordinates from current (24, 16) to (19, 8)
# We are currently at (24, 16)
PATH_2A = [
    "Left", "Left", # to (22, 16)
    "Up", "Up",     # to (22, 14)
    "Right", "Right", "Right", "Right", # to (26, 14)
    "Up", "Up", "Up", "Up", "Up", # to (26, 9) (passing through (26, 13) cut bush)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", # to (19, 9)
    "Up" # to (19, 8)
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

def run_path(path):
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
            idx += 1
    return True

def main():
    print("=== FUCHSIA TO SAFARI: PART 2A (CORRECTED) ===")
    pos = get_pos()
    print("Starting at:", pos)
    if pos is None:
        return
        
    run_path(PATH_2A)
    
    pos = get_pos()
    print("Part 2A finished! Current Position:", pos)

if __name__ == "__main__":
    main()
