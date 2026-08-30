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

# Starting from current (21, 16) in State B
# Walk to 3F West switch at (2, 5) Stand at (2, 6)
steps = [
    # 1. Walk Right along Row 16 to Column 25
    ("Right", 22, 16),
    ("Right", 23, 16),
    ("Right", 24, 16),
    ("Right", 25, 16),
    # 2. Walk UP Column 25 to Row 3
    ("Up", 25, 15),
    ("Up", 25, 14),
    ("Up", 25, 13), # Open in State B
    ("Up", 25, 12),
    ("Up", 25, 11),
    ("Up", 25, 10),
    ("Up", 25, 9),
    ("Up", 25, 8),
    ("Up", 25, 7),
    ("Up", 25, 6),
    ("Up", 25, 5),
    ("Up", 25, 4),
    ("Up", 25, 3),
    # 3. Walk Left along Row 3 to Column 10
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

print("Executing steps to reach the Mewtwo Switch...")
for direction, tx, ty in steps:
    success = take_step(direction, tx, ty)
    if not success:
        print("Step failed! Stopping.")
        mgba.take_screenshot()
        break
