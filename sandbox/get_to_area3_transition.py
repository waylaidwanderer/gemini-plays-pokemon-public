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
                    print(f"SUCCESS! Transitioned to Area 3 (West) at {new_pos}")
                    break
            idx += 1
    return True

def go_to_area3():
    print("=== STARTING WALK TO AREA 3 (WEST) TRANSITION ===")
    pos = get_pos()
    print("Starting position:", pos)
    
    if pos is None:
        handle_battle()
        pos = get_pos()
        if pos is None:
            return False
            
    # We are at (12, 10). Let's construct path to transition
    path = []
    
    # 1. Walk Down Column 12 to Row 33
    if pos[1] < 33:
        path.extend(["Down"] * (33 - pos[1]))
    elif pos[1] > 33:
        path.extend(["Up"] * (pos[1] - 33))
        
    # 2. Walk Left to Column 8
    if pos[0] > 8:
        path.extend(["Left"] * (pos[0] - 8))
    elif pos[0] < 8:
        path.extend(["Right"] * (8 - pos[0]))
        
    # 3. Walk Down Column 8 to Row 36 to trigger warp
    path.extend(["Down"] * 3)
    
    print("Executing path to Area 3...")
    if not run_path(path, check_warp=True):
        print("Failed to reach Area 3 transition!")
        return False
        
    print("SUCCESS!")
    return True

if __name__ == "__main__":
    go_to_area3()
