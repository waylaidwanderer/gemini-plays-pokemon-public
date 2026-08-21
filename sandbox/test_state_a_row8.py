import mgba
import time

def test_row8_state_a():
    print("Testing Row 8 gates in State A...")
    
    # We are currently at (10, 1)
    # Walk Down Column 10 to (10, 8)
    for _ in range(7):
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
    pos = mgba.get_coordinates()
    print(f"At (10, 8): {pos}")
    
    if pos == {'x': 10, 'y': 8}:
        # Test Left along Row 8
        print("Walking Left on Row 8...")
        for step in range(1, 5):
            mgba.press_buttons(["Left"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            print(f"Step {step} Left: {new_pos}")
            if new_pos == pos:
                print(f"Blocked at {pos} on step {step} Left")
                break
            pos = new_pos
            
    scr = mgba.take_screenshot()
    print(f"Final screenshot: {scr}")

test_row8_state_a()
