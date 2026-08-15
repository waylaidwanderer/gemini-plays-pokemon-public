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
    # Start at (19, 24)
    # We want to walk Right along Row 24 (up to Col 29)
    # At each column, try to walk DOWN.
    # If we manage to walk down (y > 24), we succeed and stop!
    
    start_pos = get_pos()
    print(f"Grid search started from: {start_pos}")
    
    current_col = start_pos[0]
    while current_col < 29:
        # Try to walk Down
        pos = get_pos()
        print(f"Trying to walk Down from {pos}...")
        new_pos = walk_step_robust("Down")
        if new_pos is not None and new_pos[1] > 24:
            print(f"SUCCESS! Walked Down to {new_pos}")
            return
            
        # If we couldn't walk Down, walk Right
        pos = get_pos()
        if pos[0] >= 29:
            break
            
        print(f"Walking Right from {pos}...")
        new_pos = walk_step_robust("Right")
        if new_pos is not None and new_pos != pos:
            current_col = new_pos[0]
        else:
            print("Could not walk Right, stuck!")
            break
            
    print(f"Finished search. Final pos: {get_pos()}")

if __name__ == "__main__":
    main()
