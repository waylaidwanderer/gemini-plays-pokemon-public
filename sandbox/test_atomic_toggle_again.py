import mgba
import sys
import time

def get_pos():
    return mgba.get_coordinates()

# Starting at (1, 13)
print("Start position:", get_pos())

# 1. Walk to (2, 12) and face UP
mgba.press_buttons(["Up", "sleep 600"]) # to (1, 12)
mgba.press_buttons(["Right", "sleep 600"]) # to (2, 12)
print("Position before toggle:", get_pos())

# 2. Toggle switch atomically
print("Toggling switch...")
mgba.press_buttons(["Up", "sleep 250", "A", "sleep 1000", "A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
print("Position after toggle:", get_pos())

# 3. Walk to (1, 13) and test if (1, 14) is open
mgba.press_buttons(["Left", "sleep 600"]) # to (1, 12)
mgba.press_buttons(["Down", "sleep 600"]) # to (1, 13)
print("Position at test start:", get_pos())

print("Testing if (1, 14) is open...")
mgba.press_buttons(["Down", "sleep 600"])
print("Position after trying Down to 14:", get_pos())

# 4. Walk to (1, 10) and test if (1, 9) is open
mgba.press_buttons(["Up", "sleep 600"]) # to (1, 12)
mgba.press_buttons(["Up", "sleep 600"]) # to (1, 11)
mgba.press_buttons(["Up", "sleep 600"]) # to (1, 10)
print("Testing if (1, 9) is open...")
mgba.press_buttons(["Up", "sleep 600"])
print("Position after trying Up to 9:", get_pos())
mgba.take_screenshot()
