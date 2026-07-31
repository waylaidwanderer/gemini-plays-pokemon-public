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

# We start at B3F (2, 9)
print("Start Position:", mgba.get_coordinates())

# 1. Walk to (3, 14) (LEFT spinner) -> spins to (2, 14) stopper
mgba.press_buttons(["Right"])
wait_for_movement()
print("At (3, 9):", mgba.get_coordinates())

for i in range(5):
    mgba.press_buttons(["Down"])
    wait_for_movement()
print("At (3, 14) spinner:", mgba.get_coordinates())

# The last Down step onto (3, 14) is a LEFT spinner -> spins to (2, 14) stopper
# Wait, let's make sure the slide finishes
time.sleep(2.0)
pos_stopper = wait_for_movement()
print("Landed at (2, 14) stopper:", pos_stopper)

# 2. From (2, 14) stopper, walk Down into the bottom-left area.
# Let's see: on column 2, is row 15 walkable?
# Let's test walking Down to row 19-23.
# We'll just walk Down and print coordinates after each step
for i in range(10):
    mgba.press_buttons(["Down"])
    p_curr = wait_for_movement()
    print(f"Down step {i+1}: {p_curr}")
    if p_curr['y'] >= 19:
        break

pos_bottom = mgba.get_coordinates()
print("Reached bottom-left area at:", pos_bottom)

# 3. Walk Right along Row 24, Row 25 and Row 26 to test Column 15!
# We want to systematically find if we can cross Column 15 on any of these bottom rows.
# Let's walk to column 14, then try walking Right to Column 15!

# Walk to Column 14 (Y should be 24 or 25)
# Walk Down to Row 24 if we are not there yet
curr = mgba.get_coordinates()
while curr['y'] < 24:
    mgba.press_buttons(["Down"])
    curr = wait_for_movement()
print("At Row 24:", curr)

# Try walking Right as far as possible on Row 24
print("Exploring Row 24 Right...")
for col in range(curr['x'] + 1, 20):
    mgba.press_buttons(["Right"])
    p_new = wait_for_movement()
    if p_new['x'] < col:
        print(f"Row 24 blocked at: {p_new}")
        break
    print(f"Row 24: {p_new}")

# Walk back to Column 14, go Down to Row 25, and try walking Right
mgba.press_buttons(["Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left"])
curr = wait_for_movement()
# Walk to (14, 25)
while curr['x'] < 14:
    mgba.press_buttons(["Right"])
    curr = wait_for_movement()
while curr['y'] < 25:
    mgba.press_buttons(["Down"])
    curr = wait_for_movement()
print("At (14, 25):", curr)

# Try walking Right as far as possible on Row 25
print("Exploring Row 25 Right...")
for col in range(15, 20):
    mgba.press_buttons(["Right"])
    p_new = wait_for_movement()
    if p_new['x'] < col:
        print(f"Row 25 blocked at: {p_new}")
        break
    print(f"Row 25: {p_new}")

# Walk back to Column 14, go Down to Row 26, and try walking Right
mgba.press_buttons(["Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left"])
curr = wait_for_movement()
while curr['x'] < 14:
    mgba.press_buttons(["Right"])
    curr = wait_for_movement()
while curr['y'] < 26:
    mgba.press_buttons(["Down"])
    curr = wait_for_movement()
print("At (14, 26):", curr)

# Try walking Right as far as possible on Row 26
print("Exploring Row 26 Right...")
for col in range(15, 20):
    mgba.press_buttons(["Right"])
    p_new = wait_for_movement()
    if p_new['x'] < col:
        print(f"Row 26 blocked at: {p_new}")
        break
    print(f"Row 26: {p_new}")

# Take screenshot to verify where we end up
screenshot_path = mgba.take_screenshot()
print("Verification Screenshot:", screenshot_path)
