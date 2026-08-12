import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        time.sleep(0.1)
    return None

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return None
    bridge.press_buttons([direction])
    for _ in range(5):
        time.sleep(0.12)
        new_pos = get_pos()
        if new_pos != pos:
            return new_pos
    return pos

def probe_gap():
    print("=== PROBING FOR CONNECTION GAP ON COLUMN 11 ===")
    pos = get_pos()
    print("Starting from:", pos)
    
    # We are at (12, 17)
    # Walk Up Column 12 to Row 11
    path_up = ["Up"] * 6 # to (12, 11)
    for step in path_up:
        res = walk_step_robust(step)
        if res is None or res == pos:
            print(f"Failed to walk Up to Row 11! Stuck at {res}")
            return False
            
    current_y = 11
    # Probe each row from 11 down to 0
    for y in range(11, -1, -1):
        # Walk to Row y on Column 12
        while current_y > y:
            res = walk_step_robust("Up")
            if res is not None:
                current_y = res[1]
            else:
                break
        while current_y < y:
            res = walk_step_robust("Down")
            if res is not None:
                current_y = res[1]
            else:
                break
                
        # Try walking Left to Column 11
        pos_before = get_pos()
        if pos_before is None or pos_before[1] != y:
            print(f"Position desync, expected Column 12 Row {y} but got {pos_before}")
            continue
            
        res_left = walk_step_robust("Left")
        if res_left is not None and res_left[0] == 11:
            print(f"!!! SUCCESS! GAP FOUND AT ROW {y} !!!")
            # Walk back to Column 12 to continue probe or stop
            walk_step_robust("Right")
        else:
            print(f"Row {y} is blocked.")
            
    print("=== PROBE COMPLETE ===")
    return True

if __name__ == "__main__":
    probe_gap()
