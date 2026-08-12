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
            # Transition occurred or battle
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
            # Let's wait a moment and check if we are actually in a battle transition
            time.sleep(0.5)
            check_pos = get_pos()
            if check_pos is None:
                print("Battle transition detected during stuck check! Handling battle...")
                handle_battle()
                stuck_count = 0
                continue
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

def walk_to_staging_point():
    print("=== WALKING TO STAGING POINT (11, 12) IN AREA 3 ===")
    pos = get_pos()
    print("Starting position:", pos)
    if pos != (21, 18):
        print("Expected starting position (21, 18)!")
        return False
        
    path = [
        "Up", "Up", "Up", "Up",                                           # to (21, 14) (climbs stairs)
        "Left", "Left", "Left", "Left", "Left", "Left",                   # to (15, 14)
        "Down", "Down",                                                   # to (15, 16)
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
        "Left", "Left",                                                   # to (5, 16) (10 steps Left)
        "Right",                                                          # to (6, 16)
        "Down", "Down", "Down", "Down",                                   # to (6, 20) (descends West Stairs)
        "Left", "Left", "Left", "Left", "Left",                           # to (1, 20) (5 steps Left)
        "Up", "Up", "Up", "Up",                                           # to (1, 16) (4 steps Up)
        "Right",                                                          # to (2, 16)
        "Up", "Up",                                                       # to (2, 14)
        "Right", "Right", "Right", "Right", "Right", "Right", "Right",
        "Right",                                                          # to (10, 14) (8 steps Right)
        "Up", "Up",                                                       # to (10, 12)
        "Right"                                                           # to (11, 12)
    ]
    
    print("Executing path...")
    if not run_path(path):
        print("Failed to reach staging point (11, 12)!")
        return False
        
    print("SUCCESS! Standing at (11, 12).")
    return True

if __name__ == "__main__":
    walk_to_staging_point()
