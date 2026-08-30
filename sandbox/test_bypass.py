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

# From (26, 12):
# Walk Left to Column 25: (25, 12)
# Walk Down Column 25: (25, 13) -> (25, 14) -> (25, 15) -> (25, 16)
# Walk Right to Column 26: (26, 16)
steps = [
    ("Left", 25, 12),
    ("Down", 25, 13),
    ("Down", 25, 14),
    ("Down", 25, 15),
    ("Down", 25, 16),
    ("Right", 26, 16),
]

print("Executing Column 25 bypass of the Row 13 gate...")
for direction, tx, ty in steps:
    success = take_step(direction, tx, ty)
    if not success:
        print("Bypass failed! Stopping.")
        mgba.take_screenshot()
        break
