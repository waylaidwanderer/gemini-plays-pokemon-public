import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    print("No movement detected. Checking for text box or battle...")
    # Clear dialogue text with B
    bridge.press_buttons(["B", "sleep 200", "B", "sleep 200"])
    
    # Try to flee: press Down, then A
    print("Attempting to run from battle...")
    bridge.press_buttons(["Down", "sleep 100", "A", "sleep 1000"])
    
    pos = get_pos()
    print(f"Coordinates after flee attempt: {pos}")
    return pos

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return None
        
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 350"])
    
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
        
    if new_pos != pos:
        return new_pos
        
    time.sleep(1.0)
    new_pos = get_pos()
    if new_pos == pos:
        return handle_textbox_or_battle()
    return new_pos

def main():
    # Phase 1: Walk from (19, 24) to the western ground level at (4, 23) via Plateau
    pos = get_pos()
    print(f"Starting transition to western ground from {pos}...")
    
    # 1. Walk Right to (21, 24)
    # 2. Walk Up to (21, 16)
    # 3. Walk Left to (6, 16)
    # 4. Walk Down to (6, 20)
    # 5. Walk Left to (4, 20)
    # 6. Walk Down to (4, 23)
    transition_path = (
        ["Right"] * 2 +
        ["Up"] * 8 +
        ["Left"] * 15 +
        ["Down"] * 4 +
        ["Left"] * 2 +
        ["Down"] * 3
    )
    
    idx = 0
    stuck_count = 0
    while idx < len(transition_path):
        pos = get_pos()
        if pos is None:
            handle_textbox_or_battle()
            continue
            
        print(f"Transition step {idx+1}/{len(transition_path)}: at {pos}, walking {transition_path[idx]}")
        new_pos = walk_step_robust(transition_path[idx])
        if new_pos is not None:
            if new_pos != pos:
                idx += 1
                stuck_count = 0
            else:
                print("No progress made in transition. Retrying...")
                stuck_count += 1
                if stuck_count > 3:
                    bridge.press_buttons(["B", "sleep 300"])
                    stuck_count = 0
        time.sleep(0.5)
        
    print(f"Successfully arrived at {get_pos()}. Starting systematic Column search...")
    
    # Phase 2: Systematic Column Search from Col 4 to Col 17
    # For each column:
    # We are at (col, 23).
    # Try to walk Down. If success, try to walk Down further to Row 26.
    # If we reach Row 26, we succeed!
    # If blocked, walk back up to Row 23 (if needed), walk Right to (col+1, 23), and repeat.
    
    for col in range(4, 18):
        pos = get_pos()
        print(f"\n--- TESTING COLUMN {col} at {pos} ---")
        
        # Ensure we are at (col, 23)
        while pos[0] != col or pos[1] != 23:
            if pos[1] > 23:
                # Walk Up to 23
                pos = walk_step_robust("Up")
            elif pos[1] < 23:
                # Walk Down to 23
                pos = walk_step_robust("Down")
            elif pos[0] < col:
                # Walk Right to col
                pos = walk_step_robust("Right")
            elif pos[0] > col:
                # Walk Left to col
                pos = walk_step_robust("Left")
                
        # Try to walk DOWN to Row 24
        print(f"Attempting Down from Row 23 on Column {col}...")
        new_pos = walk_step_robust("Down")
        if new_pos is not None and new_pos[1] == 24:
            print(f"Column {col} allows DOWN to Row 24! Attempting Row 25...")
            new_pos = walk_step_robust("Down")
            if new_pos is not None and new_pos[1] == 25:
                print(f"Column {col} allows DOWN to Row 25! Attempting Row 26...")
                new_pos = walk_step_robust("Down")
                if new_pos is not None and new_pos[1] == 26:
                    print(f"SUCCESS!!! COLUMN {col} IS THE OPEN PASSAGE TO ROW 26!")
                    print(f"Final coordinates: {get_pos()}")
                    return
                else:
                    print(f"Blocked at Row 25 -> 26 on Column {col}.")
            else:
                print(f"Blocked at Row 24 -> 25 on Column {col}.")
        else:
            print(f"Blocked at Row 23 -> 24 on Column {col}.")
            
    print("Search finished, no open column found between 4 and 17.")

if __name__ == "__main__":
    main()
