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

# Starting at (1, 10) on 3F West in State A
# 1. Walk to switch at (2, 12)
steps_to_switch = [
    ("Down", {"x": 1, "y": 11}),
    ("Down", {"x": 1, "y": 12}),
    ("Right", {"x": 2, "y": 12}),
]

success = True
for direction, coords in steps_to_switch:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (2, 12) on 3F West successfully! Toggling switch to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])   # Opens "A secret switch! Press it?"
    time.sleep(1.0)             # Wait for text scroll
    mgba.press_buttons(["A"])   # Selects YES and toggles
    time.sleep(1.0)             # Wait for toggle
    mgba.press_buttons(["B"])   # Dismisses dialog
    time.sleep(0.5)
    print("Switch toggled! Current coordinates:", mgba.get_coordinates())
    
    # 2. Walk to (11, 6) on 3F East
    steps_to_cross = [
        ("Left", {"x": 1, "y": 12}),
        ("Up", {"x": 1, "y": 11}),
        ("Up", {"x": 1, "y": 10}),
        ("Up", {"x": 1, "y": 9}),   # OPEN in State B!
        ("Up", {"x": 1, "y": 8}),
        ("Up", {"x": 1, "y": 7}),
        ("Up", {"x": 1, "y": 6}),
        ("Right", {"x": 2, "y": 6}),
        ("Right", {"x": 3, "y": 6}),
        ("Right", {"x": 4, "y": 6}),
        ("Right", {"x": 5, "y": 6}),
        ("Right", {"x": 6, "y": 6}),
        ("Right", {"x": 7, "y": 6}),
        ("Right", {"x": 8, "y": 6}),
        ("Right", {"x": 9, "y": 6}),
        ("Right", {"x": 10, "y": 6}),
        ("Right", {"x": 11, "y": 6}), # Crosses to 3F East!
    ]
    
    for d, c in steps_to_cross:
        if not walk_step(d, c):
            success = False
            break
            
    if success:
        print("Successfully reached (11, 6) on 3F East!")
    else:
        print("Failed to navigate to 3F East.")
else:
    print("Failed to reach switch on 3F West.")
