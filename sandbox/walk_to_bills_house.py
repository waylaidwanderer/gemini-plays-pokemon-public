import mgba
import time

def move(direction, steps=1):
    for i in range(steps):
        mgba.press_buttons([direction])
        time.sleep(0.18)

# Start at (24, 5)
print("Walking to the east side of the maze...")
move("Down", 2)   # to (24, 7)
move("Right", 3)  # to (27, 7)
move("Up", 1)     # to (27, 6)
move("Right", 5)  # to (32, 6) which is past column 28!

time.sleep(0.5)
screenshot = mgba.take_screenshot()
print(f"Pathing completed. Screenshot: {screenshot}")
