import mgba
import sys
import time

def get_pos():
    return mgba.get_coordinates()

def walk_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 200"])
    pos_after = get_pos()
    return pos_before, pos_after

# Starting at (10, 6)
print("Starting B1F East Switch Test...")
print("Position before walking:", get_pos())

# Walk to (12, 9)
# From (10, 6) -> Right to (12, 6) -> Down to (12, 9)
mgba.press_buttons(["Right", "sleep 200", "Right", "sleep 200"])
mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200"])

print("Arrived at:", get_pos())

# Face Right towards statue at (13, 9)
mgba.press_buttons(["Right", "sleep 200"])

# Interact with statue
print("Interacting with statue...")
mgba.press_buttons(["A", "sleep 800"])

# Take screenshot to see dialogue
screenshot_path = mgba.take_screenshot()
print("Screenshot taken:", screenshot_path)

# Clear any text boxes if they appeared
mgba.press_buttons(["A", "sleep 800"])
mgba.press_buttons(["A", "sleep 800"])
mgba.press_buttons(["B", "sleep 500"])

print("Done! Position:", get_pos())
