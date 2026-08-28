import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Start position:", get_pos())

# Since we are currently at (2, 12) showing "A secret switch!"
# Let's perform the 3 A-presses to toggle and close the dialogue.
print("Pressing A (1/3) to advance to YES/NO prompt...")
mgba.press_buttons(["A"])
time.sleep(1.5)
mgba.take_screenshot()

print("Pressing A (2/3) to select YES and toggle to State B...")
mgba.press_buttons(["A"])
time.sleep(1.5)
mgba.take_screenshot()

print("Pressing A (3/3) to dismiss 'Who wouldn't?' and close dialogue...")
mgba.press_buttons(["A"])
time.sleep(1.5)
mgba.take_screenshot()

# Now we should be in the overworld at (2, 12) facing UP in State B.
print("Position after toggling:", get_pos())

# Let's test walking to Column 1 and up past the gate to see if it is open!
print("Stepping Left to (1, 12)...")
mgba.press_buttons(["Left"])
time.sleep(0.6)
print("Position:", get_pos())

print("Stepping Up to (1, 11)...")
mgba.press_buttons(["Up"])
time.sleep(0.6)
print("Position:", get_pos())

print("Stepping Up to (1, 10)...")
mgba.press_buttons(["Up"])
time.sleep(0.6)
print("Position:", get_pos())

print("Stepping Up to (1, 9) (the gate!)...")
mgba.press_buttons(["Up"])
time.sleep(0.6)
print("Position:", get_pos())

print("Stepping Up to (1, 8)...")
mgba.press_buttons(["Up"])
time.sleep(0.6)
print("Position:", get_pos())

print("Finished testing. Taking final screenshot.")
mgba.take_screenshot()
