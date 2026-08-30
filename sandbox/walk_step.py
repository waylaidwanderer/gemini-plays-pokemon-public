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

# We are at (28, 7).
# Let's walk back to Column 27 first: Left to (27, 7)
# Then walk Down to (27, 9)
# Then walk Left to (26, 9)
# Then walk Down to (26, 12)
steps = [
    ("Left", 27, 7),
    ("Down", 27, 8),
    ("Down", 27, 9),
    ("Left", 26, 9),
    ("Down", 26, 10),
    ("Down", 26, 11),
    ("Down", 26, 12),
    ("Down", 26, 13),
    ("Down", 26, 14),
    ("Down", 26, 15),
    ("Down", 26, 16),
]

print("Executing precise step-by-step path...")
for direction, tx, ty in steps:
    success = take_step(direction, tx, ty)
    if not success:
        print("Step failed! Taking screenshot and stopping to prevent runaway behavior.")
        mgba.take_screenshot()
        break
