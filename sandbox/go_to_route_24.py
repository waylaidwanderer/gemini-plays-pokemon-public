import mgba
import time

# We are at (19, 18).
# Let's walk to Route 24:
# 1. Left 19 times to (0, 18)
# 2. Up 6 times to (0, 12)
# 3. Right 20 times to (20, 12)
# 4. Up 12 times to go north onto Route 24
steps = ["Left"] * 19 + ["Up"] * 6 + ["Right"] * 20 + ["Up"] * 12

print("Moving to Route 24...")
for step in steps:
    mgba.press_buttons([step])
    time.sleep(0.3)

print("Done!")
