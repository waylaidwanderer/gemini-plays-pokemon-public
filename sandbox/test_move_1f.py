import mgba
import time

# Close any menu
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Current position:", pos)

if pos == {"x": 4, "y": 10}:
    print("Moving Right to (5, 10)...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    if pos == {"x": 5, "y": 10}:
        print("Moving Down to (5, 11)...")
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
        
        pos = mgba.get_coordinates()
        print("Current position:", pos)
        
        # Take a screenshot to verify
        mgba.take_screenshot()
