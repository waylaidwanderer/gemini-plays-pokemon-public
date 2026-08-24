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

# 1. Walk from (26, 4) on 1F East to stairs at (22, 2)
steps_1f = [
    ("Up", {"x": 26, "y": 3}),
    ("Left", {"x": 25, "y": 3}),
    ("Left", {"x": 24, "y": 3}),
    ("Left", {"x": 23, "y": 3}),
    ("Left", {"x": 22, "y": 3}),
]

success = True
for direction, coords in steps_1f:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (22, 3) on 1F East! Stepping UP onto stairs to warp DOWN to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5) # Wait for warp animation
    pos = mgba.get_coordinates()
    print(f"Coordinates after warp (should be (22, 3) on B1F East): {pos}")
    
    # 2. Walk on B1F East around the Row 5 Column 20-21 wall
    steps_b1f = [
        ("Left", {"x": 21, "y": 3}),
        ("Down", {"x": 21, "y": 4}),
        ("Left", {"x": 20, "y": 4}),
        ("Left", {"x": 19, "y": 4}),
        ("Down", {"x": 19, "y": 5}),
    ]
    
    for d, c in steps_b1f:
        if not walk_step(d, c):
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
else:
    print("Failed to navigate 1F East.")
