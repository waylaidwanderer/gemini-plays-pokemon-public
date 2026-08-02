import mgba
import time

print("Starting Complete Route 8 Doorway Sweep...")

# Close dialogue and exit building
mgba.press_buttons(["B", "sleep 300", "Down", "Down", "Down", "sleep 1000"])

pos = mgba.get_coordinates()
print(f"Position after exiting building: {pos}")
s1 = mgba.take_screenshot()
print(f"Outside screenshot: {s1}")

# We are outside on Route 8 (around 13, 16 / 13, 17)
# Let's probe Col 9, Col 11, Col 19, Col 25, Col 30 for doorways!
# First probe West along Row 16/17 towards Col 9 & Col 5
seq_west = ["Left", "Left", "Left", "Left", "sleep 300"]
mgba.press_buttons(seq_west)

pos_w = mgba.get_coordinates()
print(f"Position after Left 4: {pos_w}")

# Try stepping Up to check for doorway
mgba.press_buttons(["Up", "Up", "sleep 500"])
pos_door = mgba.get_coordinates()
print(f"Position after stepping Up: {pos_door}")
s_door = mgba.take_screenshot()
print(f"Screenshot at door test: {s_door}")
