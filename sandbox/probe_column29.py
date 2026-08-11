import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Attempting robust run away from battle...")
    time.sleep(1.5)
    bridge.press_buttons(["B", "sleep 500", "B", "sleep 500", "B", "sleep 500"])
    bridge.press_buttons(["Down", "sleep 300", "Right", "sleep 300", "A", "sleep 1000"])
    bridge.press_buttons(["B", "sleep 500"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 300"])

def walk_to_target(tx, ty):
    print(f"Walking to: ({tx}, {ty})")
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
            # Blocked, try to clear/run
            run_away()
            time.sleep(2.0)
            after_run = get_pos()
            if after_run == pos:
                print(f"Stalled trying to go {dir_btn} at ({cx}, {cy})")
                return False
    return True

def probe_column29():
    print("Systematic probe of Column 29 starting...")
    # First, make sure we are at (28, 16)
    if not walk_to_target(28, 16):
        print("Failed to reach start coordinate (28, 16)")
        return
        
    for y in range(16, 25):
        print(f"Probing Row {y}...")
        # Walk to (28, y)
        if not walk_to_target(28, y):
            print(f"Failed to reach (28, {y})")
            continue
            
        # Try to step Right
        walk_step("Right")
        pos = get_pos()
        if pos is None:
            run_away()
            time.sleep(2.0)
            pos = get_pos()
            
        if pos is not None and pos[0] == 29:
            print(f"!!! SUCCESS !!! Walkable path found on Column 29 at Row {y}!")
            # Walk back Left to stay on Column 28
            walk_step("Left")
            return
        else:
            print(f"Row {y} is BLOCKED on Column 29.")

probe_column29()
