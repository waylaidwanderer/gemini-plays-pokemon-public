import mgba
import time

def get_pos():
    return mgba.get_coordinates()

# Currently at (7, 10) on 2F West facing UP
print("Stepping UP to warp to 3F West...")
mgba.press_buttons(["Up", "sleep 400"]) # Warp UP
time.sleep(1.5)
print("Position on 3F West:", get_pos())

# Walk Row 13 path to switch on 3F West
# We land at (7, 11) facing DOWN.
print("Walking Row 13 path to switch...")
mgba.press_buttons(["Down", "sleep 250", "Down", "sleep 250"]) # Land on (7, 13)
for _ in range(6): # Walk Left to (1, 13)
    mgba.press_buttons(["Left", "sleep 250"])
mgba.press_buttons(["Up", "sleep 250", "Up", "sleep 250"]) # Walk Up to (1, 11)

print("Arrived at (1, 11)! Toggling switch to State B...")
mgba.press_buttons(["Right", "sleep 250", "A", "sleep 500", "B", "sleep 250"])
print("State B toggled! Position:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot:", sc)
