import mgba
import time

def take_step(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Current: {pos_before}. Trying to move {direction} to ({target_x}, {target_y})")
    mgba.press_buttons([direction])
    time.sleep(0.6)
    pos_after = mgba.get_coordinates()
    
    # Check if we triggered a map transition warp (like the balcony drop)
    if abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2:
        print(f"WARPED! From {pos_before} to {pos_after}")
        return True

    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        print(f"Arrived at ({target_x}, {target_y}) successfully.")
        return True
    else:
        print(f"FAILED to reach ({target_x}, {target_y}). Actual position: {pos_after}")
        return False

# Starting from current (26, 16)
steps = [
    ("Left", 25, 16),
    ("Left", 24, 16),
    ("Left", 23, 16),
    ("Left", 22, 16),
    ("Left", 21, 16),
    ("Down", 21, 17),
    ("Down", 21, 18),
    ("Left", 20, 18),
    ("Left", 19, 18) # Balcony drop warp!
]

print("Executing steps to reach the balcony drop...")
for direction, tx, ty in steps:
    pos = mgba.get_coordinates()
    # Check if we are already warped to B1F West (which would be at (9, 16) or similar)
    if pos['y'] == 16 and pos['x'] < 15:
        print("We are on B1F West! Stopped.")
        break
    success = take_step(direction, tx, ty)
    if not success:
        print("Step failed! Stopping.")
        mgba.take_screenshot()
        break
