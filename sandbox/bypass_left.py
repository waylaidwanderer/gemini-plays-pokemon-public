import mgba
import time

def move(direction, steps=1):
    for _ in range(steps):
        mgba.press_buttons([direction])
        time.sleep(0.1)

# Current position is (15, 18)
# Step 1: Walk Up 2 steps to row 16
print("Moving Up to row 16...")
move("Up", 2)

# Step 2: Walk Left until map transitions to Route 4
print("Walking Left to Route 4...")
for i in range(25):
    # Get current coordinates
    pos = mgba.get_coordinates()
    print(f"Step {i}: Position is {pos}")
    # In some harness states get_coordinates returns {'x': 0, 'y': 0}.
    # We can also check if we transitioned by checking if we have walked a lot.
    # To be extremely safe, we will just walk Left 18 times.
    move("Left", 1)

print("Completed walking Left. Capturing screenshot...")
screenshot = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot}")
