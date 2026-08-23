import mgba
import time

def get_pos():
    return mgba.get_coordinates()

# Current position is (1, 11) on 3F West
print("Attempting to toggle 3F West switch at (2, 11)...")

# Turn Right to face the switch
mgba.press_buttons(["Right", "sleep 250"])
# Press A to examine the statue
mgba.press_buttons(["A", "sleep 400"])
# Press A to select 'Yes' to press it
mgba.press_buttons(["A", "sleep 400"])
# Press B to close the dialogue box
mgba.press_buttons(["B", "sleep 250"])

print("Switch sequence executed!")
sc = mgba.take_screenshot()
print("Screenshot after switch attempt:", sc)
