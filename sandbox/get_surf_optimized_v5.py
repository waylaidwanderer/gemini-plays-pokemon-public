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

def handle_battle():
    print("Wild battle/interaction detected! Escaping...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 250"])
    bridge.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1200"])
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

def run_surf():
    # 1. Escape from active battle
    handle_battle()
    
    time.sleep(1.0)
    pos = get_pos()
    print("Oveworld coordinates after escape:", pos)
    if pos is None:
        print("Failed to get overworld position.")
        return False
        
    # In case escaping didn't land us at (6, 27), adjust to Row 31
    path_to_row31 = []
    if pos[1] < 31:
        path_to_row31.extend(["Down"] * (31 - pos[1]))
    elif pos[1] > 31:
        path_to_row31.extend(["Up"] * (pos[1] - 31))
        
    # Walk Left to Column 4
    if pos[0] > 4:
        path_to_row31.extend(["Left"] * (pos[0] - 4))
    elif pos[0] < 4:
        path_to_row31.extend(["Right"] * (4 - pos[0]))
        
    # Walk Down to (4, 36) to transition
    path_to_row31.extend(["Down"] * 5)
    
    print("--- STAGE 1: Transitioning to Area 3 West northwest ground ---")
    if not run_path(path_to_row31, check_warp=True):
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Landed in Area 3 West northwest ground at:", pos)
    
    # 2. To Secret House door at (3, 8)
    path_to_house = []
    if pos is not None and pos[0] == 2:
        path_to_house.append("Right")
    elif pos is not None and pos[0] == 4:
        path_to_house.append("Left")
        
    path_to_house.extend(["Down"] * 8)   # to (3, 8)
    path_to_house.append("Up")           # to enter Secret House!
    
    print("--- STAGE 2: Walking to Secret House ---")
    if not run_path(path_to_house, check_warp=True):
        return False
        
    print("=== SUCCESS! INSIDE SECRET HOUSE ===")
    return True

if __name__ == "__main__":
    run_surf()
