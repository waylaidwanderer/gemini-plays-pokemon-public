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
                # If coordinate changes significantly, warp happened!
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"Transition occurred! New pos: {new_pos}")
                    break
            idx += 1
    return True

def main():
    print("=== EXECUTING SYSTEMATIC ROUTE TO SAFARI ZONE ===")
    
    pos = get_pos()
    print("Initial position inside Warden's House:", pos)
    if pos is None:
        print("Failed to get starting position!")
        return
        
    # 1. Exit the Warden's House
    if pos == (2, 4):
        print("Walking to the Warden's House exit...")
        exit_path = ["Right", "Right", "Down", "Down", "Down", "Down", "Down"]
        if not run_path(exit_path, check_warp=True):
            print("Failed to exit Warden's House!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Position after exiting house:", pos)
        
    # 2. Walk the detour route in Fuchsia City to the Safari Gatehouse
    # We should be around (27, 28) outside the house
    if pos is not None and abs(pos[0] - 27) <= 2 and abs(pos[1] - 28) <= 2:
        print("Walking Fuchsia City detour to Gatehouse...")
        # Recalculate based on current exact coordinates:
        # Let's align to (27, 28) first if not exact, or just run the relative path.
        # Relative path from (27, 28):
        fuchsia_path = (
            ["Right"] * 3 +                                                    # to (30, 28)
            ["Down"] * 2 +                                                    # to (30, 30)
            ["Left"] * 6 +                                                    # to (24, 30)
            ["Up"] * 9 +                                                      # to (24, 21)
            ["Left"] * 1 +                                                    # to (23, 21)
            ["Up"] * 7 +                                                      # to (23, 14)
            ["Right"] * 6 +                                                   # to (29, 14)
            ["Down"] * 1 +                                                    # to (29, 15)
            ["Right"] * 2 +                                                   # to (31, 15)
            ["Up"] * 1 +                                                      # to (31, 14)
            ["Right"] * 6 +                                                   # to (37, 14)
            ["Up"] * 12 +                                                     # to (37, 2)
            ["Left"] * 19 +                                                   # to (18, 2)
            ["Down"]                                                          # to (18, 3) (Gatehouse warp)
        )
        if not run_path(fuchsia_path, check_warp=True):
            print("Failed to reach Gatehouse!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Position inside Gatehouse:", pos)
        
    # 3. Enter the Gatehouse and talk to clerk
    if pos is not None and abs(pos[0] - 4) <= 1 and abs(pos[1] - 5) <= 1:
        print("Navigating inside Gatehouse to the counter...")
        gatehouse_path = ["Up", "Up"]
        if not run_path(gatehouse_path):
            print("Failed to align in front of clerk counter!")
            return
            
        pos = get_pos()
        print("Aligned in front of clerk:", pos)
        
        # We should be at (4, 3) facing UP. Let's make sure we face UP
        bridge.press_buttons(["Up", "sleep 300"])
        
        print("Talking to clerk...")
        bridge.press_buttons(["A", "sleep 1000"])
        
        # Dialogue sequence to buy ticket and enter
        for i in range(8):
            print(f"Dialogue step {i+1}...")
            bridge.press_buttons(["A", "sleep 1200"])
            
        time.sleep(1.0)
        pos = get_pos()
        print("Position after entry dialogue:", pos)
        
        if pos is None:
            time.sleep(1.0)
            pos = get_pos()
            
        if pos == (15, 25):
            print("Successfully entered the Safari Zone Center!")
        else:
            print("Warp did not place us at (15, 25). Current pos:", pos)

if __name__ == "__main__":
    main()
