import mgba
import time

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

# Starting at (6, 12) on 2F West
# Walk to (12, 10)
steps = [
    ("Up", {"x": 6, "y": 11}),
    ("Right", {"x": 7, "y": 11}),
    ("Right", {"x": 8, "y": 11}),
    ("Right", {"x": 9, "y": 11}),
    ("Right", {"x": 10, "y": 11}),
    ("Right", {"x": 11, "y": 11}),
    ("Right", {"x": 12, "y": 11}),
    ("Up", {"x": 12, "y": 10}),
]

success = True
for d, c in steps:
    if not walk_step(d, c):
        success = False
        break

if success:
    print("Reached (12, 10)! Testing if Row 9 gate at (12, 9) is open (State B) or closed (State A)...")
    if walk_step("Up", {"x": 12, "y": 9}):
        print("Mansion is in STATE B! Row 9 gate is OPEN.")
    else:
        print("Mansion is in STATE A! Row 9 gate is CLOSED.")

