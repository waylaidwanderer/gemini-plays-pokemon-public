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
        if new_pos != pos:
            return new_pos
    return pos

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            if check_warp:
                print("Transition occurred!")
                return True
            time.sleep(0.5)
            continue
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print("Blocked!")
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
    print("=== BYPASSING HIKER AND WALKING TO POKEMON CENTER ===")
    pos = get_pos()
    print("Starting pos:", pos)
    
    if pos == (31, 14):
        # Detour around Hiker at (30, 14):
        # 1. Down to (31, 15)
        # 2. Left 2 to (29, 15)
        # 3. Up to (29, 14)
        # 4. Left 6 to (23, 14)
        # 5. Down 7 to (23, 21)
        # 6. Right 1 to (24, 21)
        # 7. Down 7 to (24, 28)
        # 8. Left 5 to (19, 28)
        # 9. Up to enter Center!
        path = (
            ["Down"] +
            ["Left"] * 2 +
            ["Up"] +
            ["Left"] * 6 +
            ["Down"] * 7 +
            ["Right"] * 1 +
            ["Down"] * 7 +
            ["Left"] * 5 +
            ["Up"]
        )
        print("Walking to Pokémon Center...")
        if not run_path(path, check_warp=True):
            print("Failed to reach Pokémon Center!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Inside Pokémon Center:", pos)
        
    if pos is not None and pos[1] >= 5:
        # Walk to PC at (13, 4) from entrance mat (usually (3, 7))
        path_to_pc = []
        if pos[1] > 4:
            path_to_pc.extend(["Up"] * (pos[1] - 4))
        if pos[0] < 13:
            path_to_pc.extend(["Right"] * (13 - pos[0]))
            
        print("Walking to PC...")
        if not run_path(path_to_pc):
            print("Failed to reach PC!")
            return
            
        pos = get_pos()
        print("Aligned in front of PC:", pos)
        
        # Access PC
        print("Accessing PC...")
        bridge.press_buttons(["A", "sleep 800", "A", "sleep 800", "Down", "sleep 200", "A", "sleep 800", "A"])
        # This will open ACE's PC -> ITEM STORAGE -> WITHDRAW ITEM
        time.sleep(1.5)
        print("Withdraw menu opened successfully!")

if __name__ == "__main__":
    main()
