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
    print("Wild battle/interaction detected! Escaping...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 200"])
    bridge.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1200"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        handle_battle()
        return None
        
    bridge.press_buttons([direction])
    
    # Wait for position to change (up to 750 ms)
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
            
        print(f"Path: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                handle_battle()
                continue
                
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                return False
        else:
            stuck_count = 0
            idx += 1
    return True

def scan_column5():
    print("=== SCANNING COLUMN 5 GAPS ===")
    
    # Currently at (7, 33).
    # We will walk UP to Row 16 on Column 7.
    # At each row, we will try to walk Left up to Column 4.
    
    # Let's walk UP to Row 16 on Column 7.
    pos = get_pos()
    steps_up = pos[1] - 16
    print(f"Walking UP {steps_up} steps on Column 7...")
    for _ in range(steps_up):
        run_path(["Up"])
        
    # Now we are at (7, 16). Let's scan DOWN from row 16 to 33
    row = 16
    while row <= 33:
        # Move player to (7, row) if not already there
        pos = get_pos()
        if pos[1] != row:
            if pos[1] < row:
                run_path(["Down"] * (row - pos[1]))
            else:
                run_path(["Up"] * (pos[1] - row))
                
        # Try to walk Left to Column 4
        print(f"Probing LEFT on Row {row}...")
        stuck = False
        pos = get_pos()
        steps_left = pos[0] - 4
        for _ in range(steps_left):
            curr_pos = get_pos()
            new_pos = walk_step_robust("Left")
            if new_pos is None:
                handle_battle()
                new_pos = get_pos()
            if new_pos == curr_pos:
                print(f"BLOCKED at {curr_pos} walking Left!")
                stuck = True
                break
                
        if not stuck:
            print(f"=== SUCCESS! FOUND OPEN PATH TO COL 4 ON ROW {row} ===")
            # Walk Down to (4, 36) to transition!
            curr_pos = get_pos()
            down_steps = 36 - curr_pos[1]
            print(f"Walking Down {down_steps} steps to transition...")
            run_path(["Down"] * down_steps)
            return True
            
        # Walk back to Column 7 if we moved
        pos = get_pos()
        if pos[0] < 7:
            print(f"Returning to Col 7...")
            run_path(["Right"] * (7 - pos[0]))
            
        row += 1
        
    print("Scan completed. No open gap found on Column 5 from Row 16 to 33!")
    return False

if __name__ == "__main__":
    scan_column5()
