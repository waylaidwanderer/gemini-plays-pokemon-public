import mgba
import sys
import time

def get_pos():
    return mgba.get_coordinates()

# We are currently at (2, 12) facing UP.
print("Triggering switch dialogue...")
mgba.press_buttons(["A", "sleep 2000"])
sc1 = mgba.take_screenshot()
print("Dialogue opened. Screenshot 1 saved:", sc1)

# Let's try pressing B to see if it advances!
print("Pressing B to see if it advances...")
mgba.press_buttons(["B", "sleep 2000"])
sc2 = mgba.take_screenshot()
print("After B. Screenshot 2 saved:", sc2)

# Let's try pressing A to see if it advances!
print("Pressing A to see if it advances...")
mgba.press_buttons(["A", "sleep 2000"])
sc3 = mgba.take_screenshot()
print("After A. Screenshot 3 saved:", sc3)

# Let's close the textbox with B just in case
mgba.press_buttons(["B", "sleep 1000"])
sc4 = mgba.take_screenshot()
print("After close B. Screenshot 4 saved:", sc4)
