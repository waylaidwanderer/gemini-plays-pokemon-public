import bridge
import time
import sys

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        time.sleep(0.1)
    return None

def handle_battle():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    # First press B multiple times to dismiss text
    for _ in range(4):
        bridge.press_buttons(["B"])
        time.sleep(0.3)
    # Move to RUN and select (Safari Zone escape)
    bridge.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    bridge.press_buttons(["B"])
    time.sleep(0.3)

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction])
    
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
            if check_warp and idx == len(path) - 1:
                print("Transition occurred on last step!")
                return True
            handle_battle()
            continue
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            # Check if warp happened
            time.sleep(1.0)
            new_pos = get_pos()
            if new_pos is None:
                if check_warp and idx == len(path) - 1:
                    print("Transition occurred!")
                    return True
                handle_battle()
                continue
                
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Path blocked!")
                # Attempt to move away to unstuck
                walk_step_robust("Up")
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
    print("=== FINAL SURF MASTER PLAN V14 ===")
    
    pos = get_pos()
    print("Starting position:", pos)
    
    if pos is not None and pos[1] <= 10:
        print("=== STEP 1: WALKING TO SW TRANSITION ===")
        # Walk Left to Column 4, then Down to Row 36 (Warp!)
        # From (7, 6) -> Left 3 to (4, 6) -> Down 30 to (4, 36)
        path_across_area2 = ["Left"] * 3 + ["Down"] * 30
        if not run_path(path_across_area2, check_warp=True):
            print("Failed to reach SW transition!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived in Area 3 Northwest isolated ground:", pos)
        
    # We should land at (4, 0) inside Area 3 (West) Northwest isolated ground
    if pos is not None and pos[0] == 4 and pos[1] == 0:
        print("=== STEP 2: WALKING TO SECRET HOUSE ===")
        path_to_secret_house = [
            "Left",                                                          # to (3, 0) (1 step Left)
            "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down",  # to (3, 8) (8 steps Down)
            "Up"                                                             # Enter Secret House! (transition)
        ]
        if not run_path(path_to_secret_house, check_warp=True):
            print("Failed to enter Secret House!")
            return
            
        time.sleep(1.0)
        pos = get_pos()
        print("Arrived inside Secret House:", pos)
        
    # Standard coordinates inside Secret House starting point (usually (3, 8) or similar)
    if pos is not None and pos[0] <= 5 and pos[1] <= 8:
        print("=== STEP 3: TALKING TO NPC FOR SURF ===")
        # Walk Left to stand below NPC and interact
        path_inside = [
            "Left", 
            "Up"
        ]
        for step in path_inside:
            bridge.press_buttons([step])
            time.sleep(0.4)
            
        print("Interacting with Surf NPC...")
        bridge.press_buttons(["A"])
        time.sleep(1.2)
        # Dialogue sequence to receive HM03 (Surf)
        for _ in range(8):
            bridge.press_buttons(["A"])
            time.sleep(1.2)
            
        print("=== MASTER PLAN COMPLETED SUCCESSFULLY! ===")

if __name__ == "__main__":
    main()
