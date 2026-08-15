import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    print("No movement detected. Checking for text box or battle...")
    bridge.press_buttons(["B", "sleep 200", "B", "sleep 200"])
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
    # Start at current position (13, 24)
    pos = get_pos()
    print(f"Starting search for Columns 14-17 from current pos: {pos}")
    
    for col in range(14, 18):
        pos = get_pos()
        print(f"\n--- TESTING COLUMN {col} at {pos} ---")
        
        # Ensure we are at (col, 23)
        while pos[0] != col or pos[1] != 23:
            if pos[1] > 23:
                pos = walk_step_robust("Up")
            elif pos[1] < 23:
                pos = walk_step_robust("Down")
            elif pos[0] < col:
                pos = walk_step_robust("Right")
            elif pos[0] > col:
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
            
    print("Search finished, no open column found between 14 and 17.")

if __name__ == "__main__":
    main()
