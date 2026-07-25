import mgba
import time

def move(direction, steps=1):
    for i in range(steps):
        mgba.press_buttons([direction])
        time.sleep(0.18)

# Start at (10, 14) on Route 24
print("Exploring north on Route 24...")
move("Up", 6)

time.sleep(0.5)
screenshot = mgba.take_screenshot()
print(f"Reached north end. Screenshot: {screenshot}")
pos = mgba.get_coordinates()
print(f"Final position (internal, note warning): {pos}")
