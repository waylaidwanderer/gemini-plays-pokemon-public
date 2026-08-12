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
            # We transition maps or enter battle
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
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            # Transition or battle occurred
            time.sleep(1.0)
            new_pos = get_pos()
            if new_pos is None:
                handle_battle()
                continue
            else:
                if check_warp:
                    dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                    if dist > 5:
                        print(f"SUCCESS! Transitioned to: {new_pos}")
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
                    print(f"SUCCESS! Transitioned to: {new_pos}")
                    break
            idx += 1
    return True

def obtain_surf():
    print("=== EXECUTING SURF ACQUISITION CAMPAIGN FROM (21, 18) ===")
    pos = get_pos()
    print("Starting position:", pos)
    
    if pos is None:
        handle_battle()
        pos = get_pos()
        
    # We are at (21, 18)
    path = []
    # 1. Walk Up to climb East Stairs
    path.extend(["Up"] * 4)       # to (21, 14) (climbs stairs at (21, 17) and goes to (21, 14))
    # 2. Walk Left to Column 15
    path.extend(["Left"] * 6)     # to (15, 14)
    # 3. Walk Down to Row 16
    path.extend(["Down"] * 2)     # to (15, 16)
    # 4. Walk Left to Column 5
    path.extend(["Left"] * 10)    # to (5, 16)
    # 5. Walk Right to Column 6
    path.append("Right")          # to (6, 16)
    # 6. Walk Down to Row 20
    path.extend(["Down"] * 4)     # to (6, 20) (descends West Stairs at (6, 19))
    # 7. Walk Left to Column 1
    path.extend(["Left"] * 5)     # to (1, 20)
    # 8. Walk Up to Row 8
    path.extend(["Up"] * 12)      # to (1, 8)
    # 9. Walk Right to Column 3
    path.extend(["Right"] * 2)    # to (3, 8)
    # 10. Walk Up to enter Secret House (warp)
    path.append("Up")
    
    print("Walking to Secret House...")
    if not run_path(path, check_warp=True):
        print("Failed to reach Secret House!")
        return False
        
    time.sleep(1.5)
    pos = get_pos()
    print("Position inside Secret House:", pos)
    
    # 11. Walk to NPC inside Secret House
    path_inside = [
        "Up", "Up", "Up", "Left", "Up"
    ]
    print("Walking to NPC...")
    for step in path_inside:
        bridge.press_buttons([step, "sleep 350"])
        
    print("Interacting with NPC to obtain HM03 (Surf)...")
    for _ in range(8):
        bridge.press_buttons(["A", "sleep 1200"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 500"])
        
    print("=== SURF RETRIEVED SUCCESSFULLY ===")
    return True

if __name__ == "__main__":
    obtain_surf()
