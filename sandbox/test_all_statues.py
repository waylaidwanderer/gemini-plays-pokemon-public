import mgba
import time

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting position for exploration:", pos)

# We are at (12, 11). Let's test walking UP Column 12.
def walk_to_y(target_y):
    current = mgba.get_coordinates()
    while current["y"] > target_y:
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        next_pos = mgba.get_coordinates()
        if next_pos == current:
            print(f"Blocked going UP at {current}")
            return False
        current = next_pos
    while current["y"] < target_y:
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        next_pos = mgba.get_coordinates()
        if next_pos == current:
            print(f"Blocked going DOWN at {current}")
            return False
        current = next_pos
    return True

def test_direction(direction, expected_pos):
    current = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos = mgba.get_coordinates()
    if pos == expected_pos:
        print(f"  {direction} to {expected_pos}: SUCCESS")
        # Walk back
        opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[direction]
        mgba.press_buttons([opposite])
        time.sleep(0.4)
        return True
    else:
        print(f"  {direction} to {expected_pos}: BLOCKED (ended at {pos})")
        return False

# 1. Walk up to y=8
if walk_to_y(8):
    print("At y=8, testing horizontal:")
    test_direction("Right", {"x": 13, "y": 8})
    test_direction("Left", {"x": 11, "y": 8})

# 2. Walk up to y=7
if walk_to_y(7):
    print("At y=7, testing horizontal:")
    test_direction("Right", {"x": 13, "y": 7})
    test_direction("Left", {"x": 11, "y": 7})

# 3. Walk up to y=6
if walk_to_y(6):
    print("At y=6, testing horizontal:")
    test_direction("Right", {"x": 13, "y": 6})
    test_direction("Left", {"x": 11, "y": 6})

# 4. Walk up to y=5
if walk_to_y(5):
    print("At y=5, testing horizontal:")
    test_direction("Right", {"x": 13, "y": 5})
    test_direction("Left", {"x": 11, "y": 5})

# Restore position back to y=11
walk_to_y(11)
print("Finished exploration script.")
