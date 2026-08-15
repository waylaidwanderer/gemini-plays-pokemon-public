import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    print("Coordinates are None. Handling potential battle or dialog...")
    # Clear any potential wild encounter or entry dialog
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
    
    # Check new position
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
        
    if new_pos != pos:
        return new_pos
        
    # If same, try pressing B to clear potential text block
    print("Position didn't change, pressing B...")
    bridge.press_buttons(["B", "sleep 200"])
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
    if new_pos != pos:
        return new_pos
        
    # Still same? Call battle handler
    return handle_textbox_or_battle()

def walk_path(path_steps):
    for i, step in enumerate(path_steps):
        print(f"\nStep {i+1}/{len(path_steps)}: {step}")
        pos = get_pos()
        if pos is None:
            handle_textbox_or_battle()
            pos = get_pos()
            
        # Try to walk the step robustly
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
    # Phase 2: Area 1 (East) to Area 2 (North)
    # Starting at (0, 22) in Area 1 (East)
    print("Starting Phase 2...")
    phase2_steps = (
        ["Down"] * 2 +
        ["Right"] * 20 +
        ["Up"] * 4 +
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
    walk_path(phase2_steps)
    
    # We should have transitioned to Area 2 (North) at (39, 31)
    # Let's wait a moment and verify position
    time.sleep(2.0)
    pos = get_pos()
    print(f"Position after Phase 2: {pos}")
    
    # Phase 3: Area 2 (North) to Area 3 (West)
    print("Starting Phase 3...")
    phase3_steps = (
        ["Left"] * 17 +
        ["Up"] * 9 +
        ["Left"] * 6 +
        ["Down"] * 6 +
        ["Left"] * 4 +
        ["Down"] * 2 +
        ["Left"] * 4 +
        ["Down"] * 5 +
        ["Down"]
    )
    walk_path(phase3_steps)
    
    # We should have transitioned to Area 3 (West) at (26, 0)
    time.sleep(2.0)
    pos = get_pos()
    print(f"Position after Phase 3: {pos}")
    
    # Phase 4: Area 3 (West) to (19, 24)
    print("Starting Phase 4...")
    phase4_steps = (
        ["Down"] * 2 +
        ["Left"] * 1 +
        ["Down"] * 16 +
        ["Left"] * 4 +
        ["Down"] * 6 +
        ["Left"] * 2
    )
    walk_path(phase4_steps)
    
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final Position: {pos}")
    
if __name__ == "__main__":
    main()
