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

def run_segment1():
    print("Running Segment 1: Center to Area 1 (East)...")
    path1 = [(16, 24), (16, 16), (28, 16), (28, 11), (29, 11)]
    if not navigate_path(path1):
        print("Failed Segment 1 path.")
        return False
        
    print("Transitioning into Area 1 (East)...")
    walk_step("Right")
    time.sleep(1.0)
    
    pos = get_pos()
    print(f"Arrived in Area 1 (East)! Position: {pos}")
    return True

run_segment1()
