import mgba
import time

# We are at (11, 12) outside the Pokemon Center.
# Let's walk to the Mansion entrance!
# Path:
# 1. Left to (9, 12)
# 2. UP to (9, 3) (or row 4 if row 3 is blocked, but Cinnabar has open streets)
# 3. Left to (2, 3) (or column 2/3 row 4/3 where the Mansion door is)
# 4. UP to step into the Mansion!

print("Walking to Mansion...")

# Let's walk Left to column 9
print("Left to column 9...")
mgba.press_buttons(["Left", "sleep 150", "Left", "sleep 150"])
time.sleep(0.5)
print("Position:", mgba.get_coordinates())

# Let's walk UP column 9 to row 3
print("UP column 9 to row 3...")
for i in range(9):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
print("Position:", mgba.get_coordinates())

# Now we are at (9, 3) or (9, 4). Let's walk Left along row 3 to column 2
print("Left along row 3 to column 2...")
for i in range(7):
    mgba.press_buttons(["Left"])
    time.sleep(0.3)
print("Position:", mgba.get_coordinates())

# Now we are at (2, 3) or (2, 4) or similar. Let's try to walk UP into the Mansion door!
print("Pressing Up to enter Mansion...")
mgba.press_buttons(["Up"])
time.sleep(1.5) # Wait for warp transition into Mansion

print("New Position inside Mansion:", mgba.get_coordinates())
