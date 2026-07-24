import mgba
import time

def step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    print(f"Step {direction}: {pos_before} -> {pos_after}")
    return pos_before != pos_after

# Let's walk back to the left from (24, 23)
# To go left:
# First we need to go down to row 24 or 25 since row 23 has those rocks/bars?
# Wait, at (24, 23), can we walk Left? 
# Let's try to walk Left 5 times and see what happens.
for i in range(15):
    if not step("Left"):
        print("Blocked walking Left.")
        break

# Let's see what coordinates we are at now
print(f"Final coordinates: {mgba.get_coordinates()}")
mgba.take_screenshot()
