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
    print("Wild battle detected! Escaping...")
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
    
    # Wait for position to change
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is None:
            time.sleep(1.0)
            new_pos = get_pos()
            if new_pos is None:
                handle_battle()
                return None
            else:
                return new_pos
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
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(1.0)
            new_pos = get_pos()
            if new_pos is None:
                handle_battle()
                continue
            else:
                if check_warp:
                    dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                    if dist > 5:
                        print(f"SUCCESS! Transitioned to coordinates: {new_pos}")
                        break
                idx += 1
                continue
            
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Path blocked. Exiting path.")
                return False
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"SUCCESS! Transitioned to coordinates: {new_pos}")
                    break
            idx += 1
    return True

def go_back_to_area2():
    print("=== WALKING BACK TO AREA 2 (NORTH) FROM (16, 18) ===")
    pos = get_pos()
    print("Starting position:", pos)
    
    path = []
    # 1. Walk Left on the plateau to (6, 18)
    if pos == (16, 18):
        path.extend(["Left"] * 10) # to (6, 18)
        path.extend(["Down"] * 2)  # to (6, 20) (descends West Stairs)
        path.extend(["Right"] * 19) # to (25, 20)
        path.extend(["Up"] * 17)    # to (25, 3)
        path.append("Right")        # to (26, 3)
        path.extend(["Up"] * 3)     # warp to Area 2!
    else:
        print(f"Unexpected starting position: {pos}. Aligning...")
        return False
        
    print("Executing path...")
    if not run_path(path, check_warp=True):
        print("Failed to transition back!")
        return False
        
    print("Back in Area 2 North successfully!")
    return True

if __name__ == "__main__":
    go_back_to_area2()
