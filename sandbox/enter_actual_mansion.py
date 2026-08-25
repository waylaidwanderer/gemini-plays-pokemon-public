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

# Starting at (11, 5) on Cinnabar Island
# Walk UP to Row 4, Left to Column 6 on Row 4, and UP to (6, 3) to enter actual Mansion
steps = [
    ("Up", {"x": 11, "y": 4}),
    ("Left", {"x": 10, "y": 4}),
    ("Left", {"x": 9, "y": 4}),
    ("Left", {"x": 8, "y": 4}),
    ("Left", {"x": 7, "y": 4}),
    ("Left", {"x": 6, "y": 4}),
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
