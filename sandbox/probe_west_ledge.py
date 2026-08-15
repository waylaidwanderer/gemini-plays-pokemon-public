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
    print("Probing western ground level for south-facing ledges on Row 23...")
    # We are at (8, 23).
    # Probe DOWN on Column 8, 7, 6, 5, 4, 3...
    for col in range(8, 2, -1):
        print(f"\nProbing DOWN at column {get_pos()[0]} Row {get_pos()[1]}...")
        success, p = try_move("Down")
        if success:
            print(f"SUCCESS! Walked DOWN to {p}")
            # Try to walk DOWN again
            success2, p2 = try_move("Down")
            if success2:
                print(f"SUCCESS! Walked DOWN to {p2}")
                walk_step_robust("Up")
            walk_step_robust("Up")
        else:
            print("DOWN is BLOCKED")
            
        # Move Left to next column
        print("Moving Left...")
        success, p = try_move("Left")
        if not success:
            print(f"Blocked going Left at {get_pos()}")
            break
            
    print(f"\nFinal probe position: {get_pos()}")

if __name__ == "__main__":
    main()
