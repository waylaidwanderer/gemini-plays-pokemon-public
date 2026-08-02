import mgba
import time

print("Starting Cerulean City Route 5 South Exit Probe...")

# Step 1: Walk Up out of the dead-end alcove (17, 28) to Row 20 (17, 20)
mgba.press_buttons(["Up"] * 8 + ["sleep 500"])

pos = mgba.get_coordinates()
print(f"Position on Row 20: {pos}")

# Step 2: Test walking West along Row 20 to Col 9, then South along Col 9
# From (17, 20): Left 8 to (9, 20), then Down 15 steps!
seq_west = ["Left"] * 8 + ["Down"] * 15 + ["sleep 1000"]
mgba.press_buttons(seq_west)

pos_after_west = mgba.get_coordinates()
print(f"Position after West test: {pos_after_west}")
s_west = mgba.take_screenshot()
print(f"West test screenshot: {s_west}")
