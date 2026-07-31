import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.1)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.1)
        p2 = mgba.get_coordinates()
    return p1

# We are at B3F (8, 11)
print("Start Position:", mgba.get_coordinates())

# 1. Walk to the right side
print("Walking to (10, 14)...")
mgba.press_buttons(["Right", "Right", "Down", "Down", "Down"])
wait_for_movement()

print("Spinning through row 14 to (9, 16)...")
mgba.press_buttons(["Left"])
time.sleep(1.0)
wait_for_movement()

print("Spinning through row 16 to (15, 17)...")
mgba.press_buttons(["Right", "Right"])
time.sleep(1.5)
wait_for_movement()

print("Spinning UP to (14, 15)...")
mgba.press_buttons(["Left"])
time.sleep(1.0)
wait_for_movement()

print("Walking to (15, 14)...")
mgba.press_buttons(["Right", "Up"])
wait_for_movement()

print("Spinning to (16, 13)...")
mgba.press_buttons(["Right"])
time.sleep(1.0)
wait_for_movement()

# 2. From (16, 13), walk to (2, 9)
# First, walk UP to row 10
print("Walking UP to row 10...")
mgba.press_buttons(["Up", "Up", "Up"]) # from (16, 13) to (16, 10)
wait_for_movement()

# Walk Left to (13, 10)
print("Walking Left to (13, 10)...")
mgba.press_buttons(["Left", "Left", "Left"])
wait_for_movement()

# Spin DOWN to (14, 12)
print("Spinning DOWN to (14, 12)...")
mgba.press_buttons(["Left"])
time.sleep(1.0)
wait_for_movement()

# Walk to (12, 13)
print("Walking to (12, 13)...")
mgba.press_buttons(["Down", "Left", "Left"])
wait_for_movement()

# Spin to (2, 9)
print("Spinning to (2, 9)...")
mgba.press_buttons(["Left"])
time.sleep(1.5)
pos = wait_for_movement()
print(f"At B3F left side: {pos}")

# 3. From (2, 9), walk to (2, 14) via row 14 Left spinner
print("Navigating to row 14...")
mgba.press_buttons(["Right", "Down", "Down", "Down", "Down", "Right", "Down", "Left"])
time.sleep(1.0)
pos = wait_for_movement()
print(f"Landed at: {pos}")

# 4. From (2, 14), walk Down to row 17
print("Walking to bottom-left area...")
mgba.press_buttons(["Down", "Down", "Down"])
pos = wait_for_movement()
print(f"At row 17 position: {pos}")

# Try to find stairs: test (1, 17), (2, 17), (3, 17)
# Let's walk Left to (1, 17)
print("Testing (1, 17)...")
mgba.press_buttons(["Left"])
pos = wait_for_movement()
print(f"Position: {pos}")

# Take a screenshot
screenshot_path = mgba.take_screenshot()
print(f"Screenshot: {screenshot_path}")
