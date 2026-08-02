import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B1F elevator systematic door test from:", pos)

if pos['x'] == 25 and pos['y'] == 14:
    # 1. Walk Down 1 to (25, 15)
    pos = move(["Down"])
    
    # 2. Test right half of door at (25, 16)
    print("Testing right half at (25, 15) facing DOWN...")
    mgba.press_buttons(["Down"]) # Face Down
    time.sleep(0.3)
    mgba.press_buttons(["A"]) # Press A
    time.sleep(1.0)
    
    # Press A again in case of a textbox
    print("Pressing A again to dismiss potential textbox...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Try walking Down
    print("Trying to walk Down...")
    pos = move(["Down"])
    if pos['y'] == 16:
        print("Successfully opened and entered the right half of the door!")
        # Continue Down into elevator warp
        for _ in range(3):
            pos = move(["Down"])
        time.sleep(2.0)
        print("Final position inside elevator:", mgba.get_coordinates())
    else:
        print("Right half failed. Moving to Left half...")
        # 3. Walk to (24, 15)
        pos = move(["Left"])
        
        # 4. Test left half of door at (24, 16)
        print("Testing left half at (24, 15) facing DOWN...")
        mgba.press_buttons(["Down"]) # Face Down
        time.sleep(0.3)
        mgba.press_buttons(["A"]) # Press A
        time.sleep(1.0)
        
        # Press A again in case of a textbox
        print("Pressing A again to dismiss potential textbox...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Try walking Down
        print("Trying to walk Down...")
        pos = move(["Down"])
        if pos['y'] == 16:
            print("Successfully opened and entered the left half of the door!")
            # Continue Down into elevator warp
            for _ in range(3):
                pos = move(["Down"])
            time.sleep(2.0)
            print("Final position inside elevator:", mgba.get_coordinates())
        else:
            print("Left half failed as well.")

mgba.take_screenshot()
