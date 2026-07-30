import mgba
import time

def get_stable_coords():
    pos1 = mgba.get_coordinates()
    time.sleep(0.1)
    pos2 = mgba.get_coordinates()
    while pos1 != pos2:
        pos1 = pos2
        time.sleep(0.1)
        pos2 = mgba.get_coordinates()
    return pos1

# We are currently at (3, 7) inside Celadon Game Corner
pos = get_stable_coords()
print(f"Starting position inside Game Corner: {pos}")

# 1. Walk UP to Row 1
while pos['y'] > 1:
    mgba.press_buttons(["Up"])
    time.sleep(0.5) # robust delay
    pos = get_stable_coords()

print(f"At top walkway: {pos}")

# 2. Walk Right along Row 1 to find the Rocket Grunt or right wall
# In standard Red/Blue, the room is about 20 columns wide.
# We will walk Right and take screenshots along the way to find the Grunt.
for step in range(25):
    pos_before = get_stable_coords()
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    pos_after = get_stable_coords()
    
    if pos_after == pos_before:
        # Blocked
        print(f"Blocked going Right at: {pos_after}")
        # Take a screenshot to see what's blocking us
        scr = mgba.take_screenshot()
        print(f"Screenshot of blockage saved at: {scr}")
        break
    
    pos = pos_after
    print(f"Walked Right to: {pos}")
    
    # Take screenshot every 4 steps
    if step % 4 == 0:
        scr = mgba.take_screenshot()
        print(f"Screenshot at {pos} saved at: {scr}")

print("End of script.")
