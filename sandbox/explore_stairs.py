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

# We are at (28, 10) on B3F
print("Start Position:", mgba.get_coordinates())

# Let's walk Down systematically on Column 28
print("Walking Down Column 28...")
for i in range(1, 12):
    mgba.press_buttons(["Down"])
    pos = wait_for_movement()
    print(f"Step {i} Down: {pos}")

# If we get blocked, let's try walking Left to see if there is a gap, and then Down!
pos = mgba.get_coordinates()
if pos['y'] < 19:
    print("Blocked on Column 28. Trying Column 27, 26, 25...")
    # Walk Up back to row 15 if needed
    dy = 15 - pos['y']
    move_dir = "Down" if dy > 0 else "Up"
    for _ in range(abs(dy)):
        mgba.press_buttons([move_dir])
        wait_for_movement()
    
    # Try different columns to go Down
    for col in [27, 26, 25, 24]:
        pos = mgba.get_coordinates()
        dx = col - pos['x']
        move_dir = "Right" if dx > 0 else "Left"
        for _ in range(abs(dx)):
            mgba.press_buttons([move_dir])
            wait_for_movement()
        
        print(f"Trying to go Down on Column {col}...")
        for i in range(1, 8):
            mgba.press_buttons(["Down"])
            p_test = wait_for_movement()
            if p_test['y'] > 16:
                print(f"Success! Reached Row {p_test['y']} on Column {col}!")
                break
        
        # If we reached Row 19 or deeper, break!
        pos_check = mgba.get_coordinates()
        if pos_check['y'] >= 19:
            break
            
        # Backtrack to Row 15
        dy = 15 - pos_check['y']
        move_dir = "Down" if dy > 0 else "Up"
        for _ in range(abs(dy)):
            mgba.press_buttons([move_dir])
            wait_for_movement()

# If we are now south of Row 16, let's walk all the way to the B4F stairs!
pos = mgba.get_coordinates()
print("Position after column checks:", pos)
if pos['y'] >= 19:
    # Walk to Column 18 on Row 20 or 21 (whichever we are on)
    dx = 18 - pos['x']
    move_dir = "Right" if dx > 0 else "Left"
    for _ in range(abs(dx)):
        mgba.press_buttons([move_dir])
        wait_for_movement()
        
    print("At column 18:", mgba.get_coordinates())
    
    # Walk to (18, 20)
    pos = mgba.get_coordinates()
    dy = 20 - pos['y']
    move_dir = "Down" if dy > 0 else "Up"
    for _ in range(abs(dy)):
        mgba.press_buttons([move_dir])
        wait_for_movement()
        
    print("At (18, 20):", mgba.get_coordinates())
    
    # Walk Up onto the B4F stairs!
    print("Stepping Up onto B4F stairs...")
    mgba.press_buttons(["Up"])
    time.sleep(3.0) # wait for warp
    pos_after = wait_for_movement()
    print("Position on B4F:", pos_after)

# Take screenshot
screenshot_path = mgba.take_screenshot()
print("Final Screenshot:", screenshot_path)
