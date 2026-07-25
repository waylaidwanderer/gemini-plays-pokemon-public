import mgba
import time

def move(direction, steps=1):
    for i in range(steps):
        print(f"Pressing {direction}...")
        mgba.press_buttons([direction])
        time.sleep(0.18)
        pos = mgba.get_coordinates()
        print(f"Step {i}: Position is {pos}")

# Start at (3, 8) on Route 25
print("Walking Right along the paved path...")
move("Right", 10)

time.sleep(0.5)
screenshot = mgba.take_screenshot()
print(f"Completed walking. Screenshot: {screenshot}")
