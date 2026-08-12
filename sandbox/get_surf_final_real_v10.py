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
                    print(f"SUCCESS! Transitioned to: {new_pos}")
                    break
            idx += 1
    return True

def walk_to_secret_house():
    print("=== WALKING FROM (26, 0) TO SECRET HOUSE ===")
    pos = get_pos()
    print("Starting position:", pos)
    
    if pos is None:
        handle_battle()
        pos = get_pos()
        
    path = []
    # 1. Walk Left to Column 25
    path.append("Left")
    # 2. Walk Down Column 25 to Row 18
    path.extend(["Down"] * 18)
    # 3. Walk Left to Column 21
    path.extend(["Left"] * 4)
    # 4. Walk Up to climb East Stairs
    path.extend(["Up"] * 2)
    # 5. Walk Left across Plateau to Column 6
    path.extend(["Left"] * 15)
    # 6. Walk Down to descend West Stairs
    path.extend(["Down"] * 4)
    # 7. Walk Left to Column 1
    path.extend(["Left"] * 5)
    # 8. Walk Up to Row 8
    path.extend(["Up"] * 12)
    # 9. Walk Right to Column 3
    path.extend(["Right"] * 2)
    # 10. Walk Up to enter Secret House (warp)
    path.append("Up")
    
    print("Executing path to Secret House...")
    if not run_path(path, check_warp=True):
        print("Failed to enter Secret House!")
        return False
        
    print("Entered Secret House successfully!")
    return True

if __name__ == "__main__":
    walk_to_secret_house()
