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

def run_speedrun():
    # Dismiss the "Got away safely!" screen
    print("Dismissing 'Got away safely!' screen...")
    bridge.press_buttons(["B", "sleep 500"])
    
    # 1. Path in Area 1 East: Navigate the 100% walkable spiral route to Area 2 North
    # Starting at current position (20, 24)
    path_area1 = []
    path_area1.extend(["Up"] * 4)      # to (20, 20) (climb Southern Plateau)
    path_area1.extend(["Left"] * 8)    # to (12, 20) (walk West on plateau)
    path_area1.extend(["Down"] * 2)    # to (12, 22) (descend Southern Plateau stairs)
    path_area1.extend(["Left"] * 3)    # to (9, 22)
    path_area1.extend(["Up"] * 14)     # to (9, 8) (walk UP Column 9)
    path_area1.extend(["Right"] * 3)   # to (12, 8)
    path_area1.extend(["Up"] * 2)      # to (12, 6) (climb Northern Plateau at (12, 7))
    path_area1.extend(["Right"] * 5)   # to (17, 6) (walk East on plateau)
    path_area1.extend(["Down"] * 2)    # to (17, 8) (descend Northern Plateau stairs)
    path_area1.extend(["Right"] * 3)   # to (20, 8)
    path_area1.extend(["Up"] * 3)      # to (20, 5)
    path_area1.extend(["Left"] * 20)   # to (0, 5) (transition!)

    # 2. Path in Area 2 North: To Area 3 West northwest ground at (4, 36)
    path_area2 = []
    path_area2.extend(["Left"] * 35)  # to (4, 31)
    path_area2.extend(["Down"] * 5)   # to (4, 36) (transition!)

    # 3. Path in Area 3 West: To Secret House door at (3, 8)
    path_area3 = []
    path_area3.append("Left")         # to (3, 0)
    path_area3.extend(["Down"] * 8)   # to (3, 8)
    path_area3.append("Up")           # to enter Secret House!

    print("--- STAGE 2: Walking Area 1 East to Area 2 North ---")
    if not run_path(path_area1, check_warp=True):
        return False
        
    print("--- STAGE 3: Walking Area 2 North to Area 3 West northwest ground ---")
    if not run_path(path_area2, check_warp=True):
        return False
        
    print("--- STAGE 4: Walking Area 3 West to Secret House ---")
    if not run_path(path_area3, check_warp=True):
        return False
        
    print("--- INSIDE SECRET HOUSE ---")
    return True

if __name__ == "__main__":
    run_speedrun()
