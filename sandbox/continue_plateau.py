import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_battle():
    print("Wild battle detected! Escaping...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 200"])
    bridge.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1200"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction])
    
    # Wait for position to change (up to 750 ms)
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is None:
            return None
        if new_pos != pos:
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    handle_battle()
    # Retry walking
    print(f"Retrying: walking {direction}...")
    bridge.press_buttons([direction])
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is None:
            return None
        if new_pos != pos:
            return new_pos
    return pos

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        print(f"Path step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                if check_warp:
                    print("SUCCESS! Transition occurred!")
                    return True
                handle_battle()
                continue
                
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Path blocked. Exiting path.")
                return False
        else:
            stuck_count = 0
            idx += 1
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"SUCCESS! Transitioned to coordinates: {new_pos}")
                    break
    return True

def run_plateau():
    # We are currently at (26, 0) inside Area 3 West
    
    # 1. Path to transition back to Area 2 North
    path_to_area2 = ["Up"] # to Row -1 of Area 3 (West) which transitions to Area 2 North at (8, 35) or (9, 35)

    # 2. Path in Area 2 North to southwest transition at (4, 36)
    path_area2 = []
    path_area2.extend(["Left"] * 5)  # to (4, 35) (or 5 Left from 9,35)
    path_area2.append("Down")        # to (4, 36) (transition!)

    # 3. Path inside northwest ground of Area 3 West: To Secret House door at (3, 8)
    path_to_house = []
    path_to_house.append("Left")         # to (3, 0) (in case we land at 2,0)
    path_to_house.extend(["Down"] * 8)   # to (3, 8)
    path_to_house.append("Up")           # to enter Secret House!

    print("--- STAGE 1: Transitioning back to Area 2 North ---")
    if not run_path(path_to_area2, check_warp=True):
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Landing coordinates in Area 2 North:", pos)
    
    # Adjust left steps based on actual landing position
    # (usually we land at 8,35 or 9,35)
    left_steps = 5
    if pos is not None and pos[0] == 8:
        left_steps = 4
        
    path_area2_adjusted = ["Left"] * left_steps + ["Down"]

    print("--- STAGE 2: Walking Area 2 North to Northwest Transition ---")
    if not run_path(path_area2_adjusted, check_warp=True):
        return False
        
    print("--- STAGE 3: Walking northwest ground of Area 3 West to Secret House ---")
    if not run_path(path_to_house, check_warp=True):
        return False
        
    print("=== SUCCESS! INSIDE SECRET HOUSE ===")
    return True

if __name__ == "__main__":
    run_plateau()
