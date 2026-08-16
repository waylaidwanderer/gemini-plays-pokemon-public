import mgba
import time

print("--- TESTING MOVEMENT WITH B PRESSES ---")
pos_before = mgba.get_coordinates()
print("Position before B presses:", pos_before)

# Press B multiple times to clear any possible text boxes
for _ in range(3):
    mgba.press_buttons(["B"])
    time.sleep(0.3)

# Now try moving Left
mgba.press_buttons(["Left"])
time.sleep(0.5)

pos_after = mgba.get_coordinates()
print("Position after Left:", pos_after)

# If we successfully moved Left, let's walk down to the exit!
if pos_after and pos_after['x'] == 7:
    print("Move successful! Walking to exit...")
    # Walk left again to (6, 12)
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    # Walk down to (6, 15)
    for _ in range(3):
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
        
    print("Final position after walking:", mgba.get_coordinates())

mgba.take_screenshot()
