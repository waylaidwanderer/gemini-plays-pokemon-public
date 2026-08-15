import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    print("Coordinates are None. Handling potential battle or dialog...")
    # Clear text boxes with B
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 150"])
    
    # Try to RUN
    print("Attempting to RUN from battle...")
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    
    # Clear post-flee text
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 150"])
        
    pos = get_pos()
    print(f"Coordinates after battle handling: {pos}")
    return pos

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return handle_textbox_or_battle()
        
    bridge.press_buttons([direction, "sleep 450"])
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
    return new_pos

def try_move(direction):
    pos = get_pos()
    new_pos = walk_step_robust(direction)
    if new_pos == pos:
        return False, new_pos
    return True, new_pos

def main():
    print("Probing all columns to find a way to Row 26...")
    # We are at (17, 23).
    # First, let's try to walk RIGHT and probe Column 18, 19, 20, 21, 22 on Row 23
    # Wait, we know Column 18 is a vertical wall of bushes on Row 23.
    # So we must go UP to Row 22 to walk past Column 18!
    walk_step_robust("Up") # to (17, 22)
    print(f"Current: {get_pos()}")
    
    # Walk RIGHT to Column 21 Row 22
    for _ in range(4):
        walk_step_robust("Right")
    print(f"Current: {get_pos()}") # should be (21, 22)
    
    # Now probe DOWN on Column 21, 22, 23, 24, 25, 26, 27, 28, 29...
    for col in range(21, 30):
        print(f"\nProbing DOWN at column {get_pos()[0]} Row {get_pos()[1]}...")
        success, p = try_move("Down")
        if success:
            print(f"SUCCESS! Walked DOWN to {p}")
            # Try to walk DOWN more
            success2, p2 = try_move("Down")
            if success2:
                print(f"SUCCESS! Walked DOWN to {p2}")
                # Walk back UP
                walk_step_robust("Up")
            walk_step_robust("Up")
        else:
            print(f"DOWN is BLOCKED")
            
        # Move Right to next column
        print("Moving Right...")
        success, p = try_move("Right")
        if not success:
            print(f"Blocked going Right at {get_pos()}")
            break
            
    # Now let's go back and probe the WEST side: Columns 2 to 16
    # Let's walk LEFT to Column 10 Row 22
    pos = get_pos()
    print(f"\nFinal eastern probe position: {pos}")

if __name__ == "__main__":
    main()
