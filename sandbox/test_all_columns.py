import mgba
import time

def handle_battle():
    # If a battle starts during test, flee
    mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "Down", "Right", "A", "sleep 1500", "B"])
    time.sleep(1.0)

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.35)
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        # Check if we are in battle
        handle_battle()
        pos_after = mgba.get_coordinates()
    return pos_after

# We are currently at (6, 7) on 1F West.
# We will test Column 6 to Column 2 (going Left) and Column 6 to Column 12 (going Right)
# to see where we can step DOWN to Row 8!

print("Testing going Down on Column 6...")
pos = walk_step("Down")
print("Position after Down on Col 6:", pos)
if pos['y'] == 8:
    print("Column 6 is open!")
    walk_step("Up") # go back
else:
    print("Column 6 is BLOCKED.")

# Test Column 5
print("\nTesting Column 5...")
walk_step("Left") # to (5, 7)
pos = walk_step("Down")
print("Position after Down on Col 5:", pos)
if pos['y'] == 8:
    print("Column 5 is open!")
    walk_step("Up")
else:
    print("Column 5 is BLOCKED.")
walk_step("Right") # back to (6, 7)

# Test Column 4
print("\nTesting Column 4...")
walk_step("Left") # to (5, 7)
walk_step("Left") # to (4, 7)
pos = walk_step("Down")
print("Position after Down on Col 4:", pos)
if pos['y'] == 8:
    print("Column 4 is open!")
    walk_step("Up")
else:
    print("Column 4 is BLOCKED.")
walk_step("Right")
walk_step("Right") # back to (6, 7)

# Test Column 3
print("\nTesting Column 3...")
walk_step("Left") # to (5, 7)
walk_step("Left") # to (4, 7)
walk_step("Left") # to (3, 7)
pos = walk_step("Down")
print("Position after Down on Col 3:", pos)
if pos['y'] == 8:
    print("Column 3 is open!")
    walk_step("Up")
else:
    print("Column 3 is BLOCKED.")
walk_step("Right")
walk_step("Right")
walk_step("Right") # back to (6, 7)

# Test Column 2
print("\nTesting Column 2...")
walk_step("Left") # to (5, 7)
walk_step("Left") # to (4, 7)
walk_step("Left") # to (3, 7)
walk_step("Left") # to (2, 7)
pos = walk_step("Down")
print("Position after Down on Col 2:", pos)
if pos['y'] == 8:
    print("Column 2 is open!")
    walk_step("Up")
else:
    print("Column 2 is BLOCKED.")
walk_step("Right")
walk_step("Right")
walk_step("Right")
walk_step("Right") # back to (6, 7)

print("\nFinal Position:", mgba.get_coordinates())
mgba.take_screenshot()
