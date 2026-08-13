# Part 1 of fuchsia_to_safari: Exit PC, Pokémon Center, and walk to (1, 21)
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

# Coordinates from (19, 27) inside PC, to (1, 21) in Fuchsia City
WALK_PATH = [
    # PC Exit
    "Down", "Down", "Down", "A", "sleep 800", # select LOG OFF on ACE's PC
    "Down", "Down", "A", "sleep 800",       # select LOG OFF on main PC boot menu
    "Down", "Down", "Down", "Down", "sleep 800", # exit PC to door mat (3, 7) - wait, from (13, 4) to door mat at (3, 7) is: Left 10, Down 3!
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
    print("=== FUCHSIA TO SAFARI: PART 1 ===")
    
    # 1. Exit PC menu
    print("Logging off PC...")
    # Select LOG OFF on ACE's PC
    bridge.press_buttons(["Down", "sleep 150", "Down", "sleep 150", "Down", "sleep 150", "A", "sleep 1000"])
    # Press B to exit PC entirely
    bridge.press_buttons(["B", "sleep 1000"])
    
    # 2. Walk to PC exit door mat (3, 7)
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
    # Walk to (1, 21)
    if pos is not None and pos[0] == 19 and pos[1] == 28:
        path_to_corner = (
            ["Left"] * 11 +  # to (8, 28)
            ["Down"] * 4 +   # to (8, 32) (ledge jump)
            ["Left"] * 7 +   # to (1, 32)
            ["Up"] * 11      # to (1, 21)
        )
        if not run_path(path_to_corner):
            return
            
    pos = get_pos()
    print("Part 1 finished! Current Position:", pos)

if __name__ == "__main__":
    main()
