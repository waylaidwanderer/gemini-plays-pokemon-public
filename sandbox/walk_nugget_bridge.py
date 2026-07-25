import mgba
import time

def move(direction, steps=1):
    for i in range(steps):
        mgba.press_buttons([direction])
        time.sleep(0.15)
        pos = mgba.get_coordinates()
        print(f"Moved {direction}. Now at {pos}")

# Starting at (10, 35) on Route 24
print("Walking Up Nugget Bridge...")
for i in range(25):
    mgba.press_buttons(["Up"])
    time.sleep(0.15)
    pos = mgba.get_coordinates()
    print(f"Step {i}: Position: {pos}")

screenshot = mgba.take_screenshot()
print(f"Screenshot taken at end of bridge: {screenshot}")
