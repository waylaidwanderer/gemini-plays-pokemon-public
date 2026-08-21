import mgba
import time

# We are at (18, 4) on 1F East.
print("Current position:", mgba.get_coordinates())

# Test 1: Press A facing UP
print("Pressing A facing UP...")
mgba.press_buttons(["A"])
time.sleep(0.5)
pos = mgba.get_coordinates()
print("Position after A:", pos)

if pos['x'] != 18 or pos['y'] != 4:
    print("WARPED via A!")
else:
    # Test 2: Walk Right to (19, 4) and try Up to (19, 3)
    print("Walking to (19, 4)...")
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print("At:", pos)
    
    if pos == {'x': 19, 'y': 4}:
        print("Stepping Up to (19, 3)...")
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        print("Position after Up on (19, 3):", pos)
        if pos['x'] != 19 or pos['y'] != 4:
            print("WARPED via (19, 3)!")
            
    # If still not warped, walk back to (18, 4)
    pos = mgba.get_coordinates()
    if pos == {'x': 19, 'y': 4}:
        mgba.press_buttons(["Left"])
        time.sleep(0.3)

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
