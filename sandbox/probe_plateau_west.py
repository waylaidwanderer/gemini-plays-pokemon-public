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

def probe_plateau_west():
    print("Starting plateau west probe...")
    pos = get_pos()
    print(f"Start position: {pos}")
    
    # Try Columns 20, 21, 22, 23
    for col in range(20, 24):
        print(f"=== Probing Column {col} ===")
        # Walk horizontally on Row 18 to Column col
        if not walk_to_target(col, 18):
            print(f"Failed to reach column {col}")
            continue
            
        # Try to walk UP as far as possible
        y = 18
        while y > 10:
            print(f"Trying to step UP to ({col}, {y-1})...")
            walk_step("Up")
            new_pos = get_pos()
            if new_pos is None:
                run_away()
                new_pos = get_pos()
            if new_pos is not None and new_pos[0] == col and new_pos[1] == y - 1:
                print(f"Successfully reached ({col}, {y-1})!")
                y -= 1
            else:
                print(f"Blocked! Cannot walk UP from ({col}, {y}). Current pos: {new_pos}")
                break
                
        # Walk back down to row 18
        print(f"Returning to Row 18 on Column {col}...")
        walk_to_target(col, 18)

if __name__ == "__main__":
    probe_plateau_west()
