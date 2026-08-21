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
        handle_battle()
        pos_after = mgba.get_coordinates()
    return pos_after

# We are currently at (12, 7) on 1F West in State A.
# Let's test Column 7, 8, 9, 10, 11 to see which one allows walking DOWN to Row 8!

# Test Column 11
print("Testing Column 11...")
walk_step("Left") # to (11, 7)
pos = walk_step("Down")
print("Position after Down on Col 11:", pos)
if pos['y'] == 8:
    print("Column 11 is open!")
    walk_step("Up")
else:
    print("Column 11 is BLOCKED.")
walk_step("Right") # back to (12, 7)

# Test Column 10
print("\nTesting Column 10...")
walk_step("Left") # to (11, 7)
walk_step("Left") # to (10, 7)
pos = walk_step("Down")
print("Position after Down on Col 10:", pos)
if pos['y'] == 8:
    print("Column 10 is open!")
    walk_step("Up")
else:
    print("Column 10 is BLOCKED.")
walk_step("Right")
walk_step("Right") # back to (12, 7)

# Test Column 9
print("\nTesting Column 9...")
walk_step("Left") # to (11, 7)
walk_step("Left") # to (10, 7)
walk_step("Left") # to (9, 7)
pos = walk_step("Down")
print("Position after Down on Col 9:", pos)
if pos['y'] == 8:
    print("Column 9 is open!")
    walk_step("Up")
else:
    print("Column 9 is BLOCKED.")
walk_step("Right")
walk_step("Right")
walk_step("Right") # back to (12, 7)

# Test Column 8
print("\nTesting Column 8...")
walk_step("Left") # to (11, 7)
walk_step("Left") # to (10, 7)
walk_step("Left") # to (9, 7)
walk_step("Left") # to (8, 7)
pos = walk_step("Down")
print("Position after Down on Col 8:", pos)
if pos['y'] == 8:
    print("Column 8 is open!")
    walk_step("Up")
else:
    print("Column 8 is BLOCKED.")
walk_step("Right")
walk_step("Right")
walk_step("Right")
walk_step("Right") # back to (12, 7)

# Test Column 7
print("\nTesting Column 7...")
walk_step("Left") # to (11, 7)
walk_step("Left") # to (10, 7)
walk_step("Left") # to (9, 7)
walk_step("Left") # to (8, 7)
walk_step("Left") # to (7, 7)
pos = walk_step("Down")
print("Position after Down on Col 7:", pos)
if pos['y'] == 8:
    print("Column 7 is open!")
    walk_step("Up")
else:
    print("Column 7 is BLOCKED.")
walk_step("Right")
walk_step("Right")
walk_step("Right")
walk_step("Right")
walk_step("Right") # back to (12, 7)

print("\nFinal Position:", mgba.get_coordinates())
mgba.take_screenshot()
