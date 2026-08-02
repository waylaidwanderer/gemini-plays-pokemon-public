import mgba
import time

print("Starting Master Basin Doorway Probe for Underground Path...")

# Close dialogue and exit current building
mgba.press_buttons(["B", "B", "sleep 300", "Down", "Down", "Down", "sleep 1000"])

pos = mgba.get_coordinates()
print(f"Position after exiting building: {pos}")
s_out = mgba.take_screenshot()
print(f"Outside screenshot: {s_out}")

# Now outside on Route 8.
# Let's test walking to candidate doorway areas on Route 8 & Western Gatehouse Map!
# Candidate 1: Col 25, Row 20 / Row 25
# Candidate 2: Col 35, Row 19
# Candidate 3: Col 38, Row 17
# Candidate 4: Col 9, Row 11
# Candidate 5: Col 11, Row 19

# Step 1: Walk to Col 25 Row 20 on Lower Highway
# From (13, 16): Right 12 to (25, 16), then Down 4 to (25, 20)
seq_col25 = ["Right"] * 12 + ["Down"] * 4 + ["sleep 500"]
mgba.press_buttons(seq_col25)

p25 = mgba.get_coordinates()
print(f"Position at Col 25: {p25}")
s25 = mgba.take_screenshot()
print(f"Col 25 screenshot: {s25}")

# Try stepping Up to check for doorway at Col 25
mgba.press_buttons(["Up", "sleep 1000"])
p25_door = mgba.get_coordinates()
print(f"Position after Up at Col 25: {p25_door}")

s25_door = mgba.take_screenshot()
print(f"Col 25 doorway screenshot: {s25_door}")
