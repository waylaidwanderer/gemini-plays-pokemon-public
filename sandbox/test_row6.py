import mgba
import time

def test_row6():
    print("Testing Row 6 traversal...")
    
    # Starting at (10, 7)
    # Walk Up to (10, 6)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    pos = mgba.get_coordinates()
    print(f"Position after UP: {pos}")
    
    if pos != {'x': 10, 'y': 6}:
        print("Failed to reach (10, 6)")
        return
        
    # Attempt to walk Left step by step
    for step in range(1, 10):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        print(f"Step {step} Left: {new_pos}")
        if new_pos == pos:
            print(f"Blocked at {pos} on step {step}!")
            break
        pos = new_pos

test_row6()
