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

# We are currently at (20, 13) in the Right Room
start_pos = mgba.get_coordinates()
print("Start Position:", start_pos)

# Let's explore the right side of the room systematically.
# We will walk East as much as possible, then look around.
walked_path = []
pos = start_pos

# Move East (Right) as far as we can
for i in range(10):
    mgba.press_buttons(["Right"])
    p_new = wait_for_movement()
    if p_new == pos:
        print(f"Blocked going Right at: {pos}")
        break
    pos = p_new
    walked_path.append("Right")
    print(f"Right step {i+1}: {pos}")

# From our furthest Right, let's see if we can move Down or Up
print("From furthest Right, trying Down...")
mgba.press_buttons(["Down"])
p_down = wait_for_movement()
if p_down != pos:
    print("Down is walkable:", p_down)
    # Move back Up
    mgba.press_buttons(["Up"])
    wait_for_movement()
else:
    print("Down is blocked.")

print("From furthest Right, trying Up...")
mgba.press_buttons(["Up"])
p_up = wait_for_movement()
if p_up != pos:
    print("Up is walkable:", p_up)
    # Move back Down
    mgba.press_buttons(["Down"])
    wait_for_movement()
else:
    print("Up is blocked.")

# Let's take a screenshot to inspect the far-right of this room
screenshot_path = mgba.take_screenshot()
print("Far-Right Room Screenshot:", screenshot_path)

# Return to (20, 13) so we don't stay lost
opposite = {'Right': 'Left', 'Left': 'Right', 'Up': 'Down', 'Down': 'Up'}
for move in reversed(walked_path):
    mgba.press_buttons([opposite[move]])
    wait_for_movement()

print("Returned to start:", mgba.get_coordinates())
