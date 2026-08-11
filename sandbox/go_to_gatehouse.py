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

def walk_step(direction):
    bridge.press_buttons([direction])
    time.sleep(0.4)

def main():
    # Target path points from current position (18, 8)
    path_points = [
        # 1. Walk RIGHT Row 8 to Column 23
        (23, 8),
        # 2. Detour around NPC at 24,8
        (23, 9),
        (25, 9),
        (25, 8),
        # 3. Walk RIGHT Row 8 to Column 37
        (37, 8),
        # 4. Walk UP Column 37 to Row 2
        (37, 2),
        # 5. Walk LEFT Row 2 to Column 22
        (22, 2),
        # 6. Walk DOWN Column 22 to Row 4
        (22, 4),
        # 7. Walk LEFT Row 4 to Column 18
        (18, 4),
        # 8. Walk UP Column 18 to Row 3 (enter Gatehouse!)
        (18, 3)
    ]
    
    print(f"Starting path navigation from: {get_pos()}")
    
    for idx, target in enumerate(path_points):
        print(f"--- Segment {idx+1}: Navigating to target {target} ---")
        consecutive_bumps = 0
        
        while True:
            curr = get_pos()
            if curr is None:
                time.sleep(0.5)
                continue
                
            if curr == target:
                print(f"Reached segment target: {curr}")
                break
                
            # Determine direction
            dx = target[0] - curr[0]
            dy = target[1] - curr[1]
            
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
                break
                
            print(f"Current: {curr}, Target: {target}, Walking {direction}...")
            walk_step(direction)
            
            next_pos = get_pos()
            if next_pos == curr:
                consecutive_bumps += 1
                print(f"Bumped! (Count: {consecutive_bumps})")
                
                if consecutive_bumps >= 5:
                    print("Too many consecutive bumps! We might be truly stuck or blocked by something. Aborting.")
                    return
            else:
                consecutive_bumps = 0 # Reset on success

    print(f"Path navigation complete. Current position: {get_pos()}")

if __name__ == "__main__":
    main()
