import time
import bridge

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
    # Move to RUN and select
    bridge.press_buttons(["Right", "sleep 250", "Down", "sleep 250", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 400"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 400"])

def navigate_path():
    # Desired path from (28, 17) to (30, 11)
    # 1. Down to row 20 (3 steps)
    # 2. Right to column 30 (2 steps)
    # 3. Up to row 11 (9 steps)
    
    # We will dynamically calculate the direction based on current position and target path.
    # To be extremely safe, we will just walk step-by-step.
    
    target_path = [
        # Down
        (28, 18), (28, 19), (28, 20),
        # Right
        (29, 20), (30, 20),
        # Up
        (30, 19), (30, 18), (30, 17), (30, 16), (30, 15), (30, 14), (30, 13), (30, 12), (30, 11)
    ]
    
    idx = 0
    stuck_count = 0
    
    while idx < len(target_path):
        pos = get_pos()
        if pos is None:
            run_away()
            continue
            
        cx, cy = pos
        print(f"Current position: ({cx}, {cy}). Target: {target_path[idx]}")
        
        # If we are already at the target tile, advance
        if cx == target_path[idx][0] and cy == target_path[idx][1]:
            idx += 1
            stuck_count = 0
            continue
            
        tx, ty = target_path[idx]
        dx = tx - cx
        dy = ty - cy
        
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
            idx += 1
            continue
            
        print(f"Walking {direction} to reach {target_path[idx]}")
        walk_step(direction)
        
        new_pos = get_pos()
        if new_pos is None:
            run_away()
            continue
            
        ncx, ncy = new_pos
        if ncx == cx and ncy == cy:
            stuck_count += 1
            print(f"Stuck at ({cx}, {cy})! Stuck count: {stuck_count}")
            if stuck_count >= 3:
                print("Too many stucks, running run_away() to clear any hidden battles/dialogs.")
                run_away()
                stuck_count = 0
        else:
            stuck_count = 0

    print("Path navigation complete!")

if __name__ == "__main__":
    navigate_path()
