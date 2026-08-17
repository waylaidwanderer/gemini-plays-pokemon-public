import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press_and_wait(btn):
    mgba.press_buttons([btn])
    time.sleep(0.35)
    return get_pos()

# We start at (1, 2).
# Let's walk down to Row 5, and then walk Right to Column 18.
print("Walking to Row 5, then Right to Column 18...")
curr = get_pos()

# Down 3 steps to (1, 5)
for _ in range(3):
    curr = press_and_wait("Down")

# Right to Column 18
while curr[0] < 18:
    pos = press_and_wait("Right")
    if pos == curr:
        print(f"Blocked at {curr}")
        break
    curr = pos

print(f"Reached {curr}. Testing Row 5 exit at (19, 5)...")
# Let's try to go Right onto (19, 5)
pos = press_and_wait("Right")
if abs(pos[0] - curr[0]) > 1 or abs(pos[1] - curr[1]) > 1:
    print(f"WARPED from Row 5! New position: {pos}")
else:
    print(f"Row 5 blocked. Current position: {pos}")
    if pos[0] == 19:
        # We are at (19, 5). Let's try to go Right one more time to trigger warp!
        pos2 = press_and_wait("Right")
        if abs(pos2[0] - pos[0]) > 1 or abs(pos2[1] - pos[1]) > 1:
            print(f"WARPED from (19, 5) after extra Right! New position: {pos2}")
        else:
            print("Failed to warp from (19, 5). Walking back to (18, 5)...")
            press_and_wait("Left")
            
    # Now let's try Row 4 exit!
    print("Testing Row 4 exit...")
    curr = get_pos()
    # Go Up to (18, 4)
    curr = press_and_wait("Up")
    # Go Right to (19, 4)
    pos = press_and_wait("Right")
    if abs(pos[0] - curr[0]) > 1 or abs(pos[1] - curr[1]) > 1:
        print(f"WARPED from Row 4! New position: {pos}")
    else:
        print(f"Row 4 blocked. Current position: {pos}")
        if pos[0] == 19:
            # We are at (19, 4). Let's try to go Right to trigger warp!
            pos2 = press_and_wait("Right")
            if abs(pos2[0] - pos[0]) > 1 or abs(pos2[1] - pos[1]) > 1:
                print(f"WARPED from (19, 4) after extra Right! New position: {pos2}")
            else:
                print("Failed to warp from Row 4.")

print("Exploration complete. Final position:", get_pos())
