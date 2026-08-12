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

def handle_battle():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
    bridge.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 400"])

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction])
    
    for _ in range(5):
        time.sleep(0.15)
        new_pos = get_pos()
        if new_pos is None:
            return None
        if new_pos != pos:
            return new_pos
            
    print(f"Bumping/stuck at {pos} walking {direction}!")
    return pos

def run_path(path):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        print(f"Step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(1.0)
            new_pos = get_pos()
            if new_pos is None:
                handle_battle()
                continue
                
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Path blocked!")
                return False
        else:
            stuck_count = 0
            idx += 1
    return True

def probe_left():
    # Try walking Left to Column 11
    pos_before = get_pos()
    if pos_before is None:
        return
    res_left = walk_step_robust("Left")
    if res_left is not None and res_left[0] == 11:
        print(f"!!! SUCCESS! GAP FOUND AT ROW {pos_before[1]} !!!")
        # Walk back to Column 12 to continue probe
        walk_step_robust("Right")
    else:
        print(f"Row {pos_before[1]} is blocked.")

def main():
    print("=== STARTING THE ROW 0-4 PROBE ===")
    pos = get_pos()
    print("Starting position:", pos)
    
    # Walk Up from (12, 9) to (12, 4)
    path_to_row4 = ["Up", "Up", "Up", "Up", "Up"]
    if not run_path(path_to_row4):
        print("Failed to walk to Row 4!")
        return
        
    pos = get_pos()
    print("At Row 4, position:", pos)
    
    # Try walking Left at Row 4
    probe_left()
    
    # Walk Up to Row 3
    if walk_step_robust("Up") is not None:
        print("At Row 3, position:", get_pos())
        probe_left()
        
    # Walk Up to Row 2
    if walk_step_robust("Up") is not None:
        print("At Row 2, position:", get_pos())
        probe_left()
        
    # Walk Up to Row 1
    if walk_step_robust("Up") is not None:
        print("At Row 1, position:", get_pos())
        probe_left()
        
    # Walk Up to Row 0
    if walk_step_robust("Up") is not None:
        print("At Row 0, position:", get_pos())
        probe_left()

if __name__ == "__main__":
    main()
