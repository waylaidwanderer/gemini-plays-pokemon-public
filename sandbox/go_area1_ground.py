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
                print("Running RUN sequence to clear possible battle/text.")
                run_away()
                stuck_count = 0
                time.sleep(1.0)
        else:
            stuck_count = 0
    return True

def run_segment():
    print("Starting ground level route with Row 23 bypass to Area 1 (East) from (27, 24)...")
    
    path = [
        (27, 23), (30, 23), (30, 26), (30, 11), (29, 11)
    ]
    
    for tx, ty in path:
        if not walk_to_target(tx, ty):
            print(f"Failed to reach target: ({tx}, {ty})")
            return False
            
    print("At transition coordinate (29, 11). Walking Right to transition...")
    walk_step("Right")
    time.sleep(1.5)
    
    new_pos = get_pos()
    print(f"Transition complete. New position: {new_pos}")
    return True

if __name__ == "__main__":
    run_segment()
