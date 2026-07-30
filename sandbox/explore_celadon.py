import mgba
import time

# 1. Press Down to exit the Prize Exchange
print("Exiting building...")
mgba.press_buttons(["Down"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print(f"On overworld at: {pos}")

# 2. Walk Left along Row 28 as far as possible
print("Exploring Left along Row 28...")
for x in range(pos['x'] - 1, -1, -1):
    mgba.press_buttons(["Left"])
    time.sleep(0.35)
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        # Try once more
        time.sleep(0.5)
        mgba.press_buttons(["Left"])
        time.sleep(0.35)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            print(f"Blocked going Left at {pos}")
            break
    pos = new_pos
    print(f"Reached {pos}")

# 3. Take a screenshot to see our surroundings
screenshot_path = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_path}")
