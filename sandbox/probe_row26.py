import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    print("Coordinates are None. Handling potential battle or dialog...")
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 150"])
    print("Attempting to RUN from battle...")
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 150"])
    return get_pos()

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return handle_textbox_or_battle()
        
    bridge.press_buttons([direction, "sleep 400"])
    
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
        
    return new_pos

def main():
    print("Mapping Row 25/26 access from Row 23...")
    # Starting at (8, 23).
    # We will walk Right along Row 23 from Column 8 to Column 20.
    # At each column, we will try to step Down to Row 26.
    
    open_paths = []
    
    for col in range(8, 21):
        # Navigate to (col, 23)
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
            if pos is None:
                continue
                
        # If we got into a battle and our position changed, navigate back to Row 23
        if pos[1] != 23:
            print(f"Off track at {pos}, returning to Row 23...")
            if pos[1] < 23:
                walk_step_robust("Down")
            else:
                walk_step_robust("Up")
            continue
            
        # Walk horizontally to the target column on Row 23
        while pos[0] < col:
            pos = walk_step_robust("Right")
            if pos is None:
                pos = handle_textbox_or_battle()
            if pos is None or pos[0] >= col:
                break
                
        pos = get_pos()
        if pos is None:
            continue
            
        print(f"At ({pos[0]}, 23). Probing Down...")
        # Try to step Down to Row 24
        new_pos = walk_step_robust("Down")
        if new_pos is not None and new_pos[1] == 24:
            print(f"-> Column {pos[0]} is open on Row 24!")
            # Try to step Down to Row 25
            new_pos2 = walk_step_robust("Down")
            if new_pos2 is not None and new_pos2[1] == 25:
                print(f"-> Column {pos[0]} is open on Row 25!")
                # Try to step Down to Row 26
                new_pos3 = walk_step_robust("Down")
                if new_pos3 is not None and new_pos3[1] == 26:
                    print(f"-> SUCCESS! Column {pos[0]} is completely open to Row 26!")
                    open_paths.append(pos[0])
                    # Step back Up
                    walk_step_robust("Up")
                walk_step_robust("Up")
            walk_step_robust("Up")
        else:
            print(f"-> Column {pos[0]} is blocked on Row 24.")
            
        time.sleep(0.2)
        
    print(f"Probing complete. Completely open columns to Row 26: {open_paths}")

if __name__ == "__main__":
    main()
