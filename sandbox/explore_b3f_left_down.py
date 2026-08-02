import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (22, 18) on B3F
# 1. Walk Right to Column 25 (3 steps Right)
for _ in range(3):
    pos = move(["Right"])

# 2. Walk Down Column 25 as far as possible
print("Walking Down Column 25...")
for i in range(18, 25):
    pos = move(["Down"])
    if pos['y'] != i + 1:
        print(f"Blocked at {pos} during Down movement along Column 25")
        break

# 3. If we got blocked, let's try Column 26
pos = mgba.get_coordinates()
if pos['y'] < 22:
    print("Trying Column 26...")
    # Walk to Column 26 if we can
    pos = move(["Right"])
    if pos['x'] == 26:
        # Walk Down Column 26
        for i in range(pos['y'], 25):
            pos = move(["Down"])
            if pos['y'] != i + 1:
                print(f"Blocked at {pos} during Down movement along Column 26")
                break

# 4. If we got blocked, let's try Column 27
pos = mgba.get_coordinates()
if pos['y'] < 22:
    print("Trying Column 27...")
    # Walk to Column 27 if we can
    pos = move(["Right"])
    if pos['x'] == 27:
        # Walk Down Column 27
        for i in range(pos['y'], 25):
            pos = move(["Down"])
            if pos['y'] != i + 1:
                print(f"Blocked at {pos} during Down movement along Column 27")
                break

print("Final position after exploration:", mgba.get_coordinates())
mgba.take_screenshot()
