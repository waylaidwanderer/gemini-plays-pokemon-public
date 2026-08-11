import time
import sys
import bridge

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
    bridge.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 300"])

def walk_step(direction):
    bridge.press_buttons([direction])
    time.sleep(0.4)

def walk_to(target_x, target_y):
    consecutive_bumps = 0
    while True:
        pos = get_pos()
        if pos is None:
            run_away()
            continue
            
        cx, cy = pos
        if cx == target_x and cy == target_y:
            print(f"Arrived at target: ({cx}, {cy})")
            return True
            
        dx = target_x - cx
        dy = target_y - cy
        
        direction = None
        if dx > 0:
            direction = "Right"
        elif dx < 0:
            direction = "Left"
        elif dy > 0:
            direction = "Down"
        elif dy < 0:
            direction = "Up"
            
        if direction is None:
            return True
            
        print(f"Currently at ({cx}, {cy}). Walking {direction} towards ({target_x}, {target_y})...")
        walk_step(direction)
        
        new_pos = get_pos()
        if new_pos is None:
            run_away()
            continue
            
        if new_pos == pos:
            consecutive_bumps += 1
            print(f"Bumped! (Count: {consecutive_bumps})")
            if consecutive_bumps >= 5:
                print("Stuck! Attempting RUN away to clear...")
                run_away()
                consecutive_bumps = 0
        else:
            consecutive_bumps = 0

def main():
    print("Starting remaining speedrun from current position...")
    
    # --- Part 1: Area 3 (West) to Center (East Compartment) ---
    print("--- PART 1: Navigating to Center Transition (0, 13) ---")
    path_part1 = [
        # Walk down to Row 14 (Hedge Wall Gap)
        (26, 14),
        # Walk Left to Column 9
        (9, 14),
        # Walk Up to Row 13
        (9, 13),
        # Walk Left to Column 0
        (0, 13)
    ]
    for target in path_part1:
        if not walk_to(target[0], target[1]):
            print("Failed in Part 1")
            return
            
    # Walk Left to transition into Center (East Compartment)
    print("Transitioning into Center...")
    walk_step("Left")
    time.sleep(1.5)
    
    # --- Part 2: Inside Center (East Compartment) to get Gold Teeth ---
    print("--- PART 2: Retrieving Gold Teeth ---")
    pos = get_pos()
    print(f"Position inside Center: {pos}")
    
    # Walk to (19, 26)
    if not walk_to(19, 26):
        print("Failed to reach (19, 26) for Gold Teeth")
        return
        
    print("Standing below Gold Teeth. Picking them up...")
    # Interaction sequence to pick up the Gold Teeth
    bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
    
    # --- Part 3: Center (East Compartment) to Area 3 (West) ---
    print("--- PART 3: Navigating to Area 3 Transition (0, 14) ---")
    path_part3 = [
        # Walk to (5, 26)
        (5, 26),
        # Walk to (5, 14)
        (5, 14),
        # Walk to (0, 14)
        (0, 14)
    ]
    for target in path_part3:
        if not walk_to(target[0], target[1]):
            print("Failed in Part 3")
            return
            
    # Walk Left to transition into Area 3 (West)
    print("Transitioning back to Area 3...")
    walk_step("Left")
    time.sleep(1.5)
    
    # --- Part 4: Area 3 (West) to Secret House door (3, 8) ---
    print("--- PART 4: Entering Secret House ---")
    pos = get_pos()
    print(f"Position inside Area 3: {pos}")
    
    path_part4 = [
        # Walk to (0, 14)
        (0, 14),
        # Walk to (0, 8)
        (0, 8),
        # Walk to (3, 8)
        (3, 8)
    ]
    for target in path_part4:
        if not walk_to(target[0], target[1]):
            print("Failed in Part 4")
            return
            
    print("Arrived at Secret House door. Entering...")
    walk_step("Up")
    time.sleep(1.5)
    
    print(f"Speedrun complete! Current position: {get_pos()}")

if __name__ == "__main__":
    main()
