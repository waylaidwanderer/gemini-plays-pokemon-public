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

# We start at (6, 7)
pos = get_stable_coords()
print(f"Starting position: {pos}")

# Walk Right along Row 7 as far as possible (up to column 20)
# We will check each coordinate and print it.
for x in range(7, 21):
    pos_before = get_stable_coords()
    mgba.press_buttons(["Right"])
    time.sleep(0.35)
    pos_after = get_stable_coords()
    
    if pos_after == pos_before:
        print(f"Blocked going Right on Row 7 at: {pos_after}")
        break
    pos = pos_after
    print(f"Walked Right to: {pos}")

# Now try to walk Up along the current column (which should be a vertical walkway)
print(f"At {pos}, trying to walk Up...")
while pos['y'] > 1:
    pos_before = get_stable_coords()
    mgba.press_buttons(["Up"])
    time.sleep(0.35)
    pos_after = get_stable_coords()
    
    if pos_after == pos_before:
        print(f"Blocked going Up at: {pos_after}")
        break
    pos = pos_after
    print(f"Walked Up to: {pos}")

# Take a screenshot
scr = mgba.take_screenshot()
print(f"Final screenshot saved at: {scr}")
