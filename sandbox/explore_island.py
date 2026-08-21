import mgba
import time

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.35)
    pos_after = mgba.get_coordinates()
    return pos_after

# We are at (19, 4) on Cinnabar Island.
# Let's walk to Column 8 Row 12, and then try to walk UP on Column 8 and Column 9!

print("Walking to (8, 12) on Cinnabar Island...")
# From (19, 4):
# Down to Row 12
while True:
    curr = mgba.get_coordinates()
    if curr['y'] == 12:
        break
    curr = walk_step("Down")
    
# Left to Column 8
while True:
    curr = mgba.get_coordinates()
    if curr['x'] == 8:
        break
    curr = walk_step("Left")

print("Arrived at start position (8, 12):", mgba.get_coordinates())

# 1. Test walking UP on Column 8
print("\nTesting Column 8...")
curr = mgba.get_coordinates()
for i in range(10):
    pos_before = mgba.get_coordinates()
    pos_after = walk_step("Up")
    print(f"Row {pos_after['y']}")
    if pos_before == pos_after:
        print(f"Column 8 blocked at Row {pos_after['y']}")
        break
    if pos_after['y'] <= 3:
        print("Column 8 is OPEN to the North side!")
        break

# Walk back to Row 12
curr = mgba.get_coordinates()
if curr['y'] < 12:
    print("Walking back DOWN to Row 12...")
    while curr['y'] < 12:
        curr = walk_step("Down")

# 2. Test walking UP on Column 9 (by stepping Right to Column 9 on Row 12 first)
print("\nTesting Column 9...")
walk_step("Right") # to (9, 12)
for i in range(10):
    pos_before = mgba.get_coordinates()
    pos_after = walk_step("Up")
    print(f"Row {pos_after['y']}")
    if pos_before == pos_after:
        print(f"Column 9 blocked at Row {pos_after['y']}")
        break
    if pos_after['y'] <= 3:
        print("Column 9 is OPEN to the North side!")
        break

time.sleep(1.0)
print("Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
