import mgba
import time

def step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    print(f"Moved {direction}: {pos_before} -> {pos_after}")
    return pos_after

pos = mgba.get_coordinates()
print(f"Starting at {pos}")

# Walk down to (20, 16)
pos = step("Down")

# Try to walk down to (20, 17)
pos = step("Down")

# Let's take a screenshot to verify what happens
screenshot_file = mgba.take_screenshot()
print(f"Captured screenshot: {screenshot_file}")
