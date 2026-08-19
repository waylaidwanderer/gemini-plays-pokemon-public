import mgba
import time

# We are at (21, 6) on 3F in State B.
# Let's walk back to (2, 12) on 3F and toggle the switch back to State A!
# Path:
# 1. Down 5 times to (21, 11)
# 2. Left 19 times to (2, 11)
# 3. Down to (2, 12)
# 4. Up to face (2, 11)
# 5. Press A to select switch, then B, A, A to toggle back to State A!

path = []
for _ in range(5):
    path.append("Down")
    path.append("sleep 100")
for _ in range(19):
    path.append("Left")
    path.append("sleep 100")
path.append("Down")
path.append("sleep 100")
path.append("Up")
path.append("sleep 300")

# Interact with switch
path.append("A")
path.append("sleep 500")
path.append("A")
path.append("sleep 500")
path.append("A")
path.append("sleep 1000")

print("Walking to switch on 3F and toggling to State A...")
mgba.press_buttons(path)

pos = mgba.get_coordinates()
print(f"Coordinates after switch toggle: {pos}")

scr = mgba.take_screenshot()
print(f"Screenshot saved to: {scr}")
