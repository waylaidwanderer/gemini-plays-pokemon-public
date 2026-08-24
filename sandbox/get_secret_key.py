import mgba
import time
import os

# Clean up obsolete temporary scripts to maintain workspace hygiene
obsolete = [
    "walk_to_pitfall_correct.py",
    "get_secret_key_clean.py"
]
for f in obsolete:
    if os.path.exists(f):
        try:
            os.remove(f)
            print(f"Deleted obsolete file: {f}")
        except Exception as e:
            print(f"Error deleting {f}: {e}")

# 1. Dismiss the "Got away safely!" screen
mgba.press_buttons(["B"])
time.sleep(1.5) # Wait for fade back to overworld

# 2. Walk from (20, 4) to (1, 5) on B1F
steps = [
    ("Left", {"x": 19, "y": 4}),
    ("Down", {"x": 19, "y": 5}),
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
    print("Successfully bypassed B1F East wall! Walking Left along Row 5 to the Secret Key...")
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
