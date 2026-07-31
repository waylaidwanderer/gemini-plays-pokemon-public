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

# 1. Exit Prize Exchange
# Current pos inside is (9, 7). Walk Left to (3, 7) and then exit.
path_inside = [
    ("Left", 4), # (9,7) -> (5,7)
    ("Up", 3),   # (5,7) -> (5,4)
    ("Left", 1), # (5,4) -> (4,4)
    ("Up", 3),   # (4,4) -> (4,1)
    ("Left", 1), # (4,1) -> (3,1)
    ("Down", 6), # (3,1) -> (3,7)
]

print("Walking to exit of Prize Exchange...")
for direction, steps in path_inside:
    for i in range(steps):
        mgba.press_buttons([direction])
        time.sleep(0.35)

pos = get_stable_coords()
print(f"At exit: {pos}. Pressing DOWN to exit...")
mgba.press_buttons(["Down"])
time.sleep(1.0) # wait for warp

pos = get_stable_coords()
print(f"Exited to overworld at: {pos}")

# Ensure we are on Row 28
if pos['y'] != 28:
    mgba.press_buttons(["Down"])
    time.sleep(0.35)
    pos = get_stable_coords()

# 2. Walk Right to Column 35 on Row 28
while pos['x'] < 35:
    mgba.press_buttons(["Right"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"At ({pos['x']}, {pos['y']}). Walking DOWN to Row 31...")

# 3. Walk Down to Row 31
while pos['y'] < 31:
    mgba.press_buttons(["Down"])
    time.sleep(0.35)
    pos = get_stable_coords()

# Check if bush at (35, 32) is blocking us
print(f"At ({pos['x']}, {pos['y']}). Checking if bush at (35, 32) is clear...")
mgba.press_buttons(["Down"])
time.sleep(0.5)
pos_down = get_stable_coords()

if pos_down['y'] == 31:
    print("Blocked by bush! Using CUT...")
    # Open Start Menu, POKEMON, TRUFFLE, CUT
    # We know the Start menu cursor position can vary. Let's make it safe:
    # Close menu just in case, then press Start
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300", "Start"])
    time.sleep(0.8)
    # Cursor is likely on ITEM. Let's press Up to select POKEMON
    mgba.press_buttons(["Up", "A"])
    time.sleep(1.2)
    # Select TRUFFLE (slot 2)
    mgba.press_buttons(["Down", "A"])
    time.sleep(1.2)
    # Select CUT (slot 2 in menu: DIG, CUT, STATS...)
    mgba.press_buttons(["Down", "A"])
    time.sleep(2.0)
    # Dismiss CUT textbox
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    # Try to step Down again
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    pos_down = get_stable_coords()

print(f"Coordinates after passing bush: {pos_down}")

# Walk Down to Row 34
pos = pos_down
while pos['y'] < 34:
    mgba.press_buttons(["Down"])
    time.sleep(0.35)
    pos = get_stable_coords()

# Walk Left to Column 18
while pos['x'] > 18:
    mgba.press_buttons(["Left"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"At Row 34 Column 18: {pos}. Walking UP column 18...")

# Walk Up to Row 27
while pos['y'] > 27:
    mgba.press_buttons(["Up"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"Reached Row 27 Column 18: {pos}. Testing warp by pressing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

pos_after = get_stable_coords()
print(f"Coordinates after UP warp test: {pos_after}")

scr = mgba.take_screenshot()
print(f"Screenshot saved at: {scr}")
