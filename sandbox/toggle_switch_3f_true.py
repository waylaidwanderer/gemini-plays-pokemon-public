import mgba
import time

def handle_battle_or_text():
    print("Coordinates did not change. Checking for battle or text box...")
    # Press B to dismiss any dialogue or text
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # Try the run sequence: Down, Right, A (navigates to RUN from FIGHT)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    
    # Dismiss any "Can't escape" or extra battle messages
    mgba.press_buttons(["B"])
    time.sleep(0.5)

def move_step(direction, tx, ty):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
        
    print(f"Moving {direction} towards ({tx}, {ty}) from {pos}...")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    new_pos = mgba.get_coordinates()
    
    attempts = 0
    while new_pos != {'x': tx, 'y': ty} and attempts < 10:
        if new_pos == pos:
            # We didn't move at all. Battle, dialogue, or wall.
            print("Did not move. Attempting to handle battle/text...")
            handle_battle_or_text()
            # Try moving again
            mgba.press_buttons([direction])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        else:
            # We moved, but not to the target tile (maybe we wandered off?)
            print(f"Moved to unexpected position {new_pos}. Trying to correct...")
            # We will try to step in the direction of the target
            pos = new_pos
            mgba.press_buttons([direction])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        attempts += 1
        
    return new_pos == {'x': tx, 'y': ty}

def main():
    print("Starting route from (12, 11) to true 3F switch at (2, 11)...")
    
    # 1. Walk Left to (10, 11)
    path = [
        ("Left", 11, 11),
        ("Left", 10, 11),
        # 2. Walk Down to (10, 13)
        ("Down", 10, 12),
        ("Down", 10, 13),
        # 3. Walk Left to (7, 13)
        ("Left", 9, 13),
        ("Left", 8, 13),
        ("Left", 7, 13),
        # 4. Walk Up to (7, 11)
        ("Up", 7, 12),
        ("Up", 7, 11),
        # 5. Walk Left to (4, 11)
        ("Left", 6, 11),
        ("Left", 5, 11),
        ("Left", 4, 11),
        # 6. Walk Down to (4, 13)
        ("Down", 4, 12),
        ("Down", 4, 13),
        # 7. Walk Left to (1, 13)
        ("Left", 3, 13),
        ("Left", 2, 13),
        ("Left", 1, 13),
        # 8. Walk Up to (1, 11)
        ("Up", 1, 12),
        ("Up", 1, 11),
    ]
    
    success = True
    for direction, tx, ty in path:
        if not move_step(direction, tx, ty):
            print(f"Failed at step to ({tx}, {ty})!")
            success = False
            break
            
    if success:
        print("Successfully reached (1, 11)! Toggling true switch at (2, 11)...")
        # Face Right and press A to toggle
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        # Dismiss the switch text box and press Yes
        print("Pressing A to confirm switch activation...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Take a final screenshot
        mgba.take_screenshot()
        print("Done!")
    else:
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
