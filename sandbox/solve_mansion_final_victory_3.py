import mgba
import time

def align_to(tx, ty):
    # Align to tx, ty using a simple rule-based approach
    # 1. Align x to tx if we are on row 13
    pos = mgba.get_coordinates()
    while pos['y'] == 13 and pos['x'] != tx:
        d = "Right" if pos['x'] < tx else "Left"
        mgba.press_buttons([d, "sleep 120"])
        pos = mgba.get_coordinates()
        
    # 2. Align y to ty if we are on column tx
    while pos['x'] == tx and pos['y'] != ty:
        d = "Down" if pos['y'] < ty else "Up"
        mgba.press_buttons([d, "sleep 120"])
        pos = mgba.get_coordinates()
        
    return pos['x'] == tx and pos['y'] == ty

def walk_from_west_to_east():
    # From current position on row 13 (or similar) to (21, 6)
    # Step 1: Walk to (9, 13)
    pos = mgba.get_coordinates()
    print("West-to-East path start position:", pos)
    
    # Get onto row 13 if we are at (2, 12)
    if pos == {'x': 2, 'y': 12}:
        mgba.press_buttons(["Down", "sleep 150"])
        pos = mgba.get_coordinates()
        
    # Row 13: walk to column 9
    while pos['y'] == 13 and pos['x'] < 9:
        mgba.press_buttons(["Right", "sleep 120"])
        pos = mgba.get_coordinates()
    print("At column 9:", pos)
    
    # Column 9: walk Up to row 10
    while pos['x'] == 9 and pos['y'] > 10:
        mgba.press_buttons(["Up", "sleep 120"])
        pos = mgba.get_coordinates()
    print("At row 10:", pos)
    
    # Row 10: walk Right to column 12
    while pos['y'] == 10 and pos['x'] < 12:
        mgba.press_buttons(["Right", "sleep 120"])
        pos = mgba.get_coordinates()
    print("At column 12:", pos)
    
    # Column 12: walk Up to row 6
    while pos['x'] == 12 and pos['y'] > 6:
        mgba.press_buttons(["Up", "sleep 120"])
        pos = mgba.get_coordinates()
    print("At row 6:", pos)
    
    # Row 6: walk Right to column 21
    while pos['y'] == 6 and pos['x'] < 21:
        mgba.press_buttons(["Right", "sleep 120"])
        pos = mgba.get_coordinates()
    print("At column 21:", pos)
    
    return pos == {'x': 21, 'y': 6}

def walk_from_east_to_west():
    # From (21, 6) back to (2, 12)
    pos = mgba.get_coordinates()
    print("East-to-West path start position:", pos)
    
    # Row 6: walk Left to column 12
    while pos['y'] == 6 and pos['x'] > 12:
        mgba.press_buttons(["Left", "sleep 120"])
        pos = mgba.get_coordinates()
        
    # Column 12: walk Down to row 10
    while pos['x'] == 12 and pos['y'] < 10:
        mgba.press_buttons(["Down", "sleep 120"])
        pos = mgba.get_coordinates()
        
    # Row 10: walk Left to column 9
    while pos['y'] == 10 and pos['x'] > 9:
        mgba.press_buttons(["Left", "sleep 120"])
        pos = mgba.get_coordinates()
        
    # Column 9: walk Down to row 13
    while pos['x'] == 9 and pos['y'] < 13:
        mgba.press_buttons(["Down", "sleep 120"])
        pos = mgba.get_coordinates()
        
    # Row 13: walk Left to column 2
    while pos['y'] == 13 and pos['x'] > 2:
        mgba.press_buttons(["Left", "sleep 120"])
        pos = mgba.get_coordinates()
        
    # Column 2: walk Up to row 12
    if pos['x'] == 2 and pos['y'] == 13:
        mgba.press_buttons(["Up", "sleep 150"])
        pos = mgba.get_coordinates()
        
    return pos == {'x': 2, 'y': 12}

def toggle_switch():
    print("Toggling Mewtwo statue switch at (2, 11)...")
    mgba.press_buttons(["Up", "sleep 300"])
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 500", "B", "sleep 500"])
    print("Switch toggle sequence executed.")

def walk_to_pit_and_drop():
    # From (21, 5), walk to (26, 6)
    pos = mgba.get_coordinates()
    
    # Column 21: walk Up to row 3
    while pos['x'] == 21 and pos['y'] > 3:
        mgba.press_buttons(["Up", "sleep 120"])
        pos = mgba.get_coordinates()
        
    # Row 3: walk Right to column 26
    while pos['y'] == 3 and pos['x'] < 26:
        mgba.press_buttons(["Right", "sleep 120"])
        pos = mgba.get_coordinates()
        
    # Column 26: walk Down to row 6
    while pos['x'] == 26 and pos['y'] < 6:
        mgba.press_buttons(["Down", "sleep 120"])
        pos = mgba.get_coordinates()
        
    if pos == {'x': 26, 'y': 6}:
        print("At pit entry (26, 6). Stepping Left into the pit...")
        mgba.press_buttons(["Left", "sleep 3000"]) # Wait for falling animation
        final_pos = mgba.get_coordinates()
        print("Landed on floor! Position:", final_pos)
        mgba.take_screenshot()
    else:
        print("Failed to reach (26, 6) for pit entry! Position:", pos)

def main():
    pos = mgba.get_coordinates()
    print("Starting master victory script 3 at:", pos)
    
    # Walk to (21, 6)
    if not walk_from_west_to_east():
        print("Failed to reach (21, 6)!")
        mgba.take_screenshot()
        return
        
    pos = mgba.get_coordinates()
    print("At gate checkpoint! Position:", pos)
    
    # Attempt to step UP to (21, 5) to test the gate
    print("Testing gate at (21, 5)...")
    mgba.press_buttons(["Up", "sleep 150"])
    pos = mgba.get_coordinates()
    
    if pos == {'x': 21, 'y': 5}:
        print("Gate is OPEN! We are in State B.")
    else:
        print("Gate is CLOSED! We are in State A. Toggling switch...")
        # Walk back to (2, 12)
        if not walk_from_east_to_west():
            print("Failed to walk back to the switch landing!")
            mgba.take_screenshot()
            return
            
        toggle_switch()
        
        # Walk back to (21, 6)
        if not walk_from_west_to_east():
            print("Failed to walk back to the gate checkpoint!")
            mgba.take_screenshot()
            return
            
        # Step UP to (21, 5)
        print("Stepping UP to (21, 5)...")
        mgba.press_buttons(["Up", "sleep 150"])
        pos = mgba.get_coordinates()
        if pos != {'x': 21, 'y': 5}:
            print("Failed to pass gate even after toggle!")
            mgba.take_screenshot()
            return
            
    # Walk to the pit and drop
    walk_to_pit_and_drop()

if __name__ == "__main__":
    main()
