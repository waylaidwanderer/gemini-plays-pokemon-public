import mgba
import time

def test_state_a():
    print("Testing B1F paths in State A...")
    
    # Currently at (1, 11)
    # 1. Walk to (3, 11) via Row 12
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    mgba.press_buttons(["Right", "Right"])
    time.sleep(1.0)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print(f"At (3, 11): {mgba.get_coordinates()}")
    
    # 2. Walk Right to (9, 11)
    for _ in range(6):
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
    print(f"At (9, 11): {mgba.get_coordinates()}")
    
    # 3. Walk Right to (10, 11)
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    pos = mgba.get_coordinates()
    print(f"At Column 10: {pos}")
    
    if pos == {'x': 10, 'y': 11}:
        # 4. Walk Up Column 10 to Row 6
        print("Walking Up Column 10...")
        for step in range(1, 6):
            mgba.press_buttons(["Up"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            print(f"Step {step} UP: {new_pos}")
            if new_pos == pos:
                print(f"Blocked at {pos} on step {step} UP")
                break
            pos = new_pos
            
        # We should be at (10, 6)
        print(f"At North-East corner: {mgba.get_coordinates()}")
        
        # Test Left along Row 6
        print("Testing Row 6 LEFT...")
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        pos_r6 = mgba.get_coordinates()
        print(f"Position after Left from (10, 6): {pos_r6}")
        if pos_r6 == {'x': 9, 'y': 6}:
            # If open, walk back to (10, 6)
            mgba.press_buttons(["Right"])
            time.sleep(0.5)
            
        # Walk Up to (10, 5) and test Left along Row 5
        print("Testing Row 5 LEFT...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        pos_r5_start = mgba.get_coordinates()
        print(f"Position at row 5: {pos_r5_start}")
        if pos_r5_start == {'x': 10, 'y': 5}:
            mgba.press_buttons(["Left"])
            time.sleep(0.5)
            pos_r5 = mgba.get_coordinates()
            print(f"Position after Left from (10, 5): {pos_r5}")
            
    scr = mgba.take_screenshot()
    print(f"Screenshot at end: {scr}")

test_state_a()
