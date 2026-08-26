import mgba
import time

pos = mgba.get_coordinates()
print("Starting position:", pos)

# 1. Walk to (2, 11)
if pos == {"x": 2, "y": 10}:
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    pos = mgba.get_coordinates()
    print("Moved to:", pos)

if pos == {"x": 2, "y": 11}:
    # Face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Press A to open dialogue
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Take screenshot 1
    mgba.take_screenshot()
    print("Pressed A, screenshot 1 taken.")
    
    # Press A to advance/yes
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Take screenshot 2
    mgba.take_screenshot()
    print("Pressed A again, screenshot 2 taken.")
    
    # Press A to advance
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Take screenshot 3
    mgba.take_screenshot()
    print("Pressed A third time, screenshot 3 taken.")
    
    # Press B to dismiss any remaining text
    mgba.press_buttons(["B"])
    time.sleep(0.4)
