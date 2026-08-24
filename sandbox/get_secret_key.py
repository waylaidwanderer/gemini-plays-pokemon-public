import mgba
import time
import os

# Starting at (18, 5) on B1F East in State B
# Walk Down to Row 6, Left to Column 9, Up to Row 5, and Left to B1F West
steps = [
    ("Down", {"x": 18, "y": 6}),
    ("Left", {"x": 17, "y": 6}),
    ("Left", {"x": 16, "y": 6}),
    ("Left", {"x": 15, "y": 6}),
    ("Left", {"x": 14, "y": 6}),
    ("Left", {"x": 13, "y": 6}),
    ("Left", {"x": 12, "y": 6}),
    ("Left", {"x": 11, "y": 6}),
    ("Left", {"x": 10, "y": 6}),
    ("Left", {"x": 9, "y": 6}),
    ("Up", {"x": 9, "y": 5}),  # Open gate in State B!
]

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        mgba.press_buttons([direction])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.2)
    return False

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Successfully crossed through gate at (9, 5)! Walking Left along Row 5 to the Secret Key...")
    curr = mgba.get_coordinates()
    while curr['x'] > 1:
        if not walk_step("Left", {"x": curr['x'] - 1, "y": 5}):
            success = False
            break
        curr = mgba.get_coordinates()
        
    if success:
        print("Successfully reached (1, 5) on B1F West! Standing facing UP and retrieving the Secret Key...")
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        mgba.press_buttons(["A"])   # Opens "Obtained the SECRET KEY!"
        time.sleep(1.5)
        mgba.press_buttons(["A"])   # Dismiss obtain text
        time.sleep(1.0)
        img_path = mgba.take_screenshot()
        print(f"Secret Key retrieved successfully! Screenshot: {img_path}")
        print("Current position:", mgba.get_coordinates())
    else:
        print("Failed to reach Secret Key on B1F West.")
else:
    print("Failed to navigate B1F East.")
