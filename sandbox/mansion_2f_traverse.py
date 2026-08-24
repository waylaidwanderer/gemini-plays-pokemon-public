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

# Current position is (7, 11)
# Step 1: Left to (6, 11)
# Step 2: Up to (6, 10)
# Step 3: Up to (6, 9)
# Step 4: Up to (6, 8)
# Step 5: Up to (6, 7)
# Step 6: Left to (5, 7)
# Step 7: Down to (5, 8)
# Step 8: Down to (5, 9)

steps = [
    ("Left", {"x": 6, "y": 11}),
    ("Up", {"x": 6, "y": 10}),
    ("Up", {"x": 6, "y": 9}),
    ("Up", {"x": 6, "y": 8}),
    ("Up", {"x": 6, "y": 7}),
    ("Left", {"x": 5, "y": 7}),
    ("Down", {"x": 5, "y": 8}),
    ("Down", {"x": 5, "y": 9}),
]

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (5, 9) successfully!")
    img_path = mgba.take_screenshot()
    print(f"Screenshot saved to {img_path}")
else:
    print("Navigation failed.")
