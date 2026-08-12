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
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is not None and new_pos != pos:
            return new_pos
    return pos

def run_path(path):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            time.sleep(0.5)
            continue
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(0.5)
            continue
            
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Path blocked!")
                return False
        else:
            stuck_count = 0
            idx += 1
    return True

def main():
    print("=== LEAVING WARDEN'S AND WALKING TO POKEMON CENTER ===")
    
    # 1. Close Menu/PACK
    print("Closing PACK menu...")
    for _ in range(4):
        bridge.press_buttons(["B"])
        time.sleep(0.3)
        
    pos = get_pos()
    print("Position inside Warden's:", pos)
    
    # 2. Exit Warden's House
    if pos is not None and pos[1] <= 8:
        print("Walking Down to exit house...")
        path_exit = ["Down"] * 4
        if run_path(path_exit):
            print("Successfully exited Warden's House!")
            time.sleep(1.0)
            pos = get_pos()
            print("Position outside Warden's:", pos)
            
    # We should be at (27, 27) outside Warden's House
    if pos is not None and pos[0] == 27 and pos[1] == 27:
        # Route to Pokemon Center:
        # - Down 1 to (27, 28)
        # - Right 3 to (30, 28)
        # - Down 2 to (30, 30)
        # - Left 11 to (19, 30)
        # - Up 3 to (19, 27) (Pokemon Center door)
        # - Up 1 to enter!
        path_to_center = (
            ["Down"] +
            ["Right"] * 3 +
            ["Down"] * 2 +
            ["Left"] * 11 +
            ["Up"] * 4
        )
        if run_path(path_to_center):
            print("Successfully entered Pokemon Center!")
            time.sleep(1.5)
            pos = get_pos()
            print("Position inside Pokemon Center:", pos)
            
    # Inside Pokemon Center, we should land at the entrance mat (usually (3, 7) or similar)
    if pos is not None and pos[1] >= 5:
        # Walk to PC at (13, 4)
        # From entrance mat (3, 7):
        # - Up 3 to (3, 4)
        # - Right 10 to (13, 4)
        # If we landed at a different entrance coord, let's align
        path_to_pc = []
        if pos[1] > 4:
            path_to_pc.extend(["Up"] * (pos[1] - 4))
        if pos[0] < 13:
            path_to_pc.extend(["Right"] * (13 - pos[0]))
            
        print("Walking to PC...")
        if run_path(path_to_pc):
            print("Aligned in front of PC! Accessing...")
            # Access the PC
            bridge.press_buttons(["A"])
            time.sleep(0.8)
            bridge.press_buttons(["A"]) # Select "ACE's PC"
            time.sleep(0.8)
            bridge.press_buttons(["Down", "sleep 200", "A"]) # Select "ITEM STORAGE"
            time.sleep(0.8)
            bridge.press_buttons(["A"]) # Select "WITHDRAW ITEM"
            time.sleep(1.5) # Wait for PC item list
            print("PC item withdraw menu opened successfully!")

if __name__ == "__main__":
    main()
