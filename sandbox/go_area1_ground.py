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
    bridge.press_buttons([direction, "sleep 350"])

def walk_to_target(tx, ty):
    print(f"Walking to: ({tx}, {ty})")
    stuck_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            run_away()
            continue
        cx, cy = pos
        if cx == tx and cy == ty:
            return True
        dx = tx - cx
        dy = ty - cy
        
        if dx > 0:
            dir_btn = "Right"
        elif dx < 0:
            dir_btn = "Left"
        elif dy > 0:
            dir_btn = "Down"
        elif dy < 0:
            dir_btn = "Up"
        else:
            break
            
        walk_step(dir_btn)
        new_pos = get_pos()
        if new_pos is None:
            run_away()
            continue
        ncx, ncy = new_pos
        if ncx == cx and ncy == cy:
            stuck_count += 1
            print(f"Blocked! Didn't move from ({cx}, {cy}) trying to go {dir_btn}. Stuck: {stuck_count}")
            if stuck_count > 3:
                print("Running RUN sequence to clear.")
                run_away()
                stuck_count = 0
                time.sleep(1.0)
        else:
            stuck_count = 0
    return True

def run_bypass():
    print("Starting optimized ground-level bypass to Area 1 (East) via Column 22...")
    
    # 1. Climb down stairs to ground level (24, 16)
    if not walk_to_target(24, 14):
        return False
    if not walk_to_target(24, 15):
        return False
    # Walk DOWN onto ground level (24, 16)
    walk_step("Down")
    time.sleep(1.0)
    
    # 2. Walk Left to Column 22
    if not walk_to_target(22, 16):
        return False
        
    # 3. Walk DOWN Column 22 to Row 26 (bypassing the Row 25 barrier)
    if not walk_to_target(22, 26):
        return False
        
    # 4. Walk RIGHT along Row 26 to Column 29
    if not walk_to_target(29, 26):
        return False
        
    print("At transition coordinate (29, 26). Walking Right to transition...")
    walk_step("Right")
    time.sleep(1.5)
    
    new_pos = get_pos()
    print(f"Transition complete! New position: {new_pos}")
    return True

if __name__ == "__main__":
    run_bypass()
