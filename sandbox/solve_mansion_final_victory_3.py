import mgba
import time

def step_to(direction, tx, ty):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
        
    print(f"At {pos}. Moving {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction, "sleep 120"])
    new_pos = mgba.get_coordinates()
    
    attempts = 0
    while new_pos != {'x': tx, 'y': ty} and attempts < 2:
        if new_pos == pos:
            print("Did not move. Retrying direction...")
            mgba.press_buttons([direction, "sleep 120"])
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print(f"Blocked! Cannot move {direction} to ({tx}, {ty}) from {pos}.")
                return False
        else:
            print(f"Unexpected pos {new_pos}. Correcting...")
            pos = new_pos
            mgba.press_buttons([direction, "sleep 120"])
            new_pos = mgba.get_coordinates()
        attempts += 1
        
    return new_pos == {'x': tx, 'y': ty}

def walk_path(path):
    for d, tx, ty in path:
        if not step_to(d, tx, ty):
            return False
    return True

def toggle_switch():
    print("Toggling Mewtwo statue switch at (2, 11)...")
    # Face UP
    mgba.press_buttons(["Up", "sleep 300"])
    # Press A, sleep, A, sleep, B, sleep
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 500", "B", "sleep 500"])
    print("Switch toggle sequence executed.")

def main():
    pos = mgba.get_coordinates()
    print("Starting master victory script at:", pos)
    
    # Target: Walk to the gate checkpoint at (21, 6)
    path_to_gate_checkpoint = [
        ("Down", 2, 13),
        ("Right", 3, 13), ("Right", 4, 13), ("Right", 5, 13), ("Right", 6, 13), ("Right", 7, 13), ("Right", 8, 13), ("Right", 9, 13),
        ("Up", 9, 12), ("Up", 9, 11), ("Up", 9, 10),
        ("Right", 10, 10), ("Right", 11, 10), ("Right", 12, 10),
        ("Up", 12, 9), ("Up", 12, 8), ("Up", 12, 7), ("Up", 12, 6),
        ("Right", 13, 6), ("Right", 14, 6), ("Right", 15, 6), ("Right", 16, 6), ("Right", 17, 6), ("Right", 18, 6), ("Right", 19, 6), ("Right", 20, 6), ("Right", 21, 6),
    ]
    
    # If we are starting at (2, 12), walk the path to (21, 6)
    if pos == {'x': 2, 'y': 12}:
        if not walk_path(path_to_gate_checkpoint):
            print("Failed to reach the gate checkpoint at (21, 6)!")
            mgba.take_screenshot()
            return
            
    pos = mgba.get_coordinates()
    print("At gate checkpoint! Position:", pos)
    
    # Attempt to move UP to (21, 5) (testing if gate at (21, 5) is open/State B)
    print("Attempting to step UP to (21, 5) to test the gate...")
    mgba.press_buttons(["Up", "sleep 200"])
    pos = mgba.get_coordinates()
    
    if pos == {'x': 21, 'y': 5}:
        print("Gate is OPEN! We are in State B.")
    else:
        print("Gate is CLOSED! We are in State A. Need to toggle the switch.")
        # Walk back to (2, 12)
        path_back_to_switch = [
            ("Left", 20, 6), ("Left", 19, 6), ("Left", 18, 6), ("Left", 17, 6), ("Left", 16, 6), ("Left", 15, 6), ("Left", 14, 6), ("Left", 13, 6), ("Left", 12, 6),
            ("Down", 12, 7), ("Down", 12, 8), ("Down", 12, 9), ("Down", 12, 10),
            ("Left", 11, 10), ("Left", 10, 10), ("Left", 9, 10),
            ("Down", 9, 11), ("Down", 9, 12), ("Down", 9, 13),
            ("Left", 8, 13), ("Left", 7, 13), ("Left", 6, 13), ("Left", 5, 13), ("Left", 4, 13), ("Left", 3, 13), ("Left", 2, 13),
            ("Up", 2, 12)
        ]
        if not walk_path(path_back_to_switch):
            print("Failed to walk back to the switch landing!")
            mgba.take_screenshot()
            return
            
        # Toggle the switch
        toggle_switch()
        
        # Walk back to the gate checkpoint at (21, 6)
        if not walk_path(path_to_gate_checkpoint):
            print("Failed to walk back to the gate checkpoint after toggle!")
            mgba.take_screenshot()
            return
            
        # Now step UP to (21, 5) (this time it must be open!)
        print("Stepping UP to (21, 5) now...")
        if not step_to("Up", 21, 5):
            print("Failed to pass the gate even after toggle!")
            mgba.take_screenshot()
            return
            
    # From (21, 5), walk to the pit at (25, 6)
    path_to_pit = [
        ("Up", 21, 4), ("Up", 21, 3),
        ("Right", 22, 3), ("Right", 23, 3), ("Right", 24, 3), ("Right", 25, 3), ("Right", 26, 3),
        ("Down", 26, 4), ("Down", 26, 5), ("Down", 26, 6),
    ]
    if not walk_path(path_to_pit):
        print("Failed to reach the pit!")
        mgba.take_screenshot()
        return
        
    print("At pit entry (26, 6). Stepping Left into the pit...")
    mgba.press_buttons(["Left", "sleep 3000"]) # Wait 3s for falling animation
    
    final_pos = mgba.get_coordinates()
    print("Landed on floor! Position:", final_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
