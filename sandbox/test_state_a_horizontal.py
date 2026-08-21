import mgba
import time

def test_horizontal_paths_state_a():
    print("Testing B1F horizontal paths on Rows 1-4 in State A...")
    
    # We are at (1, 10) in State A
    # 1. Walk to (3, 11) via Row 11/12
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    mgba.press_buttons(["Right", "Right"])
    time.sleep(1.0)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print(f"At (3, 11): {mgba.get_coordinates()}")
    
    # 2. Walk Right to (10, 11)
    for _ in range(7):
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
    print(f"At (10, 11): {mgba.get_coordinates()}")
    
    # 3. Walk Up Column 10 to Row 4
    for _ in range(7):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
    print(f"At (10, 4): {mgba.get_coordinates()}")
    
    # Test Left along Row 4
    if mgba.get_coordinates() == {'x': 10, 'y': 4}:
        print("Testing Row 4 Left...")
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        print(f"Row 4 Left pos: {mgba.get_coordinates()}")
        if mgba.get_coordinates() == {'x': 9, 'y': 4}:
            # Walk back
            mgba.press_buttons(["Right"])
            time.sleep(0.5)
            
    # Walk to Row 3
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print(f"At (10, 3): {mgba.get_coordinates()}")
    
    # Test Left along Row 3
    if mgba.get_coordinates() == {'x': 10, 'y': 3}:
        print("Testing Row 3 Left...")
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        print(f"Row 3 Left pos: {mgba.get_coordinates()}")
        if mgba.get_coordinates() == {'x': 9, 'y': 3}:
            mgba.press_buttons(["Right"])
            time.sleep(0.5)
            
    # Walk to Row 2
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print(f"At (10, 2): {mgba.get_coordinates()}")
    
    # Test Left along Row 2
    if mgba.get_coordinates() == {'x': 10, 'y': 2}:
        print("Testing Row 2 Left...")
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        print(f"Row 2 Left pos: {mgba.get_coordinates()}")
        if mgba.get_coordinates() == {'x': 9, 'y': 2}:
            mgba.press_buttons(["Right"])
            time.sleep(0.5)
            
    # Walk to Row 1
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print(f"At (10, 1): {mgba.get_coordinates()}")
    
    # Test Left along Row 1
    if mgba.get_coordinates() == {'x': 10, 'y': 1}:
        print("Testing Row 1 Left...")
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        print(f"Row 1 Left pos: {mgba.get_coordinates()}")
        
    scr = mgba.take_screenshot()
    print(f"Final screenshot: {scr}")

test_horizontal_paths_state_a()
