import mgba
import sys
import time

def get_pos():
    return mgba.get_coordinates()

# Starting at (2, 12)
print("Start position:", get_pos())

# Walk RIGHT to (6, 12)
print("Walking to (6, 12)...")
for _ in range(4):
    mgba.press_buttons(["Right", "sleep 450"])
print("Position after walking right:", get_pos())

# Try walking UP to (6, 6)
print("Trying to walk UP Column 6 to Row 6...")
# Walk up to (6, 11)
mgba.press_buttons(["Up", "sleep 450"])
# Walk up to (6, 10)
mgba.press_buttons(["Up", "sleep 450"])
print("Position at (6, 10):", get_pos())

# Try walking UP to (6, 9)
mgba.press_buttons(["Up", "sleep 450"])
print("Position after trying Up to 9:", get_pos())

# Try walking UP to (6, 8)
mgba.press_buttons(["Up", "sleep 450"])
print("Position after trying Up to 8:", get_pos())

mgba.take_screenshot()
