import mgba
import time

# We are at (12, 16).
# Let's explore the left side to find a gap to walk Up.
# At each column from 12 down to 0, we will:
# 1. Try to walk Up.
# 2. If it succeeds, we will stop and print the coordinates.
# But since we can't read coordinates in real-time, let's just execute a sequence:
# We'll go to column 0, and then try to walk Up.
# Wait, let's check Route 4 entrance: Route 4 is at the west.
# Let's walk Left 12 times to reach column 0.
# Then walk Up 10 times to see if we can go north on the far left!
# Then walk Right 10 times to see where we end up.

steps = ["Left"] * 12 + ["Up"] * 10 + ["Right"] * 10
for step in steps:
    mgba.press_buttons([step])
    time.sleep(0.3)

print("Finished far-left exploration!")
