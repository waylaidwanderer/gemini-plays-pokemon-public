import mgba
import time

# Starting at (10, 6) on B1F East in State B
# Walk Up to Row 5 Column 10, then Left through the gate at (9, 5) to B1F West
steps = [
    ("Up", {"x": 10, "y": 5}),
    ("Left", {"x": 9, "y": 5}),  # Cross through open gate at (9, 5)
    ("Left", {"x": 8, "y": 5}),
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
    print("Successfully crossed through B1F gate! Walking Left along Row 5 to the Secret Key...")
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
    print("Failed to navigate B1F.")
