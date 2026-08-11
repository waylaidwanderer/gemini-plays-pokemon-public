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

def run_segment_2_fixed():
    print("=== SEGMENT 2 (Fixed): Area 1 (East) -> Area 2 (North) ===")
    path_points = [
        # Start at (20, 6)
        # 1. Walk UP Column 20 to Row 3
        (20, 3),
        # 2. Walk LEFT Row 3 to Column 7
        (7, 3),
        # 3. Walk DOWN Column 7 to Row 5
        (7, 5),
        # 4. Walk LEFT Row 5 to Column 0
        (0, 5),
        # 5. Transition Left into Area 2 (North)
        (-1, 5)
    ]

    for idx, target in enumerate(path_points):
        print(f"--- Sub-Segment {idx+1}: Navigating to target {target} ---")
        
        # Check if we transitioned maps (detect x coordinate jump)
        curr = get_pos()
        if curr is not None and idx >= 3: # Near the end of Area 1
            if curr[0] > 30 or curr[1] > 28: # Typical Area 2 coords e.g., (39, 31)
                print(f"Map transition detected early at: {curr}")
                break
                
        if not walk_to(target[0], target[1]):
            print(f"Failed at sub-segment {idx+1}")
            return False
            
    print(f"Segment 2 complete. Position: {get_pos()}")
    return True

if __name__ == "__main__":
    run_segment_2_fixed()
