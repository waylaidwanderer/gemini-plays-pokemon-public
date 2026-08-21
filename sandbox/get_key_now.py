import mgba
import time

def get_key():
    print("Starting Secret Key retrieval script with Scientist bypass...")
    
    # Starting at (1, 11)
    # 1. Walk Down to (1, 13)
    for _ in range(2):
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
    print(f"At (1, 13): {mgba.get_coordinates()}")
    
    # 2. Walk Right to (5, 13)
    for _ in range(4):
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
    print(f"At (5, 13): {mgba.get_coordinates()}")
    
    # 3. Walk Up to (5, 5) step-by-step
    pos = mgba.get_coordinates()
    y_target = 5
    while pos['y'] > y_target:
        # If we are at (5, 12), check if (5, 11) is blocked
        if pos == {'x': 5, 'y': 12}:
            mgba.press_buttons(["Up"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                # Blocked at (5, 12), bypass the Scientist!
                print("Scientist is blocking (5, 11). Executing bypass...")
                # Left to (4, 12)
                mgba.press_buttons(["Left"])
                time.sleep(0.5)
                # Up to (4, 11)
                mgba.press_buttons(["Up"])
                time.sleep(0.5)
                # Up to (4, 10)
                mgba.press_buttons(["Up"])
                time.sleep(0.5)
                # Right to (5, 10)
                mgba.press_buttons(["Right"])
                time.sleep(0.5)
                pos = mgba.get_coordinates()
                print(f"Successfully bypassed Scientist. Now at: {pos}")
                continue
            else:
                pos = new_pos
                print(f"Stepped Up to (5, 11): {pos}")
                continue
        
        # Normal Up step
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            print(f"Unexpectedly blocked at {pos} while walking UP!")
            break
        pos = new_pos
        print(f"Stepped UP to: {pos}")
        
    print(f"Reached top of Column 5: {mgba.get_coordinates()}")
    
    # 4. Walk Left towards Column 1
    print("Walking Left towards Column 1...")
    for step in range(1, 5):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        print(f"Step {step} Left: {new_pos}")
        if new_pos == pos:
            print(f"Blocked at {pos} on step {step} Left!")
            break
        pos = new_pos
        
    # Now we should be at (1, 5). Walk Up to (1, 4)
    print("Walking Up to (1, 4)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print(f"Final position before pickup: {mgba.get_coordinates()}")
    
    # Take a screenshot before picking it up
    scr = mgba.take_screenshot()
    print(f"Screenshot before pickup: {scr}")
    
    # Interacting to retrieve the Secret Key
    print("Pressing A to retrieve key...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Take screenshot of dialogue
    scr2 = mgba.take_screenshot()
    print(f"Dialogue screenshot: {scr2}")
    
    # Clear dialogue
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    print(f"Retrieval complete! Final position: {mgba.get_coordinates()}")
    scr3 = mgba.take_screenshot()
    print(f"Final screenshot: {scr3}")

get_key()
