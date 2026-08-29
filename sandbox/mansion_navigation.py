import mgba
import time

def move_with_verification(action, expected_x, expected_y):
    current_pos = mgba.get_coordinates()
    mgba.press_buttons([action])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    
    if expected_x is None or expected_y is None:
        print(f"Action {action} executed (warp expected). New position: {new_pos}")
        return True
        
    if new_pos['x'] == expected_x and new_pos['y'] == expected_y:
        print(f"Successfully moved to ({expected_x}, {expected_y})")
        return True
    else:
        print(f"FAILED to move to ({expected_x}, {expected_y}). Actual position: {new_pos}")
        return False

# Current position is (1, 10) on 2F West.
# We want to walk:
# 1. Down to (1, 11)
# 2. Down to (1, 12)
# 3. Right to (2, 12)
# 4. Right to (3, 12)
# 5. Right to (4, 12)
# 6. Right to (5, 12)
# 7. Up to (5, 11)
# 8. Right to (6, 11)
# 9. Right to (7, 11)
# 10. Up to (7, 10) (warp UP to 3F West!)

def run_route():
    steps = [
        ("Down", 1, 11),
        ("Down", 1, 12),
        ("Right", 2, 12),
        ("Right", 3, 12),
        ("Right", 4, 12),
        ("Right", 5, 12),
        ("Up", 5, 11),
        ("Right", 6, 11),
        ("Right", 7, 11),
        ("Up", None, None) # Warps to 3F West!
    ]
    
    for action, ex, ey in steps:
        if not move_with_verification(action, ex, ey):
            break

run_route()
