import mgba
import time

# Current position: (7, 10) on 2F West.
print("Current position:", mgba.get_coordinates())

# Test 1: Press Up on (7, 10) to see if we warp
print("Pressing Up on (7, 10)...")
mgba.press_buttons(["Up"])
time.sleep(0.3)
pos = mgba.get_coordinates()
print("Position after Up on (7, 10):", pos)

# Check if warped
if pos['x'] != 7 or abs(pos['y'] - 10) > 2:
    print("WARPED from (7, 10)!")
else:
    # Walk to (5, 10)
    print("Walking to (5, 10)...")
    # From (7, 10), go Down to (7, 11) -> Left to (5, 11) -> Up to (5, 10)
    mgba.press_buttons(["Down", "sleep 200", "Left", "sleep 200", "Left", "sleep 200", "Up"])
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print("Arrived at:", pos)
    
    if pos == {'x': 5, 'y': 10}:
        print("Pressing Up on (5, 10)...")
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        pos_final = mgba.get_coordinates()
        print("Position after Up on (5, 10):", pos_final)
        if pos_final['x'] != 5 or abs(pos_final['y'] - 10) > 2:
            print("WARPED from (5, 10)!")

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
