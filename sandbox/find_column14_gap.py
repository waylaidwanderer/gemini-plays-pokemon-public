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

def scan_column14():
    print("=== SCANNING COLUMN 14 GAPS ===")
    
    # Currently at (13, 20).
    # We will try to walk Right at each row from row 20 to row 33.
    # If we get stuck, we walk Down 1 row and try again.
    
    row = 20
    while row <= 33:
        # Move player to (13, row) if not already there
        pos = get_pos()
        if pos[1] != row:
            if pos[1] < row:
                run_path(["Down"] * (row - pos[1]))
            else:
                run_path(["Up"] * (pos[1] - row))
                
        # Try to walk Right
        print(f"Probing RIGHT on Row {row}...")
        stuck = False
        pos = get_pos()
        
        curr_pos = get_pos()
        new_pos = walk_step_robust("Right")
        if new_pos is None:
            handle_battle()
            new_pos = get_pos()
        if new_pos == curr_pos:
            print(f"BLOCKED at {curr_pos} walking Right!")
            stuck = True
            
        if not stuck:
            print(f"=== SUCCESS! FOUND OPEN PATH TO COL 14 ON ROW {row} at {get_pos()} ===")
            return True
            
        row += 1
        
    print("Scan completed. No open gap found on Column 14 from Row 20 to 33!")
    return False

if __name__ == "__main__":
    scan_column14()
