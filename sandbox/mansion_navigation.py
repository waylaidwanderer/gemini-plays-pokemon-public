import mgba
import time

# Current position is (5, 11)
# Let's try pressing Up to step onto (5, 10) and see if we warp
print("Trying Up...")
mgba.press_buttons(["Up"])
time.sleep(0.3)
pos = mgba.get_coordinates()
print(f"Position after Up: {pos}")

# If we didn't warp (still on 1F), let's try going to (6, 10) and then Left to (5, 10)
if pos == {'x': 5, 'y': 10}:
    print("We are on (5, 10) but didn't warp. Let's try stepping Left to warp?")
    # Maybe we are blocked or standing there. Let's try to see if stepping Left from (6,10) is the warp.
elif pos == {'x': 5, 'y': 11}:
    print("Up was blocked! We are still at (5, 11). Let's go Right to (6, 11), Up to (6, 10), and Left to (5, 10)")
    mgba.press_buttons(["Right", "Up", "Left"])
    time.sleep(1.0)
    pos2 = mgba.get_coordinates()
    print(f"Position after Right-Up-Left: {pos2}")
