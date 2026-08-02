import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (28, 7) on B1F
# 1. Walk Left to Column 25 (3 steps Left)
for _ in range(3):
    pos = move(["Left"])

# 2. Walk Down 2 steps to Row 9 (2 steps Down)
for _ in range(2):
    pos = move(["Down"])

# 3. Walk Right to Column 28 (3 steps Right)
for _ in range(3):
    pos = move(["Right"])

# 4. Walk Down Column 28 to Row 25
# (From Row 9 to 25 is 16 steps Down)
for i in range(9, 25):
    pos = move(["Down"])
    if pos['y'] != i + 1:
        print(f"Blocked at {pos} during Down movement along Column 28")
        # If we got blocked near Row 18, check if we can walk around the Grunt (at Column 28, Row 18?)
        # Let's say we are at (28, 17) and blocked because the Grunt is at (28, 18).
        if pos['x'] == 28 and pos['y'] == 17:
            print("Encountered Grunt at (28, 18). Attempting to walk around via Column 27...")
            pos = move(["Left"])   # Walk to (27, 17)
            pos = move(["Down"])   # Walk to (27, 18)
            pos = move(["Down"])   # Walk to (27, 19)
            pos = move(["Right"])  # Walk to (28, 19)
            # Re-align with the down-movement loop starting from Y=19
            # Wait, we can just break the loop and continue walking down manually in the script!
            break
        else:
            break

# If we successfully walked around or reached below Row 18:
pos = mgba.get_coordinates()
if pos['y'] < 25:
    print(f"Continuing Down from Y={pos['y']}...")
    for i in range(pos['y'], 25):
        pos = move(["Down"])

# 5. Walk Left to Column 24 (4 steps Left)
pos = mgba.get_coordinates()
if pos['y'] == 25:
    for _ in range(pos['x'] - 24):
        pos = move(["Left"])

# 6. Face UP (North) to trigger the elevator door!
print("Facing UP at elevator trigger coordinate...")
pos = move(["Up"])

print("Finished movement. Current position:", mgba.get_coordinates())
mgba.take_screenshot()
