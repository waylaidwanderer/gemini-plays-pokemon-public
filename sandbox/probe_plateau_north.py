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

def probe_plateau_north():
    print("Navigating to plateau stairs at (24, 15)...")
    # Walk to (28, 17)
    if not walk_to_target(28, 17):
        return
    # Walk to (24, 17)
    if not walk_to_target(24, 17):
        return
    # Walk to (24, 14) (climbs the stairs)
    if not walk_to_target(24, 14):
        return
        
    print("Successfully reached plateau at (24, 14)!")
    
    # We will test Columns 20 to 27 on Row 12 to see if we can step UP to Row 11
    for col in range(20, 28):
        print(f"Testing Column {col}...")
        # Walk to (col, 12)
        if not walk_to_target(col, 12):
            print(f"Failed to reach target (col, 12) for Column {col}")
            continue
            
        # Try to step UP to Row 11
        walk_step("Up")
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
            
        if pos is not None and pos[1] == 11:
            print(f"!!! SUCCESS !!! Column {col} Row 11 is WALKABLE from Row 12!")
            print(f"Coordinates reached: {pos}")
            # Walk back down to stay on the plateau
            walk_step("Down")
            return
        else:
            print(f"Column {col} Row 11 is BLOCKED from Row 12.")

if __name__ == "__main__":
    probe_plateau_north()
