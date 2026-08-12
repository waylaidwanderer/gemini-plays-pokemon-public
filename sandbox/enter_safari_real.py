import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        bridge.press_buttons(["sleep 50"])
    return None

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return None
        
    bridge.press_buttons([direction])
    
    for _ in range(5):
        bridge.press_buttons(["sleep 100"])
        new_pos = get_pos()
        if new_pos is not None and new_pos != pos:
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            time.sleep(0.5)
            continue
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                if check_warp:
                    print("Transition occurred!")
                    return True
                continue
                
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print(f"Blocked at {pos}! Exiting path.")
                return False
        else:
            stuck_count = 0
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"Transition occurred! New pos: {new_pos}")
                    break
            idx += 1
    return True

def main():
    print("=== FINISHING ALL DIALOGUE AND ENTERING SAFARI ===")
    
    # We are still in the dialogue. Let's press A 5 times to be absolutely sure we clear everything and warp.
    for i in range(5):
        print(f"Dismissing box {i+1}...")
        bridge.press_buttons(["A", "sleep 1200"])
        
    time.sleep(2.0)
    pos = get_pos()
    print("Coordinates after warp:", pos)
    
    if pos == (15, 25):
        print("Successfully entered Safari Zone Center!")
        
        # We need to transition to Area 1 (East)
        # Golden Route to Area 1 (East) transition at (30, 11)
        # From (15, 25):
        # Walk Up 4 steps to (15, 21)
        # Walk Right 13 steps to (28, 21)
        # Walk Up 10 steps to (28, 11)
        # Walk Right 2 steps to (30, 11)
        # Walk Right 1 step to warp to Area 1 (East) at (0, 22) or (0, 23)
        path_center = (
            ["Up"] * 4 +
            ["Right"] * 13 +
            ["Up"] * 10 +
            ["Right"] * 3
        )
        print("Walking to Area 1 (East) transition...")
        if run_path(path_center, check_warp=True):
            print("Successfully transitioned to Safari Zone Area 1 (East)!")
            time.sleep(1.0)
            
            # Let's verify we are in Area 1 (East)
            new_pos = get_pos()
            print("Position in Area 1:", new_pos)
            
    else:
        print("Not at expected start position (15, 25)!")

if __name__ == "__main__":
    main()
