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

# Let's try to walk right as far as we can on Row 10 or Row 11
# First, walk down to Row 11 if we are at (5, 10)
if pos == {"x": 5, "y": 10}:
    print("Walking Down to (5, 11)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    pos = get_state()

# Now walk RIGHT as far as we can
for i in range(15):
    print(f"Step {i+1}: Walking Right...")
    mgba.press_buttons(["Right"])
    time.sleep(0.45)
    new_pos = get_state()
    if new_pos == pos:
        print("Blocked walking Right!")
        break
    pos = new_pos
