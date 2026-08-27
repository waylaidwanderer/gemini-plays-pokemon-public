import mgba
import time

def get_state():
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    return pos

# Clear any text/menus
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = get_state()

# We are at (15, 6) on 2F East.
# Let's walk to Column 18 on Row 6
if pos == {"x": 15, "y": 6}:
    print("Walking RIGHT on Row 6 to Column 18...")
    mgba.press_buttons(["Right", "sleep 450", "Right", "sleep 450", "Right"])
    time.sleep(1.5)
    pos = get_state()

# Walk DOWN Column 18 to Row 10
if pos == {"x": 18, "y": 6}:
    print("Walking DOWN Column 18 to Row 10...")
    mgba.press_buttons(["Down", "sleep 450", "Down", "sleep 450", "Down", "sleep 450", "Down"])
    time.sleep(2.0)
    pos = get_state()

# Walk LEFT along Row 10 to Column 15
if pos == {"x": 18, "y": 10}:
    print("Walking LEFT along Row 10 to Column 15...")
    mgba.press_buttons(["Left", "sleep 450", "Left", "sleep 450", "Left"])
    time.sleep(1.5)
    pos = get_state()

# Step DOWN onto the stairs at (15, 11) to warp UP to 3F East
if pos == {"x": 15, "y": 10}:
    print("Stepping DOWN onto stairs to warp...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    pos = get_state()
