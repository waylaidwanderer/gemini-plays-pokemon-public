import mgba
import time

def move(direction, steps=1):
    for i in range(steps):
        mgba.press_buttons([direction])
        time.sleep(0.18)

# Start at (10, 29)
print("Starting Slalom...")
move("Right", 1)  # to (11, 29)
move("Up", 3)     # to (11, 26)
move("Left", 1)   # to (10, 26)
move("Up", 3)     # to (10, 23)
move("Right", 1)  # to (11, 23)
move("Up", 3)     # to (11, 20)
move("Left", 1)   # to (10, 20)
move("Up", 6)     # to (10, 14)

time.sleep(0.5)
screenshot = mgba.take_screenshot()
print(f"Slalom completed. Screenshot: {screenshot}")
