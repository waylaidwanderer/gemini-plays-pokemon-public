import mgba
import time

def test_column1_state_a():
    print("Walking to Column 1 and testing vertical traversal in State A...")
    
    # Starting at (12, 10)
    # 1. Left to (8, 10)
    for _ in range(4):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
    print(f"At (8, 10): {mgba.get_coordinates()}")
    
    # 2. Down to (8, 11)
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    print(f"At (8, 11): {mgba.get_coordinates()}")
    
    # 3. Left to (3, 11)
    for _ in range(5):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
    print(f"At (3, 11): {mgba.get_coordinates()}")
    
    # 4. Down to (3, 12)
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    print(f"At (3, 12): {mgba.get_coordinates()}")
    
    # 5. Left to (1, 12)
    for _ in range(2):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
    print(f"At (1, 12): {mgba.get_coordinates()}")
    
    # 6. Up to (1, 11)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    pos = mgba.get_coordinates()
    print(f"At (1, 11): {pos}")
    
    # 7. Walk Up Column 1 as far as possible
    if pos == {'x': 1, 'y': 11}:
        print("Walking UP Column 1 in State A...")
        for step in range(1, 10):
            mgba.press_buttons(["Up"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            print(f"Step {step} UP: {new_pos}")
            if new_pos == pos:
                print(f"Blocked at {pos} on step {step} UP")
                break
            pos = new_pos
            
    scr = mgba.take_screenshot()
    print(f"Screenshot at end: {scr}")

test_column1_state_a()
