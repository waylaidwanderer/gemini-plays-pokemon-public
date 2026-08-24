import mgba
import time

def walk_step(direction, expected_coords):
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {direction}, current position: {pos}")
    if pos != expected_coords:
        print(f"Desync! Expected {expected_coords}, got {pos}")
        return False
    return True

# Starting at (6, 11)
steps = [
    ("Left", {"x": 5, "y": 11}),
    ("Left", {"x": 4, "y": 11}),
    ("Down", {"x": 4, "y": 12}),
    ("Down", {"x": 4, "y": 13}),
    ("Left", {"x": 3, "y": 13}),
    ("Left", {"x": 2, "y": 13}),
]

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (2, 13) successfully! Turning UP and interacting...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(0.3)
    img_path = mgba.take_screenshot()
    print(f"Screenshot saved to {img_path}")
else:
    print("Navigation failed.")
