import mgba
import time

def step_to(direction, tx, ty):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
        
    print(f"At {pos}. Moving {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    new_pos = mgba.get_coordinates()
    
    # If we didn't move, try pressing the direction a second time (handles turning in place).
    if new_pos == pos:
        print("Did not move. Turning? Pressing direction again...")
        mgba.press_buttons([direction])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        
        # If we STILL didn't move, we are blocked by a wall or battle!
        # Exit cleanly to let the player handle it and prevent blind drift.
        if new_pos == pos:
            print(f"Blocked! Cannot move {direction} to ({tx}, {ty}) from {pos}. Exiting script to prevent drift.")
            return False
            
    return new_pos == {'x': tx, 'y': ty}

def follow_path(path):
    for direction, tx, ty in path:
        if not step_to(direction, tx, ty):
            return False
    return True

def main():
    print("Starting absolute master route to B1F starting from (6, 11) in State A...")
    
    # Dismiss 'Got away safely!' text if any
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # We should be at (6, 11) on 3F
    if pos != {'x': 6, 'y': 11}:
        print("Warning: not at (6, 11). Re-aligning...")
        if pos['y'] != 11:
            step_to("Down" if pos['y'] < 11 else "Up", pos['x'], 11)
        pos = mgba.get_coordinates()
        if pos['x'] != 6:
            step_to("Left" if pos['x'] > 6 else "Right", 6, 11)
            
    # 1. Walk from (6, 11) to switch at (2, 12) on 3F in State A
    print("--- 3F (State A): Walking to switch at (2, 12) ---")
    path_to_switch = [
        ("Left", 5, 11),
        ("Left", 4, 11),
        ("Left", 3, 11),
        ("Left", 2, 11),
        ("Down", 2, 12),
    ]
    if not follow_path(path_to_switch):
        mgba.take_screenshot()
        return
        
    # Toggle switch to State B
    print("Facing Up to toggle switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Toggling switch to State B...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"]) # YES
    time.sleep(1.0)
    mgba.press_buttons(["B"]) # Close dialogue
    time.sleep(1.0)
    
    # 2. Walk to Pit on 3F (State B) and fall
    print("--- 3F (State B): Walking to Pit ---")
    path_to_pit = [
        ("Right", 3, 12),
        ("Right", 4, 12),
        ("Right", 5, 12),
        ("Right", 6, 12),
        ("Right", 7, 12),
        ("Down", 7, 13),
        ("Right", 8, 13),
        ("Right", 9, 13),
        ("Up", 9, 12),
        ("Up", 9, 11),
        ("Up", 9, 10),
        ("Right", 10, 10), # Column 10 Row 10 is OPEN!
        ("Right", 11, 10),
        ("Right", 12, 10), # Walk to Column 12 to bypass rubble at Column 11 Row 8!
        ("Up", 12, 9),
        ("Up", 12, 8),
        ("Up", 12, 7),
        ("Up", 12, 6),
        ("Up", 12, 5), # Up Column 12 to Row 5
        ("Right", 13, 5),
        ("Right", 14, 5),
        ("Right", 15, 5),
        ("Right", 16, 5),
        ("Right", 17, 5),
        ("Right", 18, 5),
        ("Right", 19, 5),
        ("Right", 20, 5),
        ("Right", 21, 5), # Gate (21, 5) is OPEN in State B!
        ("Up", 21, 4),
        ("Up", 21, 3),
        ("Right", 22, 3),
        ("Right", 23, 3),
        ("Right", 24, 3),
        ("Right", 25, 3),
        ("Right", 26, 3), # Bypasses row 4 wall at cols 22-25
        ("Down", 26, 4),
        ("Down", 26, 5),
        ("Down", 26, 6), # Column 26 Row 6
    ]
    if not follow_path(path_to_pit):
        mgba.take_screenshot()
        return
        
    print("At (26, 6). Stepping Left onto the pit at (25, 6)...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0) # wait for falling animation
    
    # We should land on 1F in the fenced area
    print("--- 1F (State B): Landing in fenced area and going to B1F ---")
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print("Landed on 1F! Position:", pos)
    mgba.take_screenshot()
    
    print("Walking onto stairs to B1F...")
    for i in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
    pos = mgba.get_coordinates()
    print("Position after walking UP:", pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
