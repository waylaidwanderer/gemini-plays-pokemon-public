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
    print("=== NAVIGATING TO SAFARI ZONE GATEHOUSE ===")
    
    pos = get_pos()
    print("Initial position:", pos)
    if pos is None:
        return
        
    # We are at (19, 8). Let's go to (19, 9) first to avoid the NPC at (24, 8)
    if pos == (19, 8):
        print("Stepping Down to Row 9...")
        if not run_path(["Down"]):
            return
            
    pos = get_pos()
    print("Position on Row 9:", pos)
    
    # Path to Column 37 along Row 9
    if pos is not None and pos[1] == 9 and pos[0] < 37:
        right_steps = ["Right"] * (37 - pos[0])
        print(f"Walking Right {len(right_steps)} steps to Column 37...")
        if not run_path(right_steps):
            return
            
    pos = get_pos()
    print("Position at Column 37:", pos)
    
    # Path to Row 2 along Column 37
    if pos is not None and pos[0] == 37 and pos[1] > 2:
        up_steps = ["Up"] * (pos[1] - 2)
        print(f"Walking Up {len(up_steps)} steps to Row 2...")
        if not run_path(up_steps):
            return
            
    pos = get_pos()
    print("Position at Row 2:", pos)
    
    # Path to Column 18 along Row 2
    if pos is not None and pos[1] == 2 and pos[0] > 18:
        left_steps = ["Left"] * (pos[0] - 18)
        print(f"Walking Left {len(left_steps)} steps to Column 18...")
        if not run_path(left_steps):
            return
            
    pos = get_pos()
    print("Position at (18, 2):", pos)
    
    # Walk Down to (18, 4) to align with Gatehouse entrance
    if pos == (18, 2):
        print("Walking Down to Row 4...")
        if not run_path(["Down", "Down"]):
            return
            
    pos = get_pos()
    print("Position at (18, 4):", pos)
    
    # Walk Up to enter Gatehouse at (18, 3) (warp)
    if pos == (18, 4):
        print("Entering Gatehouse...")
        run_path(["Up"], check_warp=True)
        time.sleep(1.5)
        
    print("Navigation script finished!")

if __name__ == "__main__":
    main()
