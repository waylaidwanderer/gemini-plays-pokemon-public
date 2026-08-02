import mgba
import time

print("Starting West Route 5 South Exit Script...")

# Step 1: Exit building
mgba.press_buttons(["Down", "Down", "Down", "sleep 1000"])

pos = mgba.get_coordinates()
print(f"Position outside building: {pos}")

# Step 2: Walk to Row 20 (13, 20)
mgba.press_buttons(["Down", "Down", "Down", "Down", "sleep 300"])

# Step 3: Walk Left 13 steps to Col 0 (0, 20)
mgba.press_buttons(["Left"] * 13 + ["sleep 300"])

p_col0 = mgba.get_coordinates()
print(f"Position at Col 0 Row 20: {p_col0}")
s_col0 = mgba.take_screenshot()
print(f"Col 0 screenshot: {s_col0}")

# Step 4: Walk Down 15 steps along Col 0 to Route 5!
mgba.press_buttons(["Down"] * 15 + ["sleep 1000"])

p_route5 = mgba.get_coordinates()
print(f"Position after walking South: {p_route5}")
s_route5 = mgba.take_screenshot()
print(f"Route 5 screenshot: {s_route5}")
