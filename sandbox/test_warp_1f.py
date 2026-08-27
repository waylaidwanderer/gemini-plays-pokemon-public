import mgba
import time

# Close any menu
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Current position:", pos)

if pos == {"x": 4, "y": 10}:
    print("Moving Right onto (5, 10) staircase warp...")
    mgba.press_buttons(["Right"])
    time.sleep(2.0)
    
    pos = mgba.get_coordinates()
    print("Current position after warp attempt:", pos)
    
    # Take a screenshot to verify
    mgba.take_screenshot()
