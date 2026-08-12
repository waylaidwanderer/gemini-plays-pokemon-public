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
    # We are currently at (18, 32) on the ground in Area 2 North
    
    # 1. Path to climb the Western Southern Plateau at (22, 23)
    path_to_climb = []
    path_to_climb.append("Up")       # to (18, 31)
    path_to_climb.extend(["Right"] * 4) # to (22, 31)
    path_to_climb.extend(["Up"] * 8)    # to (22, 23) (climb stairs)
    path_to_climb.extend(["Left"] * 6)  # to (16, 23) on Plateau
    path_to_climb.extend(["Down"] * 5)  # to (16, 28) on ground (descend stairs at 16, 27)

    # 2. Path on ground to northwest transition at (4, 36)
    path_to_transition = []
    path_to_transition.extend(["Left"] * 12) # to (4, 28)
    path_to_transition.extend(["Down"] * 8)  # to (4, 36) (transition!)

    # 3. Path in Area 3 West: To Secret House door at (3, 8)
    path_to_house = []
    path_to_house.append("Left")         # to (3, 0) (in case we land at 2,0)
    path_to_house.extend(["Down"] * 8)   # to (3, 8)
    path_to_house.append("Up")           # to enter Secret House!

    print("--- STAGE 1: Climbing and Descending Western Southern Plateau ---")
    if not run_path(path_to_climb, check_warp=False):
        return False
        
    print("--- STAGE 2: Walking Ground to Northwest Transition ---")
    if not run_path(path_to_transition, check_warp=True):
        return False
        
    print("--- STAGE 3: Walking northwest ground of Area 3 West to Secret House ---")
    if not run_path(path_to_house, check_warp=True):
        return False
        
    print("=== SUCCESS! INSIDE SECRET HOUSE ===")
    return True

if __name__ == "__main__":
    run_plateau()
