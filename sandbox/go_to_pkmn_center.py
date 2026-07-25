import mgba
import time

# We are at (20, 6).
# Let's walk to the Pokémon Center:
# 1. Down 6 times to (20, 12)
# 2. Left 20 times to (0, 12)
# 3. Down 5 times to (0, 17)
# 4. Right 19 times to (19, 17)
steps = ["Down"] * 6 + ["Left"] * 20 + ["Down"] * 5 + ["Right"] * 19

print("Starting movement to Pokémon Center...")
for step in steps:
    mgba.press_buttons([step])
    time.sleep(0.3)

print("Finished movement!")
