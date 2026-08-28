import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    old_pos = get_pos()
    mgba.press_buttons([direction])
    time.sleep(0.55)
    new_pos = get_pos()
    print(f"Stepped {direction}: {old_pos} -> {new_pos}")
    return new_pos

print("Start position:", get_pos())

# 1. Walk from (3, 11) to switch position (2, 12)
step("Down") # to (3, 12)
step("Left") # to (2, 12)

# Face UP
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

# 2. Toggle Mewtwo Switch to State B with exactly 4 slow A-presses
print("Toggling switch to State B with exactly 4 slow A-presses...")
mgba.press_buttons([
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500"
])
time.sleep(7.0)
print("Switch toggle complete!")

# 3. Test Column 3 first
print("Testing Column 3 path to Row 6...")
step("Right") # to (3, 12)
step("Up")    # to (3, 11)
pos_before_gate = get_pos()
step("Up")    # try to step to (3, 10) or (3, 9)

pos_after = get_pos()
column_3_open = False
if pos_after != pos_before_gate:
    # Try one more Up to see if we can cross Row 9
    pos_gate_test = step("Up")
    if pos_gate_test[1] <= 9:
        print("Column 3 Row 9 gate is OPEN!")
        column_3_open = True
        # Walk up to Row 6
        while get_pos()[1] > 6:
            step("Up")

if not column_3_open:
    print("Column 3 path failed or blocked. Trying Column 1 path...")
    # Walk back to Row 12
    pos = get_pos()
    while pos[1] < 12:
        pos = step("Down")
    # Walk Left to Column 1 Row 12
    while pos[0] > 1:
        pos = step("Left")
    # Walk Up Column 1 to Row 6
    while get_pos()[1] > 6:
        step("Up")

# 4. Now we are on Row 6 (either on Column 3 or Column 1). Walk Right to Column 20
pos = get_pos()
print("Arrived on Row 6 at:", pos)
while pos[0] < 20:
    pos = step("Right")

# 5. Walk UP Column 20 to Row 3
while get_pos()[1] > 3:
    step("Up")

# 6. Walk RIGHT along Row 3 to Column 26
while get_pos()[0] < 26:
    step("Right")

# 7. Drop through the pitfall to 1F East
print("Dropping through pitfall to 1F East...")
step("Down")
time.sleep(2.5)
pos = get_pos()
print("Landed on 1F East:", pos)

# 8. Walk to B1F East stairs and warp down
if pos[1] == 4:
    step("Down")
pos = get_pos()
while pos[0] > 22:
    pos = step("Left")
while pos[1] > 3:
    pos = step("Up")

print("Stepping UP to warp down to B1F East...")
mgba.press_buttons(["Up"])
time.sleep(2.0)
pos = get_pos()
print("Position on B1F East:", pos)

# 9. Cross B1F East to B1F West NORTH
if pos[1] == 2:
    step("Down")
# Walk to Column 21
step("Left")
# Down to Row 5
step("Down")
step("Down")
# Left to Column 1
pos = get_pos()
while pos[0] > 1:
    pos = step("Left")

# 10. Retrieve Secret Key!
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

print("Retrieving Secret Key...")
mgba.press_buttons(["A"])
time.sleep(2.0)
for _ in range(5):
    mgba.press_buttons(["B"])
    time.sleep(0.4)

print("Mansion fully solved! Current Position:", get_pos())
mgba.take_screenshot()
