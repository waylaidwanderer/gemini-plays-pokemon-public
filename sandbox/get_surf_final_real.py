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

def run_surf_campaign_real():
    pos = get_pos()
    print("Starting campaign from position:", pos)
    
    if pos is None:
        print("Dismissing any active screen...")
        bridge.press_buttons(["B", "sleep 500"])
        pos = get_pos()
        print("Position after B:", pos)
        
    # We are at (25, 14) in Area 3 (West)
    path = []
    
    # 1. Walk from (25, 14) to (21, 18)
    path.extend(["Down"] * 4)     # To (25, 18)
    path.extend(["Left"] * 4)     # To (21, 18)
    
    # 2. Walk across Plateau
    path.extend(["Up"] * 2)       # To (21, 16) (climb East Stairs)
    path.extend(["Left"] * 15)    # To (6, 16) (across the Plateau)
    path.extend(["Down"] * 4)     # To (6, 20) (descend West Stairs)
    path.extend(["Left"] * 5)     # To (1, 20)
    
    # 3. Walk to the Secret House door at (3, 8)
    path.extend(["Up"] * 11)      # To (1, 9)
    path.extend(["Right"] * 2)    # To (3, 9)
    path.extend(["Up"] * 1)       # To (3, 8) (transition into Secret House!)
    
    print("=== EXECUTING REAL GOLDEN PATH TO SECRET HOUSE ===")
    if not run_path(path, check_warp=True):
        print("Failed to reach Secret House door!")
        return False
        
    time.sleep(1.0)
    pos = get_pos()
    print("Coordinates inside Secret House:", pos)
    
    # 4. Stand in front of NPC at (2, 7) inside Secret House
    # Typically, inside Secret House, we warp to somewhere near the entrance, e.g. (3, 8) or similar.
    # We walk to (2, 7) or walk up to face the NPC.
    path_inside = [
        "Up", "Up", "Up", "Left", "Up"
    ]
    print("=== WALKING INSIDE SECRET HOUSE ===")
    # Let's walk robustly inside (no battles, so standard steps are fine)
    for step in path_inside:
        bridge.press_buttons([step, "sleep 300"])
        
    print("Interacting with NPC to obtain HM03 (Surf)...")
    for _ in range(8):
        bridge.press_buttons(["A", "sleep 1200"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 500"])
        
    print("=== REAL CAMPAIGN COMPLETE ===")
    return True

if __name__ == "__main__":
    run_surf_campaign_real()
