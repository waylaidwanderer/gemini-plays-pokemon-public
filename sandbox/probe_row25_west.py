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
    print("Mapping Row 25 West from (29, 23) to find open columns...")
    
    # We are at (29, 23).
    # Let's walk Left along Row 23 and try to step Down at each column.
    # We will go from Column 29 down to Column 2.
    
    open_columns = []
    
    col = 29
    while col >= 2:
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
            if pos is None:
                continue
                
        col = pos[0]
        row = pos[1]
        
        # Ensure we are on Row 23
        if row != 23:
            print(f"Warning: on row {row}, detouring to Row 23...")
            if row < 23:
                walk_step_robust("Down")
            else:
                walk_step_robust("Up")
            continue
            
        print(f"At ({col}, {row}). Probing Down...")
        
        # Test Down 1 step (to Row 24)
        new_pos = walk_step_robust("Down")
        if new_pos is not None and new_pos[1] == 24:
            print(f"-> Column {col} is OPEN to Row 24!")
            # Test Down another step (to Row 25)
            new_pos2 = walk_step_robust("Down")
            if new_pos2 is not None and new_pos2[1] == 25:
                print(f"-> Column {col} is OPEN to Row 25!")
                # Test Down another step (to Row 26)
                new_pos3 = walk_step_robust("Down")
                if new_pos3 is not None and new_pos3[1] == 26:
                    print(f"-> SUCCESS! Column {col} is completely OPEN to Row 26! Position reached: {new_pos3}")
                    open_columns.append(col)
                    # Step back Up to continue probing
                    walk_step_robust("Up")
                walk_step_robust("Up")
            walk_step_robust("Up")
        else:
            print(f"-> Column {col} is BLOCKED at Row 24.")
            
        # Try to walk Left to the next column on Row 23
        print(f"Trying to walk Left from ({col}, 23)...")
        new_pos = walk_step_robust("Left")
        if new_pos is not None and new_pos[0] < col:
            # Succeeded walking Left
            continue
        else:
            # Blocked walking Left! Let's try to detour Up to Row 22, walk Left, and come back Down
            print("Blocked walking Left. Detouring Up to Row 22...")
            new_pos = walk_step_robust("Up")
            if new_pos is not None and new_pos[1] == 22:
                # Walk Left on Row 22
                print("Walking Left on Row 22...")
                new_pos_left = walk_step_robust("Left")
                if new_pos_left is not None and new_pos_left[0] < col:
                    # Try to come back Down
                    print("Stepping back Down to Row 23...")
                    walk_step_robust("Down")
                else:
                    print("Could not walk Left even on Row 22! Breaking.")
                    break
            else:
                print("Could not detour Up! We might be stuck or blocked.")
                break
                
        time.sleep(0.2)
        
    print(f"Probing complete. Open columns on Row 25 West: {open_columns}")

if __name__ == "__main__":
    main()
