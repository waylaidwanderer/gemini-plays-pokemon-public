import mgba
import time

print("Current Pos:", mgba.get_coordinates())

# From (7, 7) we are facing UP.
# Let's test walking Left to (6, 7), then UP to (6, 6), and then test walking Right to (7, 6) and (8, 6)
# and UP to (6, 5)

# 1. Walk Left to (6, 7)
print("Pressing Left...")
mgba.press_buttons(["Left"])
time.sleep(0.3)
print("Position:", mgba.get_coordinates())

# 2. Walk UP to (6, 6)
if mgba.get_coordinates() == {'x': 6, 'y': 7}:
    print("Pressing Up...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    print("Position:", mgba.get_coordinates())

# 3. From (6, 6), test walking Right
if mgba.get_coordinates() == {'x': 6, 'y': 6}:
    print("Pressing Right...")
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    print("Position after Right:", mgba.get_coordinates())
    
    # If we moved Right to (7, 6), then let's try walking Right again to (8, 6)
    if mgba.get_coordinates() == {'x': 7, 'y': 6}:
        print("Pressing Right again...")
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
        print("Position after 2nd Right:", mgba.get_coordinates())
