import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    old_pos = get_pos()
    print(f"Current: {old_pos}. Stepping {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.45)
    new_pos = get_pos()
    print(f"New position: {new_pos}")
    return new_pos

# First walk back to (8, 11) from (5, 9)
# Known walkable path: (5, 9) -> (6, 9) -> (6, 10) -> (6, 11) -> (7, 11) -> (8, 11)
print("Walking back to (8, 11)...")
step("Right")
step("Down")
step("Down")
step("Right")
step("Right")

# From (8, 11), walk down to (8, 14)
# Known path: (8, 11) -> (8, 12) -> (8, 13) -> (8, 14)
# Wait, is (8, 12) a spin tile? Yes, (8, 12) is a spin tile that sends us to (9, 11)!
# Ah! So we cannot walk down Column 8 because (8, 12) is a spin tile!
# But we can walk down Column 9!
# Known path to B1F East/Gym East:
# (8, 11) -> (9, 11) -> (9, 12)? Wait, let's see if we can walk (9, 11) -> (9, 12) -> (9, 13) -> (9, 14).
# Let's test walking down Column 9.
print("Walking down Column 9 to Row 14...")
step("Right") # to (9, 11)
step("Down")  # to (9, 12)? Let's see if this is walkable
step("Down")  # to (9, 13)?
step("Down")  # to (9, 14)?

# Try to walk Right on Row 14
print("Probing Right on Row 14...")
for x in range(10, 16):
    pos = get_pos()
    mgba.press_buttons(["Right"])
    time.sleep(0.45)
    new_pos = get_pos()
    if pos == new_pos:
        print(f"Blocked going Right at {pos}")
        break
    else:
        print(f"Moved Right to {new_pos}")

print("Probing complete!")
mgba.take_screenshot()
