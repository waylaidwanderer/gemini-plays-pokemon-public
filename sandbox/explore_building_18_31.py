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

# First, press A to dismiss the CUT textbox
print("Dismissing textbox...")
mgba.press_buttons(["A"])
time.sleep(0.8)

# Now step Down onto Row 34
pos = get_stable_coords()
print(f"Current pos: {pos}")
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

print(f"At ({pos['x']}, {pos['y']}). Walking Up to Row 31...")
# Walk Up to Row 31
while pos['y'] > 31:
    mgba.press_buttons(["Up"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"At ({pos['x']}, {pos['y']}), entering door by pressing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0) # wait for warp transition

pos_after = get_stable_coords()
print(f"New position after warp: {pos_after}")

# Take a screenshot inside
scr = mgba.take_screenshot()
print(f"Screenshot saved at: {scr}")
