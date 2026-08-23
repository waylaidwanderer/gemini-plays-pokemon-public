import mgba
import time

def get_pos():
    return mgba.get_coordinates()

# Current position is (1, 11) on 3F West, facing Right
print("Currently at:", get_pos())

# Examine the statue
print("Pressing A to examine the Mewtwo statue...")
mgba.press_buttons(["A", "sleep 2500"])

# Confirm 'Yes' to press it
print("Pressing A to select 'Yes'...")
mgba.press_buttons(["A", "sleep 2500"])

# Close text box
print("Pressing B to close text...")
mgba.press_buttons(["B", "sleep 500"])

print("Switch toggling complete! Position:", get_pos())

# Test if we can step Right onto the switch (2, 11) to verify State B is active!
print("Testing if (2, 11) is walkable (State B)...")
mgba.press_buttons(["Right", "sleep 250"])
pos_after = get_pos()
print("Position after Right step:", pos_after)

if pos_after == {'x': 2, 'y': 11}:
    print("SUCCESS! State B is active and (2, 11) is walkable!")
    # Walk back to (1, 11) so we are on the main path
    mgba.press_buttons(["Left", "sleep 250"])
    print("Returned to (1, 11):", get_pos())
else:
    print("FAILED! (2, 11) is still solid. State B not active.")

sc = mgba.take_screenshot()
print("Screenshot:", sc)
