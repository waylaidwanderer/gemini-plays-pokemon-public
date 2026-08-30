import mgba
import time

def take_step(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Current: {pos_before}. Trying to move {direction} to ({target_x}, {target_y})")
    mgba.press_buttons([direction])
    time.sleep(0.6)
    pos_after = mgba.get_coordinates()
    
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        print(f"Arrived at ({target_x}, {target_y}) successfully.")
        return True
    else:
        print(f"FAILED to reach ({target_x}, {target_y}). Actual position: {pos_after}")
        return False

# Starting from current (25, 10) in State B
# Walk UP Column 26 to Row 3, Left along Row 3 to Column 10, UP to Row 2, Left to Column 2, DOWN to Row 6.
steps = [
    # 1. Walk to Column 26
    ("Right", 26, 10),
    # 2. Walk UP Column 26 to Row 3
    ("Up", 26, 9),
    ("Up", 26, 8),
    ("Up", 26, 7),
    ("Up", 26, 6),
    ("Up", 26, 5),
    ("Up", 26, 4), # Pitfall is covered in State B
    ("Up", 26, 3),
    # 3. Walk Left along Row 3 to Column 10
    ("Left", 25, 3),
    ("Left", 24, 3),
    ("Left", 23, 3),
    ("Left", 22, 3),
    ("Left", 21, 3),
    ("Left", 20, 3),
    ("Left", 19, 3),
    ("Left", 18, 3),
    ("Left", 17, 3),
    ("Left", 16, 3),
    ("Left", 15, 3),
    ("Left", 14, 3),
    ("Left", 13, 3),
    ("Left", 12, 3),
    ("Left", 11, 3),
    ("Left", 10, 3),
    # 4. Walk UP Column 10 to Row 2
    ("Up", 10, 2),
    # 5. Walk Left along Row 2 to Column 2
    ("Left", 9, 2),
    ("Left", 8, 2),
    ("Left", 7, 2),
    ("Left", 6, 2),
    ("Left", 5, 2),
    ("Left", 4, 2),
    ("Left", 3, 2),
    ("Left", 2, 2),
    # 6. Walk Down Column 2 to Row 6
    ("Down", 2, 3),
    ("Down", 2, 4),
    ("Down", 2, 5),
    ("Down", 2, 6)
]

print("Executing steps to reach the Mewtwo Switch via Column 26...")
for direction, tx, ty in steps:
    success = take_step(direction, tx, ty)
    if not success:
        print("Step failed! Stopping.")
        mgba.take_screenshot()
        break
