import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

# We are at (15, 18) on B2F
print("Exploring from (15, 18) to the east...")

# Step 1: Step Right onto (16, 18) UP spinner -> slides to (16, 13)
move(["Right", "sleep 2500"])

# Let's verify we are at (16, 13)
pos = mgba.get_coordinates()
print("Position after slide (should be 16, 13):", pos)

# Let's try walking in all 4 directions to see where we can go!
for d in ["Up", "Down", "Left", "Right"]:
    mgba.press_buttons([d])
    curr = mgba.get_coordinates()
    print(f"Tried {d}, coordinates: {curr}")
    if curr != pos:
        # Move back to (16, 13)
        opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[d]
        mgba.press_buttons([opposite])
