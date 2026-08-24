import mgba
import sys

def get_pos():
    return mgba.get_coordinates()

print("Current position:", get_pos())

# 1. Walk left to (1, 11) (facing LEFT)
mgba.press_buttons(["Left", "sleep 500"])
print("Position after Left:", get_pos())

# 2. Press Right and A with no sleep in between!
print("Pressing Right and A...")
mgba.press_buttons(["Right", "A", "sleep 1200"]) # Dialogue opens
mgba.press_buttons(["A", "sleep 1200"]) # Press it?
mgba.press_buttons(["A", "sleep 1200"]) # YES -> click!
mgba.press_buttons(["B", "sleep 500"])  # Close dialogue

print("Toggled! Current position:", get_pos())
mgba.take_screenshot()
