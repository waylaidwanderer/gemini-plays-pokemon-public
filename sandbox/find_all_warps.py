import mgba
import time

def handle_battle():
    # Simple escape
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.2)

def walk_step(tx, ty, d):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
    mgba.press_buttons([d])
    time.sleep(0.55)
    new_pos = mgba.get_coordinates()
    return new_pos['x'] == tx and new_pos['y'] == ty

# We are currently at (11, 5) on 1F East inside the Mansion.
# Let's first walk out of the Mansion.
# Since we are at (11, 5) on 1F, we can walk Left on Row 5 to Column 2 (doormat)
print("Walking to doormat (2, 7) to exit Mansion...")
# Row 5 Left to Column 2
for col in range(10, 1, -1):
    walk_step(col, 5, 'Left')
# Row 5 to Row 7 on Column 2
walk_step(2, 6, 'Down')
walk_step(2, 7, 'Down')

# Step down to exit
print("Exiting Mansion...")
mgba.press_buttons(["Down"])
time.sleep(2.5)

pos = mgba.get_coordinates()
print("Position outside on Cinnabar Island:", pos)

# We are on Cinnabar Island. Let's systematically test columns 1 to 10 on Row 3, Row 4, Row 11, etc.
# to find where we can warp!
# Let's walk to (6, 12) first.
cur = mgba.get_coordinates()
if cur['y'] == 12:
    if cur['x'] > 6:
        for c in range(cur['x'] - 1, 5, -1):
            walk_step(c, 12, 'Left')
    elif cur['x'] < 6:
        for c in range(cur['x'] + 1, 7):
            walk_step(c, 12, 'Right')

print("At (6, 12). Testing UP on Columns 5, 6, 7...")
# Let's test walking UP on Column 6:
# (6, 12) -> (6, 11) -> (6, 10) -> (6, 9) (which is Lab door)
# Wait, let's test Column 5, 6, 7.
# Let's see what warps exist on the North side!
# To do this safely without getting stuck, we can just save our position before entering any door.
# Actually, let's test Column 5 Row 12, Row 11, Row 10, Row 9, etc.
# Let's write down the coordinate of the warp and then exit immediately if we warp!

def test_tile_warp(col, row):
    # Walk to (col, row + 1)
    # Then face UP and walk UP onto (col, row)
    # If a map transition occurs, we will print it, and then step down to exit!
    pass

