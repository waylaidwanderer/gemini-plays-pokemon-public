import mgba
import time

def move(direction, steps=1):
    for i in range(steps):
        mgba.press_buttons([direction])
        time.sleep(0.18)
        pos = mgba.get_coordinates()
        print(f"Moved {direction}. Now at {pos}")

# Start at (15, 4) on Route 24
print("Moving Down to row 8...")
move("Down", 4)

print("Moving Right to Route 25...")
# Walk Right 8 steps to transition to Route 25
for i in range(8):
    mgba.press_buttons(["Right"])
    time.sleep(0.18)
    pos = mgba.get_coordinates()
    print(f"Step {i} Right. Position: {pos}")

time.sleep(0.5)
screenshot = mgba.take_screenshot()
print(f"Transition completed. Screenshot: {screenshot}")
