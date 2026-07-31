import mgba
import time

def get_stable_coords():
    pos1 = mgba.get_coordinates()
    time.sleep(0.1)
    pos2 = mgba.get_coordinates()
    while pos1 != pos2:
        pos1 = pos2
        time.sleep(0.1)
        pos2 = mgba.get_coordinates()
    return pos1

# We are at (35, 31) with Start Menu open on POKéDEX
# 1. Select POKéMON
print("Navigating to POKéMON...")
mgba.press_buttons(["Down", "A"])
time.sleep(1.2) # wait for party menu to load

# 2. Select TRUFFLE (slot 2)
print("Selecting TRUFFLE...")
mgba.press_buttons(["Down", "A"])
time.sleep(1.2) # wait for TRUFFLE menu to load

# 3. Select CUT (slot 2 in menu: DIG, CUT, STATS...)
print("Selecting CUT...")
mgba.press_buttons(["Down", "A"])
time.sleep(2.0) # wait for CUT animation

# 4. Dismiss CUT textbox
print("Dismissing CUT textbox...")
mgba.press_buttons(["A"])
time.sleep(0.8)

# Now we should be on the overworld at (35, 31) and the bush at (35, 32) is gone!
pos = get_stable_coords()
print(f"Current pos: {pos}")

# Walk Down to Row 34
while pos['y'] < 34:
    mgba.press_buttons(["Down"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"At Row 34: {pos}. Walking Left to Column 18...")

# Walk Left to Column 18
while pos['x'] > 18:
    mgba.press_buttons(["Left"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"At ({pos['x']}, {pos['y']}). Walking Up to Row 27...")

# Walk Up to Row 27
while pos['y'] > 27:
    mgba.press_buttons(["Up"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"Reached Row 27 Column 18: {pos}. Trying UP to test warp...")
mgba.press_buttons(["Up"])
time.sleep(1.2)

pos_after = get_stable_coords()
print(f"Coordinates after UP warp test: {pos_after}")

# Take a screenshot
scr = mgba.take_screenshot()
print(f"Screenshot saved at: {scr}")
