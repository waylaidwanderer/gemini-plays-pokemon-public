import time
import mgba

def get_pos():
    pos = mgba.get_coordinates()
    if pos is None:
        return None
    return pos.get('x'), pos.get('y')

def run_away():
    print("Attempting to run away from battle...")
    # Clear any battle start text first
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
    # Press Down, Right, A to select RUN
    mgba.press_buttons(["Down", "Right", "A", "sleep 500"])

def walk_step(direction):
    print(f"Stepping {direction}...")
    mgba.press_buttons([direction, "sleep 300"])

def navigate_path(path):
    for target in path:
        tx, ty = target
        print(f"Navigating to target: ({tx}, {ty})")
        while True:
            pos = get_pos()
            if pos is None:
                # We might be in a transition or battle where coordinates are None
                run_away()
                continue
            
            cx, cy = pos
            if cx == tx and cy == ty:
                print(f"Arrived at ({tx}, {ty})")
                break
                
            dx = tx - cx
            dy = ty - cy
            
            # Decide direction
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
                
            # Try to walk
            walk_step(dir_btn)
            
            # Check if we moved
            new_pos = get_pos()
            if new_pos is None:
                run_away()
                continue
                
            ncx, ncy = new_pos
            if ncx == cx and ncy == cy:
                # We didn't move! We might be in a battle or blocked
                print("Coordinates did not change. Possible battle or block. Attempting to run/clear...")
                run_away()
                # Check again after trying to run
                after_run_pos = get_pos()
                if after_run_pos == pos:
                    # Still didn't move, we are likely blocked by collision!
                    print(f"BLOCKED! Stalled at ({cx}, {cy}) trying to go {dir_btn}")
                    return False

    return True

# Define path to the Gold Teeth (stand at 19, 26 facing UP to the teeth at 19, 25)
path = [(24, 18), (21, 18), (21, 26), (19, 26)]
success = navigate_path(path)
if success:
    print("Path navigation complete. Facing UP to retrieve teeth...")
    # Turn UP and press A to pick up the Gold Teeth
    mgba.press_buttons(["Up", "sleep 300", "A", "sleep 500", "A", "sleep 500"])
    print("Gold Teeth retrieval attempted!")
else:
    print("Failed to reach the Gold Teeth path.")
