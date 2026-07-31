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

# We start at (23, 14)
print("Start Position:", mgba.get_coordinates())

# Let's walk to the far right on Row 15.
# First, walk Down to Row 15
mgba.press_buttons(["Down"])
p_row15 = wait_for_movement()
print("At Row 15:", p_row15)

# Now, walk Right as far as we can to find the right border of the room
walked_right = 0
pos = p_row15
for i in range(10):
    mgba.press_buttons(["Right"])
    p_new = wait_for_movement()
    if p_new == pos:
        break
    pos = p_new
    walked_right += 1
    print(f"Right step {i+1}: {pos}")

# From our furthest Right on Row 15, let's see if we can walk Down to Row 16!
print("Furthest Right position:", pos)
print("Trying Down onto Row 16...")
mgba.press_buttons(["Down"])
p_down = wait_for_movement()

if p_down != pos:
    print("Row 16 is walkable at this column! Position:", p_down)
    # Let's walk Down as much as possible to reach Row 20
    for j in range(5):
        mgba.press_buttons(["Down"])
        p_new = wait_for_movement()
        if p_new == p_down:
            break
        p_down = p_new
        print(f"Down step {j+1}: {p_down}")
        
    # From where we ended up, let's see if we can walk Left towards Column 18!
    print("At bottom of right corridor:", p_down)
    print("Trying to walk Left...")
    for k in range(12):
        mgba.press_buttons(["Left"])
        p_new = wait_for_movement()
        if p_new == p_down:
            print("Blocked going Left at:", p_down)
            break
        p_down = p_new
        print(f"Left step {k+1}: {p_down}")
else:
    print("Row 16 is blocked at this column.")

# Take screenshot to verify
screenshot_path = mgba.take_screenshot()
print("Final Screenshot:", screenshot_path)
