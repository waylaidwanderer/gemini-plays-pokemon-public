import mgba
import time

# 1. Walk to (23, 28)
pos = mgba.get_coordinates()
print(f"Starting at {pos}")

if pos['x'] != 23 or pos['y'] != 28:
    mgba.press_buttons(["Right"])
    time.sleep(0.35)
    pos = mgba.get_coordinates()
    print(f"Moved to {pos}")

# 2. Walk UP column 23 as far as possible
print("Exploring Upward along column 23...")
for y in range(27, 5, -1):
    mgba.press_buttons(["Up"])
    time.sleep(0.35)
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        # Try once more
        time.sleep(0.5)
        mgba.press_buttons(["Up"])
        time.sleep(0.35)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            print(f"Blocked going Up at {pos}")
            break
    pos = new_pos
    print(f"Reached {pos}")

# 3. Explore Left and Right at the top of the walkway to see the doors!
pos = mgba.get_coordinates()
print(f"At {pos}, exploring Left...")
for x in range(pos['x'] - 1, pos['x'] - 10, -1):
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

screenshot_path = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_path}")
