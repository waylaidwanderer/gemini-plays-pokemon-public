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
        bridge.press_buttons(["B", "sleep 250"])
    bridge.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1200"])
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

def test_column5_rows():
    print("=== SCALING COLUMN 6 TO TEST COLUMN 5 ===")
    
    # 1. Walk Left to Column 6 from (7, 28) -> (6, 28)
    if not run_path(["Left"]):
        print("Failed to reach (6, 28).")
        return
        
    # We will test rows from row 28 up to 23, and then row 29
    rows_to_test = [28, 27, 26, 25, 24, 23, 29]
    for row in rows_to_test:
        pos = get_pos()
        # Move to (6, row)
        if pos[1] != row:
            if pos[1] < row:
                run_path(["Down"] * (row - pos[1]))
            else:
                run_path(["Up"] * (pos[1] - row))
                
        pos = get_pos()
        print(f"Testing LEFT on row {pos[1]} at {pos}...")
        curr_pos = get_pos()
        new_pos = walk_step_robust("Left")
        if new_pos is None:
            handle_battle()
            new_pos = get_pos()
            
        if new_pos[0] == 5:
            print(f"=== SUCCESS! Column 5 is open on Row {row}! Landed at {new_pos} ===")
            # Walk Left to Column 4
            walk_step_robust("Left")
            curr_pos = get_pos()
            print("Landed at:", curr_pos)
            # Walk Down to (4, 36) to transition!
            down_steps = 36 - curr_pos[1]
            print(f"Walking Down {down_steps} steps to transition...")
            run_path(["Down"] * down_steps)
            return True
        else:
            print(f"Row {row} is BLOCKED on Column 5.")
            
    print("All tested rows on Column 5 are blocked.")
    return False

if __name__ == "__main__":
    test_column5_rows()
