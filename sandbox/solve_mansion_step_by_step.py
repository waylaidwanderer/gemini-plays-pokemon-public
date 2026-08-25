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

# Starting at (15, 7) on 2F East (State B)
# 1. Walk LEFT to (12, 7)
steps_left = [
    ("Left", {"x": 14, "y": 7}),
    ("Left", {"x": 13, "y": 7}),
    ("Left", {"x": 12, "y": 7}),
]
success = True
for d, c in steps_left:
    if not walk_step(d, c):
        success = False
        break

if success:
    # 2. Walk DOWN Column 12 to (12, 11)
    steps_down = [
        ("Down", {"x": 12, "y": 8}),
        ("Down", {"x": 12, "y": 9}),
        ("Down", {"x": 12, "y": 10}),
        ("Down", {"x": 12, "y": 11}),
    ]
    for d, c in steps_down:
        if not walk_step(d, c):
            success = False
            break

if success:
    print("Reached (12, 11)! Facing RIGHT towards the switch...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    
    # Save step 1 screenshot
    mgba.press_buttons(["sleep 200"]) # Ensure facing direction is set
    img1 = mgba.take_screenshot()
    print("Screenshot before A:", img1)
    
    # Press A
    print("Pressing A (1st time)...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    img2 = mgba.take_screenshot()
    print("Screenshot after 1st A:", img2)
    
    # Press A again (YES)
    print("Pressing A (2nd time) to select YES...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    img3 = mgba.take_screenshot()
    print("Screenshot after 2nd A:", img3)
    
    # Press A again (Dismiss)
    print("Pressing A (3rd time) to dismiss dialogue...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    img4 = mgba.take_screenshot()
    print("Screenshot after 3rd A:", img4)
    
    print("Step-by-step toggle complete! Current position:", mgba.get_coordinates())
else:
    print("Failed to reach (12, 11).")
