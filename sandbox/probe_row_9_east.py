import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    old_pos = get_pos()
    mgba.press_buttons([direction])
    time.sleep(0.55)
    return get_pos()

print("Current position:", get_pos())

# We are at (3, 11).
# Let's walk to Row 13 first to easily navigate horizontally
print("Walking to Row 13 Column 4...")
step("Down") # to (3, 12) - wait, (3, 12) is blocked by cabinet!
# Ah! We are at (3, 11). We can walk:
# - Right to (4, 11) (open!)
# - Down to (4, 12) (open!)
# - Down to (4, 13) (open!)

step("Right") # to (4, 11)
step("Down")  # to (4, 12)

# Now we are at (4, 12).
# Let's test Column 4: walk to (4, 10)
print("Testing Column 4 Row 9...")
step("Up") # to (4, 11)
step("Up") # to (4, 10)
old_pos = get_pos()
mgba.press_buttons(["Up"])
time.sleep(0.55)
new_pos = get_pos()
if new_pos[1] == 9:
    print("SUCCESS: Column 4 Row 9 is OPEN!")
    exit(0)
else:
    print("Column 4 Row 9 is CLOSED.")

# Let's test Column 6: walk to (6, 10)
# Path: from (4, 10) -> Down to (4, 12) -> Right to (6, 12) -> Up to (6, 10)
print("Testing Column 6 Row 9...")
step("Down") # to (4, 11)
step("Down") # to (4, 12)
step("Right") # to (5, 12)
step("Right") # to (6, 12)
step("Up") # to (6, 11)
step("Up") # to (6, 10)
old_pos = get_pos()
mgba.press_buttons(["Up"])
time.sleep(0.55)
new_pos = get_pos()
if new_pos[1] == 9:
    print("SUCCESS: Column 6 Row 9 is OPEN!")
    exit(0)
else:
    print("Column 6 Row 9 is CLOSED.")

# Let's test Column 7: walk to (7, 10)
# Path: from (6, 10) -> Down to (6, 12) -> Right to (7, 12) -> Up to (7, 10)
print("Testing Column 7 Row 9...")
step("Down") # to (6, 11)
step("Down") # to (6, 12)
step("Right") # to (7, 12)
step("Up") # to (7, 11)
step("Up") # to (7, 10)
old_pos = get_pos()
mgba.press_buttons(["Up"])
time.sleep(0.55)
new_pos = get_pos()
if new_pos[1] == 9:
    print("SUCCESS: Column 7 Row 9 is OPEN!")
    exit(0)
else:
    print("Column 7 Row 9 is CLOSED.")

print("All tested columns are CLOSED.")
mgba.take_screenshot()
