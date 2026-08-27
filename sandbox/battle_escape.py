import mgba
import time

def get_state():
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    return pos

# We are in the moves menu with "No PP left for this move!"
# First, press B to dismiss "No PP left for this move!"
print("Dismissing 'No PP left for this move!'...")
mgba.press_buttons(["B"])
time.sleep(1.0)

# We are back in the moves menu. Press B to return to the main battle menu
print("Returning to main battle menu...")
mgba.press_buttons(["B"])
time.sleep(1.0)

# We are in the main battle menu. Select RUN (Down -> Right -> A)
print("Selecting RUN...")
mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
time.sleep(1.5)

# Dismiss "Got away safely!"
print("Dismissing 'Got away safely!'...")
mgba.press_buttons(["A"])
time.sleep(1.0)

pos = get_state()
