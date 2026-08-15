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
    print("Mapping Row 25 to find open columns...")
    # We are at (19, 24).
    # Let's walk Left along Row 24 and try to step Down at each column.
    # We will go from Column 19 down to Column 2.
    
    open_columns = []
    
    # First, let's go left. We need to handle blocks on Row 24 (e.g. Columns 16-17 are blocked).
    # If we hit a block while walking Left, we will detour Up to Row 23, walk Left, and come back Down to Row 24.
    
    col = 19
    while col >= 2:
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
            if pos is None:
                continue
                
        # Update current column
        col = pos[0]
        row = pos[1]
        print(f"At ({col}, {row}). Probing Down...")
        
        # Test Down
        new_pos = walk_step_robust("Down")
        if new_pos is not None and new_pos[1] > row:
            print(f"-> Column {col} is OPEN to the south! Position reached: {new_pos}")
            open_columns.append(col)
            # Step back Up to continue probing
            walk_step_robust("Up")
        else:
            print(f"-> Column {col} is BLOCKED.")
            
        # Try to walk Left to the next column
        print(f"Trying to walk Left from ({col}, {row})...")
        new_pos = walk_step_robust("Left")
        if new_pos is not None and new_pos[0] < col:
            # Succeeded walking Left
            continue
        else:
            # Blocked walking Left! Let's try to detour Up to Row 23, walk Left, and come back Down
            print("Blocked walking Left. Detouring Up...")
            new_pos = walk_step_robust("Up")
            if new_pos is not None and new_pos[1] < row:
                # Walk Left on Row 23
                print("Walking Left on Row 23...")
                new_pos = walk_step_robust("Left")
                # Try to come back Down
                print("Stepping back Down to Row 24...")
                walk_step_robust("Down")
            else:
                print("Could not detour Up! We might be stuck or blocked.")
                break
                
        time.sleep(0.2)
        
    print(f"Probing complete. Open columns on Row 25: {open_columns}")

if __name__ == "__main__":
    main()
