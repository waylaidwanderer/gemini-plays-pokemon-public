import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press_and_wait(btn):
    mgba.press_buttons([btn])
    time.sleep(0.35)
    return get_pos()

# We start at (17, 2).
curr = get_pos()
print(f"Starting right exits test from {curr}...")

# 1. Test Row 3 Exit
print("Testing Row 3 exit...")
curr = press_and_wait("Down") # Go to (17, 3)
if curr[1] == 3:
    # Walk Right along Row 3
    while curr[0] < 19:
        pos = press_and_wait("Right")
        if pos == curr:
            print(f"Blocked Row 3 at {curr}")
            break
        
        if abs(pos[0] - curr[0]) > 1 or abs(pos[1] - curr[1]) > 1:
            print(f"WARPED from Row 3! New position: {pos}")
            break
        curr = pos
    
    if curr[0] == 19:
        # We reached (19, 3). Let's try to go Right to trigger warp!
        pos2 = press_and_wait("Right")
        if abs(pos2[0] - pos[0]) > 1 or abs(pos2[1] - pos[1]) > 1:
            print(f"WARPED from Row 3 after extra Right! New position: {pos2}")
        else:
            print("Failed to warp from (19, 3).")

# Walk back to Column 17 if not warped
curr = get_pos()
if curr[0] > 17:
    print("Walking back to Column 17...")
    while curr[0] > 17:
        curr = press_and_wait("Left")

# 2. Test Row 5 Exit
print("Testing Row 5 exit...")
# Go Down from (17, 3) to (17, 5). Row 4 might be blocked, so let's try to walk Down.
curr = press_and_wait("Down") # Try (17, 4)
if curr[1] == 4:
    curr = press_and_wait("Down") # Go to (17, 5)
else:
    # Row 4 is blocked. Let's walk Left to (15, 3), Down to (15, 5), then Right to (17, 5)
    print("Row 4 is blocked. Routing around via Column 15...")
    while curr[0] > 15:
        curr = press_and_wait("Left")
    curr = press_and_wait("Down") # Go to (15, 4)
    curr = press_and_wait("Down") # Go to (15, 5)
    while curr[0] < 17:
        curr = press_and_wait("Right")

# Now we are at (17, 5). Let's walk Right along Row 5!
print(f"At {curr}. Walking Right along Row 5...")
while curr[0] < 19:
    pos = press_and_wait("Right")
    if pos == curr:
        print(f"Blocked Row 5 at {curr}")
        break
    
    if abs(pos[0] - curr[0]) > 1 or abs(pos[1] - curr[1]) > 1:
        print(f"WARPED from Row 5! New position: {pos}")
        break
    curr = pos

if curr[0] == 19:
    # We reached (19, 5). Let's try to go Right to trigger warp!
    pos2 = press_and_wait("Right")
    if abs(pos2[0] - pos[0]) > 1 or abs(pos2[1] - pos[1]) > 1:
        print(f"WARPED from Row 5 after extra Right! New position: {pos2}")
    else:
        print("Failed to warp from (19, 5).")

print("Test complete. Final position:", get_pos())
