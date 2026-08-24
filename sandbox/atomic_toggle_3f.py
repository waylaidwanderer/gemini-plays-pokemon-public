import mgba
import sys
import time

def get_pos():
    return mgba.get_coordinates()

# Currently at (1, 12) facing UP.
print("Start position:", get_pos())

# 1. Walk UP to (1, 11)
print("Walking UP to (1, 11)...")
mgba.press_buttons(["Up", "sleep 600"])
print("Position:", get_pos())

# 2. Toggle switch ATOMICALLY in a single call!
print("Toggling switch atomically...")
mgba.press_buttons(["Right", "sleep 250", "A", "sleep 1000", "A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
print("Position after toggle:", get_pos())

# 3. Test if gate is open by walking UP to (1, 9)
print("Testing if (1, 9) gate is open...")
mgba.press_buttons(["Up", "sleep 600"])
print("Position after 1st Up:", get_pos())

mgba.press_buttons(["Up", "sleep 600"])
print("Position after 2nd Up (should be 1, 9 if open):", get_pos())
mgba.take_screenshot()
