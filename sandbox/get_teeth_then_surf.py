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

def run_path(path):
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
            idx += 1
    return True

def retrieve_gold_teeth():
    print("=== RETRIEVING GOLD TEETH ===")
    pos = get_pos()
    print("Starting from:", pos)
    
    if pos is None:
        handle_battle()
        pos = get_pos()
        
    # We are at (1, 16) in Area 3 (West)
    path = []
    
    # 1. Walk Down to Row 20
    path.extend(["Down"] * 4)     # to (1, 20)
    
    # 2. Walk Right to Column 6
    path.extend(["Right"] * 5)    # to (6, 20)
    
    # 3. Walk Up to climb West Stairs onto Plateau
    path.extend(["Up"] * 4)       # to (6, 16)
    
    # 4. Walk Right across Plateau to Column 21
    path.extend(["Right"] * 15)   # to (21, 16)
    
    # 5. Walk Down to descend East Stairs onto ground
    path.extend(["Down"] * 2)     # to (21, 18)
    
    # 6. Walk Down to Row 24
    path.extend(["Down"] * 6)     # to (21, 24)
    
    # 7. Walk Left to Column 19
    path.extend(["Left"] * 2)     # to (19, 24)
    
    print("Executing path to Gold Teeth...")
    if not run_path(path):
        print("Failed to reach Gold Teeth location!")
        return False
        
    time.sleep(0.5)
    pos = get_pos()
    print(f"Arrived below Gold Teeth at {pos}. Interacting...")
    
    # Turn Down to face the item
    walk_step_robust("Down")
    time.sleep(0.5)
    
    # Pick up item
    bridge.press_buttons(["A", "sleep 1200", "A", "sleep 1200", "B", "sleep 500"])
    print("Gold Teeth obtained!")
    
    # 8. Walk to transition back to Area 2 (North) at (26, 0)
    print("Walking to exit Area 3 (West) at (26, 0)...")
    path_to_exit = [
        "Right", "Right",                      # to (21, 24)
        "Up", "Up", "Up", "Up", "Up", "Up",    # to (21, 18)
        "Right", "Right", "Right", "Right", "Right", # to (25, 18)
        "Up", "Up", "Up", "Up"                 # to (25, 14)
    ]
    if not run_path(path_to_exit):
        print("Failed to reach exit staging point!")
        return False
        
    # Walk Up to (25, 3) and Right to (26, 3) and Up to (26, 0)
    path_to_exit_2 = [
        "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", # to (25, 3)
        "Right",                                                           # to (26, 3)
        "Up", "Up", "Up"                                                   # to (26, 0) (warp to Area 2!)
    ]
    if not run_path(path_to_exit_2):
        print("Failed to transition back to Area 2!")
        return False
        
    print("=== GOLD TEETH RETRIEVED AND TRANSITIONED BACK TO AREA 2 (NORTH) ===")
    return True

if __name__ == "__main__":
    retrieve_gold_teeth()
