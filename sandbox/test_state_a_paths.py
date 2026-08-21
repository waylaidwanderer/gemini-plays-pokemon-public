import mgba
import time

def walk_and_test_state_a():
    print("Clearing text and walking to Column 10 in State A...")
    
    # 1. Clear text
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"Current overworld position: {pos}")
    
    # 2. Walk Right from (3, 11) to (9, 11)
    if pos == {'x': 3, 'y': 11}:
        for _ in range(6):
            mgba.press_buttons(["Right"])
            time.sleep(0.5)
        pos = mgba.get_coordinates()
        print(f"At (9, 11): {pos}")
        
    # 3. Walk Right to (10, 11)
    if pos == {'x': 9, 'y': 11}:
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        pos = mgba.get_coordinates()
        print(f"At Column 10: {pos}")
        
    # 4. Walk Up Column 10 to Row 6
    if pos == {'x': 10, 'y': 11}:
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
            
        print(f"At North-East: {mgba.get_coordinates()}")
        
        # Test Left along Row 6
        print("Testing Row 6 LEFT...")
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        pos_r6 = mgba.get_coordinates()
        print(f"Position after Left from (10, 6): {pos_r6}")
        if pos_r6 == {'x': 9, 'y': 6}:
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
    print(f"Final screenshot: {scr}")

walk_and_test_state_a()
