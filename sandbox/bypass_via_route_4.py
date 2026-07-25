import mgba
import time

# We are at (11, 16).
# Let's use the Gen 1 Map Connection Offset Bypass:
# 1. Left 12 times to transition to Route 4 at y=8
# 2. Up 4 times to (89, 4) on Route 4
# 3. Right 5 times to transition back to Cerulean City at (0, 12)
# 4. Right 20 times to (20, 12) in Cerulean City
# 5. Up 12 times to go north onto Route 24
steps = ["Left"] * 12 + ["Up"] * 4 + ["Right"] * 5 + ["Right"] * 20 + ["Up"] * 12

print("Executing Gen 1 Connection Offset Bypass...")
for step in steps:
    mgba.press_buttons([step])
    time.sleep(0.3)

print("Done!")
