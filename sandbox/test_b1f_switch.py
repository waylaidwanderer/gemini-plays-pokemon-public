import mgba
import time

def test_b1f():
    print("Testing B1F paths in current state...")
    
    # 1. Walk Down from (10, 6) to (10, 10)
    for _ in range(4):
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
    print(f"Position at row 10: {mgba.get_coordinates()}")
    
    # 2. Walk Left to Column 7
    for _ in range(3):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
    print(f"Position near stairs: {mgba.get_coordinates()}")
    
    # 3. Walk Down/Left towards (2, 11) or (2, 12)
    # Let's see if we can walk to Column 2 Row 11
    # Let's try Row 11: Walk to (10, 11) then Left?
    # Or Row 10: Walk to (7, 10) then Left?
    # Let's walk Left step-by-step from (7, 10) to (2, 10)
    pos = mgba.get_coordinates()
    for step in range(1, 10):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        print(f"Step {step} Left: {new_pos}")
        if new_pos == pos:
            print(f"Blocked at {pos} on step {step}")
            break
        pos = new_pos
        
    scr = mgba.take_screenshot()
    print(f"Screenshot at end: {scr}")

test_b1f()
