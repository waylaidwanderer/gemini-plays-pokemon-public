import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Attempting to run away from battle...")
    # Clear any battle start text first
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
    # Press Down, Right, A to select RUN
    bridge.press_buttons(["Down", "Right", "A", "sleep 500"])

def walk_step(direction):
    print(f"Stepping {direction}...")
    bridge.press_buttons([direction, "sleep 300"])

def navigate_path(path):
    for target in path:
        tx, ty = target
        print(f"Navigating to target: ({tx}, {ty})")
        while True:
            pos = get_pos()
            if pos is None:
                run_away()
                continue
            
            cx, cy = pos
            if cx == tx and cy == ty:
                print(f"Arrived at ({tx}, {ty})")
                break
                
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
                print("Coordinates did not change. Possible battle or block. Attempting to run/clear...")
                run_away()
                after_run_pos = get_pos()
                if after_run_pos == pos:
                    print(f"BLOCKED! Stalled at ({cx}, {cy}) trying to go {dir_btn}")
                    return False
    return True

# Path to stand at (19, 24)
path = [(20, 24), (19, 24)]
success = navigate_path(path)
if success:
    print("Arrived at (19, 24). Retrieving Gold Teeth...")
    # Turn Down, press A, then clear dialogue
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 500", "A", "sleep 500", "A", "sleep 500"])
    print("Gold Teeth retrieval script complete!")
else:
    print("Failed to reach (19, 24).")
