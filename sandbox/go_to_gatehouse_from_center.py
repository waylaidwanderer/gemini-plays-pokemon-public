import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        time.sleep(0.1)
    return None

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return None
        
    bridge.press_buttons([direction])
    
    # Wait for position to change
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is not None and new_pos != pos:
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            if check_warp:
                print("Transition occurred (pos is None)!")
                return True
            time.sleep(0.5)
            continue
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                if check_warp:
                    print("Transition occurred (pos is None after retry)!")
                    return True
                continue
                
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print(f"Blocked at {pos}! Exiting path.")
                return False
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"Transition occurred! New pos: {new_pos}")
                    break
            idx += 1
    return True

def main():
    print("=== NAVIGATING FROM (1, 16) TO SAFARI GATEHOUSE ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos != (1, 16):
        print("Not at starting position (1, 16)!")
        return
        
    # 1. Walk Down to Row 21 -> (1, 21)
    # 2. Walk Right to Column 22 -> (22, 21)
    # 3. Walk Up to Row 14 -> (22, 14)
    # 4. Walk Right to Column 26 -> (26, 14)
    escape_path = (
        ["Down"] * 5 +
        ["Right"] * 21 +
        ["Up"] * 7 +
        ["Right"] * 4
    )
    
    if not run_path(escape_path):
        print("Failed to reach the cut-able bush!")
        return
        
    print("At (26, 14). Facing UP...")
    bridge.press_buttons(["Up", "sleep 300"])
    
    print("Using CUT...")
    cut_sequence = [
        "Start", "sleep 600",
        "Up", "Up", "Up", "Up", "Up", "Up", "sleep 300", # Align to POKEDEX
        "Down", "A", "sleep 1000",                       # Select POKEMON
        "Down", "A", "sleep 1000",                       # Select Paras (2nd slot)
        "A", "sleep 1500",                               # Select CUT
        "B", "sleep 500", "B", "sleep 500"               # Close any lingering menus
    ]
    bridge.press_buttons(cut_sequence)
    time.sleep(2.0)
    
    pos = get_pos()
    print("Position after CUT attempt:", pos)
    
    # Path from (26, 14) through the cut bush to the Safari Gatehouse
    path_from_bush = (
        ["Up"] * 5 +                                                      # to (26, 9)
        ["Left"] * 7 +                                                     # to (19, 9)
        ["Up"] * 1 +                                                      # to (19, 8)
        ["Right"] * 18 +                                                   # to (37, 8)
        ["Up"] * 6 +                                                       # to (37, 2)
        ["Left"] * 19 +                                                    # to (18, 2)
        ["Down"]                                                          # to (18, 3) (Gatehouse warp)
    )
    
    if run_path(path_from_bush, check_warp=True):
        print("Successfully reached Safari Zone Gatehouse!")
        time.sleep(1.0)
        pos = get_pos()
        print("Inside Gatehouse position:", pos)
    else:
        print("Failed to reach Safari Zone Gatehouse from bush!")

if __name__ == "__main__":
    main()
