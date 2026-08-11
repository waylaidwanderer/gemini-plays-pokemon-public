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

def run_segment_3():
    print("=== SEGMENT 3: Area 2 (North) -> Area 3 (West) ===")
    path_points = [
        # Start at (18, 32)
        # 1. Walk RIGHT to Column 22
        (22, 32),
        # 2. Walk UP to Row 23
        (22, 23),
        # 3. Climb stairs UP onto Western Southern Plateau (22, 22)
        (22, 22),
        # 4. Walk LEFT on plateau to Column 16
        (16, 22),
        # 5. Descend stairs DOWN to Row 33 (16, 33)
        (16, 33),
        # 6. Walk LEFT along Row 33 to Column 9
        (9, 33),
        # 7. Walk DOWN Column 9 to Row 36
        (9, 36),
        # 8. Transition DOWN into Area 3 (West)
        (9, 37)
    ]

    for idx, target in enumerate(path_points):
        print(f"--- Sub-Segment {idx+1}: Navigating to target {target} ---")
        
        # Check if we transitioned maps (detect y coordinate jump or x coordinate jump)
        curr = get_pos()
        if curr is not None and idx >= 7: # Near the end of Area 2
            if curr[1] < 5: # Area 3 coords are around row 0, e.g. (9, 0)
                print(f"Map transition detected early at: {curr}")
                break
                
        if not walk_to(target[0], target[1]):
            print(f"Failed at sub-segment {idx+1}")
            return False
            
    print(f"Segment 3 complete. Position: {get_pos()}")
    return True

if __name__ == "__main__":
    run_segment_3()
