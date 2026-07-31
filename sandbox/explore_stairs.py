import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.12)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.12)
        p2 = mgba.get_coordinates()
    return p1

# Currently at B3F (28, 14)
print("Start Position B3F:", mgba.get_coordinates())

# 1. Walk UP to B2F (27, 8)
mgba.press_buttons(["Up", "Left", "Up"])
time.sleep(3.0)
wait_for_movement()
print("Warped UP to B2F:", mgba.get_coordinates())

# 2. On B2F, walk to (3, 15) and warp DOWN to B3F (8, 11)
# Path to (3, 15) from (27, 8):
# Walk Left to Column 3, then Down to Row 15
# Column 27 to 3 is 24 steps Left. Row 8 to 15 is 7 steps Down.
# Let's do this safely with wait_for_movement
for i in range(24):
    mgba.press_buttons(["Left"])
    wait_for_movement()
for j in range(7):
    mgba.press_buttons(["Down"])
    wait_for_movement()
print("At B2F B3F stairs:", mgba.get_coordinates())

# Step DOWN onto the stairs to warp to B3F (8, 11)
mgba.press_buttons(["Down"])
time.sleep(3.0)
wait_for_movement()
print("Warped DOWN to B3F:", mgba.get_coordinates())

# 3. We are now at B3F (8, 11) stopper!
# Let's walk to (10, 14), step onto (11, 14) DOWN spinner, and land at (15, 18) stopper.
mgba.press_buttons(["Right", "Right", "Down", "Down", "Down", "Right"])
time.sleep(3.0) # Let the slide finish
p_stopper = wait_for_movement()
print("Landed at B3F stopper:", p_stopper)

# 4. We are at (15, 18) stopper.
# Let's test walking in all 4 directions from (15, 18) and see what is walkable!
# Specifically, we want to know if we can walk:
# - Down to (15, 19)
# - Left to (14, 18)
# - Right to (16, 18) (UP spinner)
# - Up to (15, 17)
directions = ['Up', 'Down', 'Left', 'Right']
opposite = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}

for move in directions:
    mgba.press_buttons([move])
    p_new = wait_for_movement()
    if p_new != p_stopper:
        print(f"-> Walkable from (15, 18) with move {move}! Landed at: {p_new}")
        # Walk back if we didn't step on a spinner
        dx = abs(p_new['x'] - p_stopper['x'])
        dy = abs(p_new['y'] - p_stopper['y'])
        if dx <= 1 and dy <= 1:
            mgba.press_buttons([opposite[move]])
            wait_for_movement()
        else:
            print(f"   (Stepped on spinner, we are now at {p_new})")
            # If we stepped on a spinner, let's just finish the script
            break
    else:
        print(f"-> Blocked from (15, 18) with move {move}.")

screenshot_path = mgba.take_screenshot()
print("Final Screenshot:", screenshot_path)
