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
    print("Starting optimized speedrun using flat-ground routes...")
    
    # --- Part 1: Walk in Area 3 (West) to East Edge Transition ---
    print("--- PART 1: Navigating to Center Transition (30, 23) in Area 3 ---")
    path_part1 = [
        # Walk Down to Row 26 (Highway)
        (1, 26),
        # Walk Right along Row 26 to Column 21
        (21, 26),
        # Walk Up to Row 23
        (21, 23),
        # Walk Right to Column 30
        (30, 23)
    ]
    for target in path_part1:
        if not walk_to(target[0], target[1]):
            print("Failed in Part 1")
            return
            
    print("Transitioning into Center...")
    walk_step("Right")
    time.sleep(1.5)
    
    # --- Part 2: Walk in Center to get Gold Teeth ---
    print("--- PART 2: Retrieving Gold Teeth ---")
    pos = get_pos()
    print(f"Position inside Center: {pos}")
    
    path_part2 = [
        # Walk Down to Row 22
        (0, 22),
        # Walk Right to Column 28
        (28, 22),
        # Walk Down to Row 26
        (28, 26),
        # Walk Left to Column 19
        (19, 26)
    ]
    for target in path_part2:
        if not walk_to(target[0], target[1]):
            print("Failed in Part 2")
            return
            
    print("Standing below Gold Teeth. Picking them up...")
    bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
    
    # --- Part 3: Walk in Center to Transition back to Area 3 (West) ---
    print("--- PART 3: Navigating to Area 3 Transition (0, 11) in Center ---")
    path_part3 = [
        # Walk Right to Column 28
        (28, 26),
        # Walk Up to Row 22
        (28, 22),
        # Walk Left to Column 0
        (0, 22),
        # Walk Up to Row 11
        (0, 11)
    ]
    for target in path_part3:
        if not walk_to(target[0], target[1]):
            print("Failed in Part 3")
            return
            
    print("Transitioning back to Area 3...")
    walk_step("Left")
    time.sleep(1.5)
    
    # --- Part 4: Walk in Area 3 (West) to enter the Secret House ---
    print("--- PART 4: Entering Secret House ---")
    pos = get_pos()
    print(f"Position inside Area 3: {pos}")
    
    path_part4 = [
        # Walk Down to Row 26
        (29, 26),
        # Walk Left to Column 3
        (3, 26),
        # Walk Up to Row 8
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
