import mgba
import time

def step_to(direction, tx, ty):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
        
    print(f"At {pos}. Moving {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction, "sleep 100"])
    new_pos = mgba.get_coordinates()
    
    attempts = 0
    while new_pos != {'x': tx, 'y': ty} and attempts < 2:
        if new_pos == pos:
            # If we didn't move, we try pressing the button again (it might have been a turn-in-place)
            print("Did not move. Retrying direction...")
            mgba.press_buttons([direction, "sleep 100"])
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print(f"Blocked! Cannot move {direction} to ({tx}, {ty}) from {pos}.")
                return False
        else:
            print(f"Unexpected pos {new_pos}. Correcting...")
            pos = new_pos
            mgba.press_buttons([direction, "sleep 100"])
            new_pos = mgba.get_coordinates()
        attempts += 1
        
    return new_pos == {'x': tx, 'y': ty}

def main():
    pos = mgba.get_coordinates()
    print("Starting position:", pos)
    
    # Path from (12, 11) to (2, 12) on 3F in State A
    # Row 11 is walkable Left to (4, 11)
    path_to_switch = [
        ("Left", 11, 11),
        ("Left", 10, 11),
        ("Left", 9, 11),
        ("Left", 8, 11),
        ("Left", 7, 11),
        ("Left", 6, 11),
        ("Left", 5, 11),
        ("Left", 4, 11),
        # Go down to row 13 on column 4 (bypassing column 3 green cabinet)
        ("Down", 4, 12),
        ("Down", 4, 13),
        # Walk Left on row 13 to column 2
        ("Left", 3, 13),
        ("Left", 2, 13),
        # Walk Up to (2, 12)
        ("Up", 2, 12)
    ]
    
    for d, tx, ty in path_to_switch:
        if not step_to(d, tx, ty):
            print("Failed to reach the switch!")
            mgba.take_screenshot()
            return
            
    print("Reached switch landing! Facing UP to toggle Mewtwo statue at (2, 11)...")
    mgba.press_buttons(["Up", "sleep 300"])
    
    # Press A to toggle switch
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 500", "B", "sleep 500"])
    print("Toggle complete.")
    
    # Now walk from (2, 12) to (26, 6) in State B
    # Walk Down to row 13, then Right to column 9, then Up column 9 to row 10, Right to column 12
    path_to_pit = [
        ("Down", 2, 13),
        ("Right", 3, 13),
        ("Right", 4, 13),
        ("Right", 5, 13),
        ("Right", 6, 13),
        ("Right", 7, 13),
        ("Right", 8, 13),
        ("Right", 9, 13),
        ("Up", 9, 12),
        ("Up", 9, 11),
        ("Up", 9, 10),
        ("Right", 10, 10),
        ("Right", 11, 10),
        ("Right", 12, 10),
        # Go up column 12 to row 6 (bypassing column 11 row 8 rubble)
        ("Up", 12, 9),
        ("Up", 12, 8),
        ("Up", 12, 7),
        ("Up", 12, 6),
        # Go Right on row 6 to column 21
        ("Right", 13, 6),
        ("Right", 14, 6),
        ("Right", 15, 6),
        ("Right", 16, 6),
        ("Right", 17, 6),
        ("Right", 18, 6),
        ("Right", 19, 6),
        ("Right", 20, 6),
        ("Right", 21, 6),
        # Go up column 21 to row 3 (Gate at (21, 5) is OPEN in State B)
        ("Up", 21, 5),
        ("Up", 21, 4),
        ("Up", 21, 3),
        # Go Right on row 3 to column 26
        ("Right", 22, 3),
        ("Right", 23, 3),
        ("Right", 24, 3),
        ("Right", 25, 3),
        ("Right", 26, 3),
        # Go Down column 26 to row 6
        ("Down", 26, 4),
        ("Down", 26, 5),
        ("Down", 26, 6),
    ]
    
    for d, tx, ty in path_to_pit:
        if not step_to(d, tx, ty):
            print("Failed on the way to the pit!")
            mgba.take_screenshot()
            return
            
    print("At (26, 6). Stepping Left into the pit...")
    mgba.press_buttons(["Left", "sleep 3000"]) # 3s delay to let falling animation finish and load the new floor
    
    final_pos = mgba.get_coordinates()
    print("Landed! Position:", final_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
