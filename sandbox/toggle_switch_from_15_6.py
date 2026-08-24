import mgba
import time

# 1. Dismiss the battle screen
mgba.press_buttons(["B"])
time.sleep(1.5) # Wait for fade back to overworld

# 2. Walk from (15, 6) on 2F East to (12, 9)
steps = [
    ("Right", {"x": 16, "y": 6}),
    ("Right", {"x": 17, "y": 6}),
    ("Right", {"x": 18, "y": 6}),
    ("Down", {"x": 18, "y": 7}),
    ("Down", {"x": 18, "y": 8}),
    ("Down", {"x": 18, "y": 9}),
    ("Down", {"x": 18, "y": 10}),
    ("Left", {"x": 17, "y": 10}),
    ("Left", {"x": 16, "y": 10}),
    ("Left", {"x": 15, "y": 10}),
    ("Left", {"x": 14, "y": 10}),
    ("Left", {"x": 13, "y": 10}),
    ("Left", {"x": 12, "y": 10}),
    ("Up", {"x": 12, "y": 9}),
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
    print("Successfully reached (12, 9) on 2F East! Interacting with switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])   # Select YES to toggle to State B
    time.sleep(1.0)
    mgba.press_buttons(["B"])   # Dismiss dialog
    time.sleep(0.5)
    print("Switch toggled to State B! Current coordinates:", mgba.get_coordinates())
else:
    print("Failed to reach switch on 2F East.")
