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

# We are at (19, 15) on B3F
print("Start Position:", mgba.get_coordinates())

# 1. Walk Up to (19, 11)
print("Walking Up to (19, 11)...")
for _ in range(4):
    mgba.press_buttons(["Up"])
    wait_for_movement()
print("At:", mgba.get_coordinates())

# 2. Walk Left 2 steps onto (17, 11) LEFT spinner -> should slide Left into Left Room!
print("Stepping Left onto LEFT spinner...")
mgba.press_buttons(["Left"])
wait_for_movement()
mgba.press_buttons(["Left"])
time.sleep(3.0) # Wait for slide
pos = wait_for_movement()
print("Landed at:", pos)

# Take screenshot
screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
