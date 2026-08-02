import mgba
import time

print("Starting Master Overworld Doorway Sweep for Underground Path...")

# Step 1: Close dialogue and exit Trade House
mgba.press_buttons(["B", "B", "sleep 300", "Down", "Down", "Right", "Down", "Down", "sleep 1000"])

pos = mgba.get_coordinates()
print(f"Position after exiting building: {pos}")
s_out = mgba.take_screenshot()
print(f"Outside screenshot: {s_out}")

# We are outside on Route 8 around (9, 12) or (13, 16)
# Let's test walking to candidate doorway areas on Western Sector & Lower Highway!

# Candidate 1: Col 11, Row 19
# From (9, 12): Down 4 to (9, 16), Right 2 to (11, 16), Down 3 to (11, 19)
seq_c1 = ["Down", "Down", "Down", "Down", "Right", "Right", "Down", "Down", "sleep 500"]
mgba.press_buttons(seq_c1)
p_c1 = mgba.get_coordinates()
print(f"Position at Candidate 1 (11, 19) area: {p_c1}")
s_c1 = mgba.take_screenshot()
print(f"Candidate 1 screenshot: {s_c1}")

# Try stepping Up into doorway at (11, 19)
mgba.press_buttons(["Up", "sleep 1000"])
p_c1_door = mgba.get_coordinates()
print(f"Position after Up at (11, 19): {p_c1_door}")
s_c1_door = mgba.take_screenshot()
print(f"Candidate 1 doorway screenshot: {s_c1_door}")
