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

# Starting at (6, 11) on 2F West
steps = [
    ("Left", {"x": 5, "y": 11}),
    ("Left", {"x": 4, "y": 11}),
    ("Left", {"x": 3, "y": 11}),
    ("Down", {"x": 3, "y": 12}),
    ("Left", {"x": 2, "y": 12}),
]

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (2, 12) successfully! Toggling switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])   # Opens "A secret switch!"
    time.sleep(1.0)             # Wait for text scroll
    mgba.press_buttons(["A"])   # Opens "Press it?"
    time.sleep(1.0)             # Wait for menu
    mgba.press_buttons(["A"])   # Selects YES and toggles
    time.sleep(1.0)             # Wait for toggle
    mgba.press_buttons(["B"])   # Safely dismisses text box
    time.sleep(0.5)
    print("Switch toggled!")
    
    # Take a screenshot to inspect the gate state
    img_path = mgba.take_screenshot()
    print(f"Gate state inspected: {img_path}")
else:
    print("Failed to reach the switch.")
