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
    print("Probing path to Row 26...")
    # Start at current position (should be (19, 24))
    pos = get_pos()
    print(f"Starting probe at: {pos}")
    
    # We want to check columns to the right: 20, 21, 22, 23, 24...
    # Let's walk right to (21, 24)
    for col in range(pos[0], 25):
        print(f"Currently at {get_pos()}")
        # Try to walk down from here
        print(f"Probing DOWN from {get_pos()}...")
        success, p = try_move("Down")
        if success:
            print(f"SUCCESS! Walked DOWN to {p}")
            # Walk back UP to stay on Row 24 for probing
            walk_step_robust("Up")
        else:
            print(f"DOWN is BLOCKED at column {get_pos()[0]}")
            
        # Move right to next column
        print(f"Moving Right...")
        success, p = try_move("Right")
        if not success:
            print(f"Could not move Right from {get_pos()}")
            break
            
    # Let's see final position
    pos = get_pos()
    print(f"Final probe position: {pos}")

if __name__ == "__main__":
    main()
