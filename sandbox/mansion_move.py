import mgba
import time

# We are standing at (18, 12) in front of the Gym door, with "The door is locked..." on screen.
# Let's close the text box, walk Right to column 19, walk UP to row 3, walk Left to column 6, and enter the Mansion!
print("Entering Pokémon Mansion...")
mgba.press_buttons(["B", "sleep 300", "Right", "sleep 300"])

# Let's walk UP column 19 to row 3
path_up = []
for _ in range(9):
    path_up.append("Up")
    path_up.append("sleep 300")
mgba.press_buttons(path_up)

# Let's walk Left to column 6
path_left = []
for _ in range(13):
    path_left.append("Left")
    path_left.append("sleep 300")
mgba.press_buttons(path_left)

# Enter the door
mgba.press_buttons(["Up", "sleep 1000"])

pos = mgba.get_coordinates()
print(f"Coordinates inside Mansion: {pos}")

scr = mgba.take_screenshot()
print(f"Screenshot saved to: {scr}")
