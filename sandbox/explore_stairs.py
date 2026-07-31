import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.15)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.15)
        p2 = mgba.get_coordinates()
    return p1

# We start at (22, 7) on B3F
print("Start Position:", mgba.get_coordinates())

# 1. Walk Down to (22, 15)
print("Walking to (22, 15)...")
for _ in range(8):
    mgba.press_buttons(["Down"])
    wait_for_movement()
print("At:", mgba.get_coordinates())

# 2. Walk Left to (15, 15) (should be pink checkered, entering Left Room)
print("Walking Left to (15, 15)...")
for _ in range(7):
    mgba.press_buttons(["Left"])
    wait_for_movement()
print("At:", mgba.get_coordinates())

# 3. Step Down onto (15, 16) DOWN spinner -> slides to (15, 18) stopper
print("Stepping Down onto spinner...")
mgba.press_buttons(["Down"])
time.sleep(2.5) # let the slide finish
pos = wait_for_movement()
print("Landed at stopper:", pos)

# 4. Walk Left to (14, 18)
print("Walking to (14, 18)...")
mgba.press_buttons(["Left"])
wait_for_movement()
print("At:", mgba.get_coordinates())

# 5. Let's systematically test walking Down on Column 14 from Row 18!
print("Testing Down on Column 14...")
for i in range(1, 8):
    mgba.press_buttons(["Down"])
    pos = wait_for_movement()
    print(f"Step {i} Down: {pos}")

# If we get blocked on Column 14, let's see where we are!
# We want to check all rows below Row 18 to see where we can go Left or Right.
# Let's write down a systematic exploration.
pos = mgba.get_coordinates()
print("Current Position after testing column 14 Down:", pos)

# If we reached row 20 or deeper, let's see if we can walk Right to column 18!
if pos['y'] >= 19:
    print("Testing walking Right to Column 18...")
    # Try walking Right to column 18
    for i in range(1, 8):
        mgba.press_buttons(["Right"])
        pos = wait_for_movement()
        print(f"Step {i} Right: {pos}")
        
    # If we reached (18, y), try walking to stairs at (18, 19)!
    pos = mgba.get_coordinates()
    if pos['x'] == 18:
        print("At Column 18! Trying to reach stairs at (18, 19)...")
        dy = 19 - pos['y']
        move_dir = "Down" if dy > 0 else "Up"
        for _ in range(abs(dy)):
            mgba.press_buttons([move_dir])
            wait_for_movement()
        
        # Step into stairs at (18, 19) (Warp!)
        print("Stepping onto stairs...")
        mgba.press_buttons(["Up" if pos['y'] == 20 else "Down"])
        time.sleep(3.0)
        pos = wait_for_movement()
        print("Position on B4F:", pos)

# Take screenshot
screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
