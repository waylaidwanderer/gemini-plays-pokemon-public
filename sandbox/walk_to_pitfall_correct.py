import mgba
import time

# 1. Dismiss the "Got away safely!" screen
mgba.press_buttons(["B"])
time.sleep(1.5) # Wait for fade back to overworld

# 2. Walk from (21, 6) to (26, 3) and drop
steps = [
    ("Left", {"x": 20, "y": 6}),
    ("Left", {"x": 19, "y": 6}),
    ("Up", {"x": 19, "y": 5}),
    ("Up", {"x": 19, "y": 4}),
    ("Up", {"x": 19, "y": 3}),
    ("Right", {"x": 20, "y": 3}),
    ("Right", {"x": 21, "y": 3}),
    ("Right", {"x": 22, "y": 3}),
    ("Right", {"x": 23, "y": 3}),
    ("Right", {"x": 24, "y": 3}),
    ("Right", {"x": 25, "y": 3}),
    ("Right", {"x": 26, "y": 3}),
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
    print("Reached (26, 3) on 3F East! Stepping DOWN onto (26, 4) to fall through pitfall...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0) # Wait for drop animation
    pos = mgba.get_coordinates()
    print(f"Landed on 1F East inside fenced room! Position: {pos}")
else:
    print("Failed to reach pitfall.")
