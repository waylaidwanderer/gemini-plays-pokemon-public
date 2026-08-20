import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting toggle sequence from:", get_pos())

# Step Down to (3, 12)
mgba.press_buttons(["Down"])
time.sleep(0.5)
print("After Down:", get_pos())

# Step Left to (2, 12)
mgba.press_buttons(["Left"])
time.sleep(0.5)
print("After Left:", get_pos())

# Turn Up to face the statue
mgba.press_buttons(["Up"])
time.sleep(0.4)
print("Facing Up at:", get_pos())

# Interact with A
mgba.press_buttons(["A"])
time.sleep(0.6)

# Select YES
mgba.press_buttons(["A"])
time.sleep(0.6)

# Clear text
mgba.press_buttons(["B"])
time.sleep(0.4)
mgba.press_buttons(["B"])
time.sleep(0.4)

print("Toggle complete! Current position:", get_pos())
mgba.take_screenshot()
