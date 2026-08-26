import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    print("CURRENT POSITION:", pos)
    return pos

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

p = check_pos()

# Let's try walking around to map walkable tiles near (9, 10)
# Let's try walking Left to (8, 10)
mgba.press_buttons(["Left"])
time.sleep(0.5)
check_pos()

# Walk Left again to (7, 10) - wait, this might warp us? Let's be careful.
# Instead of walking to (7, 10), let's walk back Right to (9, 10)
mgba.press_buttons(["Right"])
time.sleep(0.5)
check_pos()

# Let's try walking Up to (9, 9)
mgba.press_buttons(["Up"])
time.sleep(0.5)
p_up = check_pos()

if p_up == {"x": 9, "y": 9}:
    # Try Up to (9, 8)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    p_up2 = check_pos()
    if p_up2 == {"x": 9, "y": 9}:
        print("Blocked UP at (9, 8)")
    else:
        # Walk back down
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
    # Walk back down
    mgba.press_buttons(["Down"])
    time.sleep(0.5)

# Try Down to (9, 11)
mgba.press_buttons(["Down"])
time.sleep(0.5)
p_down = check_pos()

if p_down == {"x": 9, "y": 11}:
    # Try Down to (9, 12)
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    p_down2 = check_pos()
    if p_down2 == {"x": 9, "y": 11}:
        print("Blocked DOWN at (9, 12)")
    else:
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
    # Walk back up
    mgba.press_buttons(["Up"])
    time.sleep(0.5)

print("Exploration finished!")
