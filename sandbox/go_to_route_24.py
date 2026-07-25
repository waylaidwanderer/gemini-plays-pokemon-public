import mgba
import time

# We are at (16, 16).
# The NPC is stunned at (15, 18).
# Let's walk to Route 24 via row 19:
# 1. Down 3 times to (16, 19)
# 2. Left 16 times to (0, 19)
# 3. Up 7 times to (0, 12)
# 4. Right 20 times to (20, 12)
# 5. Up 12 times to go north onto Route 24
steps = ["Down"] * 3 + ["Left"] * 16 + ["Up"] * 7 + ["Right"] * 20 + ["Up"] * 12

print("Moving to Route 24 via row 19...")
for step in steps:
    mgba.press_buttons([step])
    time.sleep(0.3)

print("Done!")
