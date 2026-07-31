import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.15)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.15)
        p2 = mgba.get_coordinates()
    return p1

# We are at (10, 11) on B3F
print("Start Position:", mgba.get_coordinates())

# Walk Up to (10, 10) UP spinner and see where we slide!
print("Pressing Up to step onto (10, 10) spinner...")
mgba.press_buttons(["Up"])
time.sleep(3.0) # Let the slide finish
pos = wait_for_movement()
print("Position after slide:", pos)

# Take screenshot
screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
