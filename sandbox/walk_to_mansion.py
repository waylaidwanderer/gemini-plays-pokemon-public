import mgba
import time

def run_from_battle():
    # Overworld has no wild battles on Cinnabar Island grass (unless in tall grass, but there is no tall grass on Cinnabar Island overworld except in Gym, and there's none here).
    # But just in case:
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

# We are at (6, 10). Let's walk Right to column 16, then UP to row 3, then LEFT to column 12.
# Let's do it step-by-step and check collision.
# On Cinnabar Island:
# Row 10 is grass. Let's try to walk Right to column 16.
print("Walking Right from (6, 10)...")
for col in range(7, 20):
    pos = mgba.get_coordinates()
    print(f"Current Pos: {pos}, trying to move Right to {col}")
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == pos['x']:
        print(f"Blocked at column {pos['x']}. Let's try to walk Down to row 12 first.")
        break

# If blocked, try to walk Down 2 steps to row 12 (where there is open grass)
pos = mgba.get_coordinates()
if pos['y'] < 12:
    print("Moving Down to row 12...")
    for row in range(pos['y'] + 1, 13):
        mgba.press_buttons(["Down"])
        time.sleep(0.3)
    print("Position after moving Down:", mgba.get_coordinates())

# Now walk Right as far as possible (up to column 16) on row 12
pos = mgba.get_coordinates()
print("Moving Right on row 12...")
for col in range(pos['x'] + 1, 20):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
print("Position after moving Right:", mgba.get_coordinates())

# Now walk UP to row 3 (or until blocked)
pos = mgba.get_coordinates()
print("Moving UP on Cinnabar Island...")
for row in range(pos['y'] - 1, 2, -1):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
print("Position after moving UP:", mgba.get_coordinates())

# Take a screenshot to inspect the northern area of Cinnabar Island
img = mgba.take_screenshot()
print("Screenshot of northern area:", img)
