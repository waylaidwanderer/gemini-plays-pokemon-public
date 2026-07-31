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

# We start at (28, 12)
print("Start Position:", mgba.get_coordinates())

# 1. Walk Left to (18, 11) gap, then into Left Room
mgba.press_buttons(["Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left"])
wait_for_movement()
print("At (18, 12):", mgba.get_coordinates())

mgba.press_buttons(["Up", "Left", "Left"])
wait_for_movement()
print("In Left Room:", mgba.get_coordinates())

# 2. Walk Left to Column 12, Row 13 (UP spinner) -> spins to (2, 9) stopper
# Wait, let's just go Left to (12, 13)
# To do this safely, walk Left to Column 12, Row 13
# We are currently around (16, 11). Walk Left to (12, 11), then Down to (12, 13)
mgba.press_buttons(["Left", "Left", "Left", "Left", "Down", "Down"])
time.sleep(2.0) # Let the slide finish
wait_for_movement()
print("Landed at (2, 9) stopper:", mgba.get_coordinates())

# 3. Walk to (3, 14) (LEFT spinner) -> spins to (2, 14) stopper
mgba.press_buttons(["Right", "Down", "Down", "Down", "Down", "Down"])
time.sleep(2.0) # Let the slide finish
wait_for_movement()
print("Landed at (2, 14) stopper:", mgba.get_coordinates())

# 4. Walk Down Column 2 to Row 25
for i in range(11):
    mgba.press_buttons(["Down"])
    wait_for_movement()
print("At Row 25:", mgba.get_coordinates())

# 5. Walk Right to Column 14
for i in range(12):
    mgba.press_buttons(["Right"])
    wait_for_movement()
print("At (14, 25):", mgba.get_coordinates())

# 6. Test Column 15 on Rows 24, 25, 26
# Test Row 25:
print("Testing (15, 25):")
pos_before = mgba.get_coordinates()
mgba.press_buttons(["Right"])
pos_after = wait_for_movement()
if pos_after != pos_before:
    print("Row 25 is walkable! Landed at:", pos_after)
    # Walk back
    mgba.press_buttons(["Left"])
    wait_for_movement()
else:
    print("Row 25 is blocked.")

# Test Row 24:
mgba.press_buttons(["Up"])
wait_for_movement()
print("At (14, 24):", mgba.get_coordinates())
pos_before = mgba.get_coordinates()
mgba.press_buttons(["Right"])
pos_after = wait_for_movement()
if pos_after != pos_before:
    print("Row 24 is walkable! Landed at:", pos_after)
    # Walk back
    mgba.press_buttons(["Left"])
    wait_for_movement()
else:
    print("Row 24 is blocked.")

# Test Row 26:
mgba.press_buttons(["Down", "Down"])
wait_for_movement()
print("At (14, 26):", mgba.get_coordinates())
pos_before = mgba.get_coordinates()
mgba.press_buttons(["Right"])
pos_after = wait_for_movement()
if pos_after != pos_before:
    print("Row 26 is walkable! Landed at:", pos_after)
    # Walk back
    mgba.press_buttons(["Left"])
    wait_for_movement()
else:
    print("Row 26 is blocked.")

screenshot_path = mgba.take_screenshot()
print("Final Screenshot:", screenshot_path)
