import bridge
import time

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    # First press B multiple times to dismiss text
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
    # Move to RUN and select (Safari Zone escape)
    bridge.press_buttons(["Right", "sleep 250", "Down", "sleep 250", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 400"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 400"])

def execute_safari():
    # 1. Path from Area 3 (29, 23) to transition (0, 13) via Row 26 Highway and Column 30
    path_to_east_warp = [
        "Right", # (30, 23)
        "Down", "Down", "Down", # (30, 26)
        # 25 steps Left to (5, 26)
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left",
        # 12 steps Up to (5, 14)
        "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up", "Up",
        # 5 steps Left to (0, 14)
        "Left", "Left", "Left", "Left", "Left",
        # 1 step Up to (0, 13) (warp!)
        "Up"
    ]
    
    # 2. Path in Center (East Compartment) to Gold Teeth at (19, 25).
    # We warp to Center at (29, 25) (or (29, 26)). Let's align to (29, 26) and walk left.
    path_to_teeth = [
        "Down", # To Row 26 (29, 26)
        # Walk Left to Column 19 (10 steps Left)
        "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left"
    ]
    
    # 3. From (19, 26), walk back to transition at (29, 25) (or (29, 26))
    path_back_to_warp = [
        # Walk Right to Column 29 (10 steps Right)
        "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right",
        "Up" # To warp (29, 25) -> transitions back to Area 3 (West) at (0, 13)
    ]
    
    # 4. From Area 3 (0, 13), walk to Secret House door at (3, 8)
    path_to_house = [
        # Walk Up Column 0 to Row 8 (5 steps Up)
        "Up", "Up", "Up", "Up", "Up",
        # Walk Right to Column 3 (3 steps Right)
        "Right", "Right", "Right"
    ]

    print("--- STEP 1: Walking to East Warp at (0, 13) ---")
    if not run_path(path_to_east_warp, check_warp=True):
        return False
        
    print("--- STEP 2: Aligned in Center (East Compartment). Walking to Gold Teeth ---")
    if not run_path(path_to_teeth, check_warp=False):
        return False
        
    # Stand at (19, 26) facing UP and press A to pick up Gold Teeth!
    pos = get_pos()
    print(f"Standing below Gold Teeth at {pos}. Interacting...")
    # First make sure we are facing UP
    walk_step("Up") # Bumps into the item, turning us UP
    time.sleep(0.5)
    bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
    print("Gold Teeth picked up!")
    
    print("--- STEP 3: Walking back to warp to Area 3 (West) ---")
    if not run_path(path_back_to_warp, check_warp=True):
        return False
        
    print("--- STEP 4: Aligned in Area 3 (West). Walking to Secret House ---")
    if not run_path(path_to_house, check_warp=False):
        return False
        
    # Arrived at (3, 8). Walk UP to enter the Secret House!
    print("Arrived at the Secret House door! Entering...")
    walk_step("Up")
    time.sleep(1.0)
    print("Inside Secret House! Coordinates:", get_pos())
    return True

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            run_away()
            continue
            
        print(f"Path step {idx}: At {pos}, sending {path[idx]}")
        walk_step(path[idx])
        
        new_pos = get_pos()
        if new_pos is None:
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                run_away()
                continue
                
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Blocked. Exiting path.")
                return False
        else:
            stuck_count = 0
            idx += 1
            if check_warp:
                # Check for warp
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"Transition occurred! Jumped to {new_pos}")
                    break
    return True

if __name__ == "__main__":
    execute_safari()
