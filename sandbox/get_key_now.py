import mgba
import time

def get_key():
    print("Starting Secret Key retrieval script...")
    
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
    
    # 3. Walk Up to (5, 5) step-by-step to check for obstacles
    pos = mgba.get_coordinates()
    for step in range(1, 9):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        print(f"Step {step} UP: {new_pos}")
        if new_pos == pos:
            print(f"Blocked at {pos} on step {step} UP!")
            break
        pos = new_pos
        
    # We should be at (5, 5). Let's check if we can walk Left to (1, 5)
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
        
    # Now we should be at (1, 5). Walk Up to (1, 4) or adjacent to pick up key.
    print("Walking Up to the key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print(f"Final position before pickup: {mgba.get_coordinates()}")
    
    # Let's take a screenshot before picking it up
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
