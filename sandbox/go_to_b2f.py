import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting go_to_b2f from:", pos)

# We want to go to B1F stairs at (23, 2)
# Let's walk Left to Column 25
print("Walking Left to Column 25...")
for _ in range(3):
    pos = move(["Left"])

# Let's try walking Up on Column 25
print("Walking Up on Column 25...")
for i in range(13):
    old_pos = pos
    pos = move(["Up"])
    if pos == old_pos:
        print(f"Blocked going Up Column 25 at {pos}")
        # If we get blocked, try to go Right to Column 26/27 and go Up, or Left to Column 24
        print("Attempting to bypass block...")
        # Let's try going Left to Column 24 first
        pos = move(["Left"])
        if pos != old_pos:
            print("Successfully moved Left to:", pos)
            pos = move(["Up"])
        else:
            # Try going Right
            pos = move(["Right"])
            if pos != old_pos:
                print("Successfully moved Right to:", pos)
                pos = move(["Up"])

# At this point, let's see where we are
pos = mgba.get_coordinates()
print("After Up attempts, pos:", pos)

# Walk to (23, 8) or (23, 2)
if pos['x'] > 23:
    dist = pos['x'] - 23
    print(f"Walking Left {dist} steps...")
    for _ in range(dist):
        pos = move(["Left"])

if pos['y'] > 2:
    dist = pos['y'] - 2
    print(f"Walking Up {dist} steps to stairs...")
    for _ in range(dist):
        pos = move(["Up"])

# Take stairs
print("Stepping onto stairs...")
pos = move(["Up"])
time.sleep(2.0)
print("New position:", mgba.get_coordinates())
mgba.take_screenshot()
