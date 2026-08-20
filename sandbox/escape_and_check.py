import mgba
import time

def escape_and_check():
    print("Dismissing 'Wild GRIMER appeared!' text...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    print("Dismissing player sending out Pokemon text...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    print("Moving cursor to RUN and executing...")
    # From FIGHT (default): Down, Right, A
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(3.0) # Wait for escape animation
    
    # Dismiss any leftover text/menus
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Post-battle position:", pos)
    
    # We should be at (18, 6). Walk Down to (18, 7) and then (18, 8)
    if pos['x'] == 18 and pos['y'] == 6:
        print("Walking Down to (18, 7)...")
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
        print("Position:", mgba.get_coordinates())
        
        print("Walking Down to (18, 8)...")
        mgba.press_buttons(["Down"])
        time.sleep(2.0) # Wait in case of warp
        
        final_pos = mgba.get_coordinates()
        print("Position after warp attempt:", final_pos)
        mgba.take_screenshot()
        return True
        
    print("Unexpected position:", pos)
    mgba.take_screenshot()
    return False

if __name__ == "__main__":
    escape_and_check()
