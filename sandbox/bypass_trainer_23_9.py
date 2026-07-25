import mgba
import time

def move(direction, steps=1):
    for i in range(steps):
        mgba.press_buttons([direction])
        time.sleep(0.18)

# Start at (18, 7)
print("Executing bypass around column 21...")
move("Right", 2)  # to (20, 7)
move("Down", 1)   # to (20, 8)
move("Right", 3)  # to (23, 8)

time.sleep(0.5)
screenshot = mgba.take_screenshot()
print(f"Bypass completed. Screenshot: {screenshot}")
