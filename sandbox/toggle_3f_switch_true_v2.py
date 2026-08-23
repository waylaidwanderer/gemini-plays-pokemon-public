import mgba
import time

def get_pos():
    return mgba.get_coordinates()

# Walk Down from (1, 10) to (1, 11)
print("Walking Down to (1, 11)...")
mgba.press_buttons(["Down", "sleep 250"])
print("Position:", get_pos())

# Turn Right to face the switch
print("Facing Right towards the statue...")
mgba.press_buttons(["Right", "sleep 250"])

# Examine the statue (this starts the "secret switch!" text)
print("Pressing A to examine the statue...")
mgba.press_buttons(["A", "sleep 2500"]) # Very long delay to let text fully print character-by-character

# Confirm 'Yes' (cursor defaults to Yes, so press A)
print("Pressing A to select 'Yes'...")
mgba.press_buttons(["A", "sleep 2500"]) # Very long delay to let state change text fully print

# Dismiss dialogue box
print("Pressing B to close text...")
mgba.press_buttons(["B", "sleep 500"])

print("Switch toggling complete! Position:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot:", sc)
