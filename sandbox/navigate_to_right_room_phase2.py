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

# We start at B3F (2, 9)
print("Start Position:", mgba.get_coordinates())

# 1. Left to (1, 9)
mgba.press_buttons(["Left"])
wait_for_movement()
print("At (1, 9):", mgba.get_coordinates())

# 2. Up to (1, 7)
mgba.press_buttons(["Up", "Up"])
wait_for_movement()
print("At (1, 7):", mgba.get_coordinates())

# 3. Right to (5, 7)
mgba.press_buttons(["Right", "Right", "Right", "Right"])
wait_for_movement()
print("At (5, 7):", mgba.get_coordinates())

# 4. Down to (5, 9)
mgba.press_buttons(["Down", "Down"])
wait_for_movement()
print("At (5, 9):", mgba.get_coordinates())

# 5. Right to (7, 9)
mgba.press_buttons(["Right", "Right"])
wait_for_movement()
print("At (7, 9):", mgba.get_coordinates())

# 6. Up to (7, 7)
mgba.press_buttons(["Up", "Up"])
wait_for_movement()
print("At (7, 7):", mgba.get_coordinates())

# 7. Right to (13, 7)
mgba.press_buttons(["Right", "Right", "Right", "Right", "Right", "Right"])
wait_for_movement()
print("At (13, 7):", mgba.get_coordinates())

# 8. Down to (13, 10) and let it spin to (14, 12)
mgba.press_buttons(["Down", "Down", "Down"])
# Wait extra for the spin to complete
time.sleep(1.0)
wait_for_movement()
print("Landed after spin at:", mgba.get_coordinates())

# 9. Up to (14, 10)
mgba.press_buttons(["Up", "Up"])
wait_for_movement()
print("At (14, 10):", mgba.get_coordinates())

# 10. Right to (19, 10)
mgba.press_buttons(["Right", "Right", "Right", "Right", "Right"])
wait_for_movement()
print("At (19, 10):", mgba.get_coordinates())

# Take a screenshot
screenshot_path = mgba.take_screenshot()
print(f"Screenshot at End: {screenshot_path}")

