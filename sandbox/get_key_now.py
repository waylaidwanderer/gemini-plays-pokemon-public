import mgba
import time

def walk_to_key_via_col10():
    print("Walking to Secret Key via Column 10...")
    
    # Starting at (5, 8)
    # 1. Down to (5, 10)
    for _ in range(2):
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
    print(f"At (5, 10): {mgba.get_coordinates()}")
    
    # 2. Right to (10, 10)
    for _ in range(5):
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
    print(f"At (10, 10): {mgba.get_coordinates()}")
    
    # 3. Up to (10, 6)
    for _ in range(4):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
    print(f"At (10, 6): {mgba.get_coordinates()}")
    
    # 4. Left through (9, 6) to (1, 6)
    print("Walking Left along Row 6...")
    pos = mgba.get_coordinates()
    for step in range(1, 10):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        print(f"Step {step} Left: {new_pos}")
        if new_pos == pos:
            print(f"Blocked at {pos} on step {step} Left!")
            break
        pos = new_pos
        
    # We should be at (1, 6)
    # 5. Up to (1, 5)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print(f"At (1, 5): {mgba.get_coordinates()}")
    
    # Try picking it up from (1, 5) facing UP
    print("Trying to pick up Secret Key from (1, 5) facing UP...")
    # First make sure we face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Clear dialogue
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # If we are still at (1, 5), try stepping Up to (1, 4) just in case
    pos_after = mgba.get_coordinates()
    if pos_after == {'x': 1, 'y': 5}:
        # Try walking UP to (1, 4)
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        pos_up = mgba.get_coordinates()
        print(f"Position after trying to step Up to (1, 4): {pos_up}")
        if pos_up == {'x': 1, 'y': 4}:
            # Try A here
            print("At (1, 4), pressing A...")
            mgba.press_buttons(["A"])
            time.sleep(1.0)
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            
    print(f"Final retrieval state: {mgba.get_coordinates()}")
    scr = mgba.take_screenshot()
    print(f"Final screenshot: {scr}")

walk_to_key_via_col10()
