import mgba
import time

def test_col10_path():
    print("Testing B1F Column 10 path step-by-step...")
    
    # Starting at (5, 9)
    pos = mgba.get_coordinates()
    print(f"Start: {pos}")
    
    # 1. Walk Right to (9, 9)
    for _ in range(4):
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
    pos = mgba.get_coordinates()
    print(f"At (9, 9): {pos}")
    
    # 2. Walk Down to (9, 11)
    for _ in range(2):
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
    pos = mgba.get_coordinates()
    print(f"At (9, 11): {pos}")
    
    # 3. Walk Right to (10, 11)
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    pos = mgba.get_coordinates()
    print(f"Attempt to step Right to (10, 11): {pos}")
    
    if pos == {'x': 10, 'y': 11}:
        # 4. Walk Up Column 10
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
            
    scr = mgba.take_screenshot()
    print(f"Screenshot: {scr}")

test_col10_path()
