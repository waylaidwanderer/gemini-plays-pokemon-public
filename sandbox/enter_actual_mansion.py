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

# Starting at (7, 10) on Cinnabar Island
# Walk DOWN to Row 12, then RIGHT to Column 18, then UP to Row 5, and LEFT to Column 6
steps = [
    ("Down", {"x": 7, "y": 11}),
    ("Down", {"x": 7, "y": 12}),
    ("Right", {"x": 8, "y": 12}),
    ("Right", {"x": 9, "y": 12}),
    ("Right", {"x": 10, "y": 12}),
    ("Right", {"x": 11, "y": 12}),
    ("Right", {"x": 12, "y": 12}),
    ("Right", {"x": 13, "y": 12}),
    ("Right", {"x": 14, "y": 12}),
    ("Right", {"x": 15, "y": 12}),
    ("Right", {"x": 16, "y": 12}),
    ("Right", {"x": 17, "y": 12}),
    ("Right", {"x": 18, "y": 12}),
    # Walk UP Column 18 past the fence
    ("Up", {"x": 18, "y": 11}),
    ("Up", {"x": 18, "y": 10}),
    ("Up", {"x": 18, "y": 9}),
    ("Up", {"x": 18, "y": 8}),
    ("Up", {"x": 18, "y": 7}),
    ("Up", {"x": 18, "y": 6}),
    ("Up", {"x": 18, "y": 5}),
    # Walk LEFT along Row 5 to Column 6
    ("Left", {"x": 17, "y": 5}),
    ("Left", {"x": 16, "y": 5}),
    ("Left", {"x": 15, "y": 5}),
    ("Left", {"x": 14, "y": 5}),
    ("Left", {"x": 13, "y": 5}),
    ("Left", {"x": 12, "y": 5}),
    ("Left", {"x": 11, "y": 5}),
    ("Left", {"x": 10, "y": 5}),
    ("Left", {"x": 9, "y": 5}),
    ("Left", {"x": 8, "y": 5}),
    ("Left", {"x": 7, "y": 5}),
    ("Left", {"x": 6, "y": 5}),
    # Walk UP Column 6 to door at (6, 3)
    ("Up", {"x": 6, "y": 4}),
    ("Up", {"x": 6, "y": 3}),
]

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached actual Pokémon Mansion entrance at (6, 3)! Entering...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5) # Wait for map transition
    pos = mgba.get_coordinates()
    print(f"Entered actual Pokémon Mansion 1F West! Position: {pos}")
else:
    print("Failed to reach Mansion entrance.")
