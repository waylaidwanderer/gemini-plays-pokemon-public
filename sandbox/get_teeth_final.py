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
    print("Starting Gold Teeth retrieval from Center entrance (15, 25)...")
    
    # 1. Walk UP Column 15 to Row 22
    if not walk_to(15, 22):
        print("Failed to reach Row 22")
        return
        
    # 2. Walk RIGHT along Row 22 to Column 28
    if not walk_to(28, 22):
        print("Failed to reach Column 28")
        return
        
    # 3. Walk DOWN Column 28 to Row 26
    if not walk_to(28, 26):
        print("Failed to reach Row 26")
        return
        
    # 4. Walk LEFT along Row 26 to Column 19
    if not walk_to(19, 26):
        print("Failed to reach (19, 26)")
        return
        
    print("Arrived below the Gold Teeth. Picking them up...")
    bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
    
    # 5. Walk to Transition to Area 1 (East) at (30, 11)
    path_part2 = [
        # Walk Right to Column 28
        (28, 26),
        # Walk Up to Row 22
        (28, 22),
        # Walk Up Column 28 to Row 11
        (28, 11),
        # Walk Right along Row 11 to Column 30
        (30, 11)
    ]
    for target in path_part2:
        if not walk_to(target[0], target[1]):
            print("Failed in Part 2")
            return
            
    print("Transitioning into Area 1 (East)...")
    walk_step("Right")
    time.sleep(1.5)
    
    print(f"Teeth Segment complete! Current position: {get_pos()}")

if __name__ == "__main__":
    main()
