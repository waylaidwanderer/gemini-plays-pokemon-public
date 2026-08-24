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

# Starting at (11, 12) outside Pokémon Center on Cinnabar Island
# Walk Left to (6, 12), then UP to (6, 3) and enter Mansion
steps = [
    ("Left", {"x": 10, "y": 12}),
    ("Left", {"x": 9, "y": 12}),
    ("Left", {"x": 8, "y": 12}),
    ("Left", {"x": 7, "y": 12}),
    ("Left", {"x": 6, "y": 12}),
    ("Up", {"x": 6, "y": 11}),
    ("Up", {"x": 6, "y": 10}),
    ("Up", {"x": 6, "y": 9}),
    ("Up", {"x": 6, "y": 8}),
    ("Up", {"x": 6, "y": 7}),
    ("Up", {"x": 6, "y": 6}),
    ("Up", {"x": 6, "y": 5}),
    ("Up", {"x": 6, "y": 4}),
    ("Up", {"x": 6, "y": 3}),
]

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (6, 3) on Cinnabar Island! Entering Pokémon Mansion...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5) # Wait for transition fade
    pos = mgba.get_coordinates()
    print(f"Entered Mansion! Landing position: {pos}")
else:
    print("Failed to reach Mansion entrance.")
