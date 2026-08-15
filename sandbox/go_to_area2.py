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
        
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 450"])
    
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
        
    if new_pos != pos:
        return new_pos
        
    print("Position didn't change, pressing B...")
    bridge.press_buttons(["B", "sleep 200"])
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
    if new_pos != pos:
        return new_pos
        
    return handle_textbox_or_battle()

def walk_path(path_steps):
    for i, step in enumerate(path_steps):
        print(f"\nStep {i+1}/{len(path_steps)}: {step}")
        pos = get_pos()
        if pos is None:
            handle_textbox_or_battle()
            pos = get_pos()
            
        stuck_count = 0
        while True:
            new_pos = walk_step_robust(step)
            if new_pos is not None and new_pos != pos:
                break
            stuck_count += 1
            if stuck_count > 3:
                print("Extremely stuck! Pressing B and retrying...")
                bridge.press_buttons(["B", "sleep 500"])
                stuck_count = 0
            time.sleep(0.5)

def main():
    # Clear "Got away safely!"
    print("Clearing initial text box...")
    bridge.press_buttons(["B", "sleep 300"])
    
    # Path from (20, 23) in Area 1 (East) to Area 2 (North)
    path = (
        ["Up"] * 3 +
        ["Left"] * 8 +
        ["Down"] * 2 +
        ["Left"] * 4 +
        ["Up"] * 14 +
        ["Right"] * 4 +
        ["Up"] * 2 +
        ["Right"] * 5 +
        ["Down"] * 2 +
        ["Right"] * 3 +
        ["Up"] * 5 +
        ["Left"] * 13 +
        ["Down"] * 2 +
        ["Left"] * 7
    )
    
    walk_path(path)
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position at end of go_to_area2: {pos}")

if __name__ == "__main__":
    main()
