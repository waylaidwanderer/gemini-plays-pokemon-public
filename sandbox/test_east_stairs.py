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

# We are at (16, 17) on B3F
print("Start Position:", mgba.get_coordinates())

# 1. Step Up onto (16, 16) UP spinner -> slides to (16, 13) stopper
print("Stepping Up onto spinner...")
mgba.press_buttons(["Up"])
time.sleep(2.5) # Let the slide finish
pos = wait_for_movement()
print("Landed at stopper:", pos)

# 2. Walk Right to (19, 13)
print("Walking to (19, 13)...")
mgba.press_buttons(["Right", "Right", "Right"])
pos = wait_for_movement()
print("At:", pos)

# 3. Walk Down to (19, 15)
print("Walking to (19, 15)...")
mgba.press_buttons(["Down", "Down"])
pos = wait_for_movement()
print("At:", pos)

# 4. Jump Down the ledge onto (19, 16) -> should land at (19, 17)
print("Jumping Down the ledge...")
mgba.press_buttons(["Down"])
time.sleep(1.0) # Let jump finish
pos = wait_for_movement()
print("Landed at:", pos)

# 5. Walk Down to (19, 19)
print("Walking Down to (19, 19)...")
mgba.press_buttons(["Down", "Down"])
pos = wait_for_movement()
print("At:", pos)

# 6. Walk Left to (18, 19) (stairs!)
print("Walking Left to stairs...")
mgba.press_buttons(["Left"])
time.sleep(3.0) # Let potential warp finish
pos = wait_for_movement()
print("Position after walking into stairs:", pos)

screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
