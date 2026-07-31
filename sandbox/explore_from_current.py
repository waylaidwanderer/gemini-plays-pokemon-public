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

# We are at (21, 25) on B4F
print("Start Position on B4F:", mgba.get_coordinates())

# Let's walk Left systematically up to 10 steps to explore B4F!
print("Walking Left...")
for i in range(1, 11):
    mgba.press_buttons(["Left"])
    pos = wait_for_movement()
    print(f"Step {i} Left: {pos}")

# Take a screenshot to see the new area
screenshot_path = mgba.take_screenshot()
print("Screenshot after exploring Left:", screenshot_path)
