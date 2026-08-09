import mgba
import time

print("Starting explore_left.py")
curr = mgba.get_coordinates()
print(f"Start coordinates: {curr}")

# Let's try to walk:
# 1. UP 2 steps to (15, 23)
for _ in range(2):
    mgba.press_buttons(["Up", "sleep 350"])
    print(f"Moved Up. Current: {mgba.get_coordinates()}")

# 2. LEFT 5 steps
for _ in range(5):
    mgba.press_buttons(["Left", "sleep 350"])
    print(f"Moved Left. Current: {mgba.get_coordinates()}")

print("Done with sequence.")
