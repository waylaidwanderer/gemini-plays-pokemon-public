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
            print(f"Blocked trying to go {dir_btn} at ({cx}, {cy})")
            return False
    return True

def test_column22():
    print("Starting Column 22 walk test...")
    # Walk horizontally to (22, 17)
    if not walk_to_target(22, 17):
        print("Failed to reach (22, 17)")
        return
        
    print("Reached (22, 17)! Now attempting to walk UP Column 22...")
    for y in range(16, 9, -1):
        print(f"Trying to step UP to (22, {y})...")
        walk_step("Up")
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        if pos is not None and pos[1] == y:
            print(f"Successfully reached (22, {y})!")
        else:
            print(f"Blocked! Cannot reach (22, {y}). Current pos: {pos}")
            break

if __name__ == "__main__":
    test_column22()
