import mgba
import time
import os

# Clean up obsolete files as requested by the overwatch system
obsolete_files = [
    "walk_to_statue_2f.py",
    "test_col9_up.py",
    "go_to_2f_east_switch.py",
    "mansion_2f_traverse.py"
]
for f in obsolete_files:
    if os.path.exists(f):
        try:
            os.remove(f)
            print(f"Deleted obsolete file: {f}")
        except Exception as e:
            print(f"Error deleting {f}: {e}")

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

# Starting at (6, 10) on 3F West of Pokemon Mansion in State B
steps_3f = [
    ("Down", {"x": 6, "y": 11}),
    ("Left", {"x": 5, "y": 11}),
    ("Left", {"x": 4, "y": 11}),
    ("Up", {"x": 4, "y": 10}),
    ("Up", {"x": 4, "y": 9}),  # OPEN in State B!
    ("Up", {"x": 4, "y": 8}),
    ("Up", {"x": 4, "y": 7}),
    ("Up", {"x": 4, "y": 6}),
    # Row 6 horizontal walk to (19, 6)
    ("Right", {"x": 5, "y": 6}),
    ("Right", {"x": 6, "y": 6}),
    ("Right", {"x": 7, "y": 6}),
    ("Right", {"x": 8, "y": 6}),
    ("Right", {"x": 9, "y": 6}),
    ("Right", {"x": 10, "y": 6}),
    ("Right", {"x": 11, "y": 6}),
    ("Right", {"x": 12, "y": 6}), # Crosses to 3F East
    ("Right", {"x": 13, "y": 6}),
    ("Right", {"x": 14, "y": 6}),
    ("Right", {"x": 15, "y": 6}),
    ("Right", {"x": 16, "y": 6}),
    ("Right", {"x": 17, "y": 6}),
    ("Right", {"x": 18, "y": 6}),
    ("Right", {"x": 19, "y": 6}),
    # Up Column 19 to Row 3
    ("Up", {"x": 19, "y": 5}),
    ("Up", {"x": 19, "y": 4}),
    ("Up", {"x": 19, "y": 3}),
    # Right along Row 3 to (26, 3)
    ("Right", {"x": 20, "y": 3}),
    ("Right", {"x": 21, "y": 3}),
    ("Right", {"x": 22, "y": 3}),
    ("Right", {"x": 23, "y": 3}),
    ("Right", {"x": 24, "y": 3}),
    ("Right", {"x": 25, "y": 3}),
    ("Right", {"x": 26, "y": 3}),
]

success = True
for direction, coords in steps_3f:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (26, 3) on 3F East! Stepping DOWN to trigger pitfall...")
    mgba.press_buttons(["Down"])
    time.sleep(1.0) # Wait for drop animation
    pos = mgba.get_coordinates()
    print(f"Landed on 1F East inside fenced room at: {pos}")
    
    # Walk to (21, 2) and then step Right to (22, 2)
    print("Routing to 1F East stairs (22, 2)...")
    curr = mgba.get_coordinates()
    while curr['y'] > 2:
        if not walk_step("Up", {"x": curr['x'], "y": curr['y'] - 1}):
            break
        curr = mgba.get_coordinates()
    while curr['x'] > 21:
        if not walk_step("Left", {"x": curr['x'] - 1, "y": curr['y']}):
            break
        curr = mgba.get_coordinates()
    # Step Right onto (22, 2) to warp down
    print("Stepping onto stairs at (22, 2) to warp to B1F East...")
    mgba.press_buttons(["Right"])
    time.sleep(1.0) # Wait for warp animation
    
    curr = mgba.get_coordinates()
    print(f"Warped to B1F East! Current coordinates: {curr}")
    
    # 3. Route on B1F East:
    steps_b1f = [
        ("Left", {"x": 21, "y": 3}),
        ("Down", {"x": 21, "y": 4}),
        ("Left", {"x": 20, "y": 4}),
        ("Left", {"x": 19, "y": 4}),
        ("Down", {"x": 19, "y": 5}),
    ]
    for d, c in steps_b1f:
        walk_step(d, c)
        
    # Now walk Left all the way to (1, 5) on Row 5
    curr = mgba.get_coordinates()
    print("Walking Left on B1F Row 5 to the Secret Key room...")
    while curr['x'] > 1:
        if not walk_step("Left", {"x": curr['x'] - 1, "y": 5}):
            break
        curr = mgba.get_coordinates()
        
    # Stand at (1, 5) facing UP and retrieve the Secret Key
    curr = mgba.get_coordinates()
    if curr == {"x": 1, "y": 5}:
        print("Successfully reached (1, 5)! Facing UP and picking up the Secret Key...")
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        mgba.press_buttons(["A"])
        time.sleep(1.5)
        # Clear dialog
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        img_path = mgba.take_screenshot()
        print(f"Secret Key retrieved! Screenshot: {img_path}")
    else:
        print(f"Failed to reach (1, 5) on B1F. Current position: {curr}")
else:
    print("Failed to navigate 3F.")
