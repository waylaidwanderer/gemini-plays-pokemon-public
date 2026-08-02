import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting explore_row8 from {pos}")

if pos['x'] == 2 and pos['y'] == 9:
    # Walk Left to (1, 9)
    pos = move(['Left'])
    # Walk Up 2 to (1, 7)
    pos = move(['Up'])
    pos = move(['Up'])
    # Walk Right to (2, 7)
    pos = move(['Right'])

if pos['x'] == 2 and pos['y'] == 7:
    # Walk Right 3 steps to (5, 7)
    for _ in range(3):
        pos = move(['Right'])
    # Walk Down 2 steps to (5, 9)
    for _ in range(2):
        pos = move(['Down'])
    # Walk Right 2 steps to (7, 9)
    for _ in range(2):
        pos = move(['Right'])
    # Walk Up 1 step to (7, 8)
    pos = move(['Up'])

# Now we are at (7, 8). Let's test walking Right to (8, 8)!
if pos['x'] == 7 and pos['y'] == 8:
    print("Testing Right to (8, 8)...")
    test_pos = move(['Right'])
    if test_pos['x'] > 7:
        print("Row 8 Column 8 is walkable! Labeled coordinates:", test_pos)
        # Let's see if we can walk Right further to Column 9, 10, etc.
        for _ in range(5):
            next_pos = move(['Right'])
            if next_pos['x'] == test_pos['x']:
                print("Blocked going Right!")
                break
            test_pos = next_pos
    else:
        print("Right is blocked from (7, 8)")

mgba.take_screenshot()
