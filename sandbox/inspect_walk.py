import mgba
import time

def test_moves():
    print("Testing immediate step-by-step movement from (10, 6)...")
    
    # Current position is (10, 6) facing Left
    
    # 1. Try to walk Left 1 step
    mgba.press_buttons(["Left"])
    time.sleep(0.1)
    pos = mgba.get_coordinates()
    print(f"Position after Left: {pos}")
    
    # If we moved Left, we are at (9, 6). Let's walk back Right to (10, 6).
    if pos['x'] == 9:
        mgba.press_buttons(["Right"])
        time.sleep(0.1)
        print("Walked back to (10, 6)")
        
    # 2. Try to walk Up 1 step
    mgba.press_buttons(["Up"])
    time.sleep(0.1)
    pos = mgba.get_coordinates()
    print(f"Position after Up: {pos}")
    
    # If we moved Up, let's walk back Down to (10, 6)
    if pos['y'] == 5:
        mgba.press_buttons(["Down"])
        time.sleep(0.1)
        print("Walked back to (10, 6)")
        
    # 3. Try to walk Down 1 step
    mgba.press_buttons(["Down"])
    time.sleep(0.1)
    pos = mgba.get_coordinates()
    print(f"Position after Down: {pos}")
    
    # If we moved Down, walk back Up to (10, 6)
    if pos['y'] == 7:
        mgba.press_buttons(["Up"])
        time.sleep(0.1)
        print("Walked back to (10, 6)")

test_moves()
