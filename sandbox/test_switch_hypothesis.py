import mgba
import time

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 100"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        attempts = 0
        while pos_before == pos_after and attempts < 5:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

# Starting from (15, 12).
print("Starting switch verification from current position...")
print("Initial position:", mgba.get_coordinates())

# 1. Walk UP Column 15 from Row 12 to Row 6
print("1. Walking UP Column 15 to Row 6...")
pos = mgba.get_coordinates()
while pos['y'] > 6:
    pos = walk_step("Up")
print("  Arrived at Row 6 Column 15:", pos)

# 2. Walk LEFT along Row 6 to Column 12
print("2. Walking LEFT along Row 6 to Column 12...")
while pos['x'] > 12:
    pos = walk_step("Left")
print("  Arrived at Row 6 Column 12:", pos)

# 3. Walk DOWN Column 12 to Row 10
print("3. Walking DOWN Column 12 to Row 10...")
while pos['y'] < 10:
    pos = walk_step("Down")
print("  Arrived at Row 10 Column 12:", pos)

# 4. Face DOWN (to (12, 11))
print("4. Facing DOWN...")
walk_step("Down")
pos = mgba.get_coordinates()
print("  Final standing position:", pos)

# Take screenshot before pressing A
mgba.take_screenshot()

# Press A to toggle switch
print("Pressing A to interact with statue...")
mgba.press_buttons(["A", "sleep 500", "B", "sleep 150"])

# Let's verify if the state toggled!
# If it toggled to State A:
# - The Row 7 gates on 3F East (columns 14-21) should OPEN!
# Let's test by walking to Column 15 Row 6, then trying to walk Down to Row 8.
print("Testing if gates opened on Column 15 Row 7...")
print("Walking to (15, 6)...")
pos = mgba.get_coordinates()
# Walk UP to Row 6
while pos['y'] > 6:
    pos = walk_step("Up")
# Walk RIGHT to Column 15
while pos['x'] < 15:
    pos = walk_step("Right")
print("  Arrived at (15, 6):", pos)

# Try to step DOWN on Column 15
print("Attempting to walk DOWN past Row 7 on Column 15...")
pos_before = mgba.get_coordinates()
pos_after = walk_step("Down")
if pos_before['y'] != pos_after['y']:
    print("SUCCESS!!! Column 15 Row 7 is OPEN! The switch worked and toggled the mansion back to State A!")
    # Walk back UP to Row 6
    walk_step("Up")
else:
    print("BLOCKED: Column 15 Row 7 remains CLOSED. The statue is decorative or didn't toggle.")

print("Final position:", mgba.get_coordinates())
