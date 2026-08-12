import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    # Robust get_pos with retry to prevent false-positive battle triggers
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        time.sleep(0.1)
    return None

def handle_battle():
    print("Wild battle detected! Escaping...")
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

def run_path(path, check_warp=False):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        print(f"Path step {idx}: At {pos}, walking {path[idx]}...")
        new_pos = walk_step_robust(path[idx])
        
        if new_pos is None:
            time.sleep(0.5)
            new_pos = get_pos()
            if new_pos is None:
                if check_warp:
                    print("SUCCESS! Transition occurred!")
                    return True
                handle_battle()
                continue
                
        if new_pos == pos:
            stuck_count += 1
            print(f"Stuck at {pos}! Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Path blocked. Exiting path.")
                return False
        else:
            stuck_count = 0
            idx += 1
            if check_warp:
                dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                if dist > 5:
                    print(f"SUCCESS! Transitioned to coordinates: {new_pos}")
                    break
    return True

def scan_rows_for_left_passage():
    print("=== SCANNING ROWS FOR LEFT PASSAGE ===")
    # Currently we are at (8, 34).
    # Let's walk UP to (8, 28) first.
    path_up = ["Up"] * 6
    if not run_path(path_up):
        print("Failed to walk up to row 28.")
        return
        
    # We are at (8, 28) or similar.
    # We want to find a row from row 28 down to row 16 that lets us walk Left to column 4.
    # Wait, let's test row 28, 27, 26, 25, 24, 23, 22, 21, 20...
    # For each row, we try to walk Left to column 4.
    # If we get stuck, we walk back to Column 8, walk Up 1 row, and try again.
    
    current_row = 28
    while current_row >= 16:
        pos = get_pos()
        print(f"Testing Row {pos[1]}...")
        
        # Try to walk Left to Column 4
        stuck = False
        steps_left = pos[0] - 4
        for _ in range(steps_left):
            curr_pos = get_pos()
            new_pos = walk_step_robust("Left")
            if new_pos is None:
                handle_battle()
                new_pos = get_pos()
            if new_pos == curr_pos:
                print(f"Blocked on row {curr_pos[1]} at col {curr_pos[0]}!")
                stuck = True
                break
                
        if not stuck:
            print(f"SUCCESS! Walked Left to column 4 on Row {get_pos()[1]}!")
            # Now walk Down to (4, 36) to transition!
            curr_pos = get_pos()
            down_steps = 36 - curr_pos[1]
            print(f"Walking Down {down_steps} steps to transition...")
            run_path(["Down"] * down_steps, check_warp=True)
            return True
            
        # If stuck, walk back to Column 8
        pos = get_pos()
        if pos[0] < 8:
            print(f"Walking back to Col 8 from Col {pos[0]}...")
            run_path(["Right"] * (8 - pos[0]))
            
        # Walk Up 1 row
        print("Walking Up 1 row to test next row...")
        if not run_path(["Up"]):
            print("Failed to walk Up.")
            break
            
    print("Failed to find any open row!")
    return False

if __name__ == "__main__":
    scan_rows_for_left_passage()
