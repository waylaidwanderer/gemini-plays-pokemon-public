import mgba
import time

def move_with_verification(action, expected_x, expected_y):
    current_pos = mgba.get_coordinates()
    mgba.press_buttons([action])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    
    # If we warped, new_pos might change map/coordinates entirely
    if expected_x is None or expected_y is None:
        print(f"Action {action} executed (warp expected). New position: {new_pos}")
        return True
        
    if new_pos['x'] == expected_x and new_pos['y'] == expected_y:
        print(f"Successfully moved to ({expected_x}, {expected_y})")
        return True
    else:
        print(f"FAILED to move to ({expected_x}, {expected_y}). Actual position: {new_pos}")
        return False

# Current position is (2, 12) on 2F West.
# We want to walk:
# 1. Left to (1, 12)
# 2. Up to (1, 11)
# 3. Up to (1, 10)
# 4. Up to (1, 9) (the open gate!)
# 5. Right to (2, 9)
# 6. Right to (3, 9)
# 7. Right to (4, 9)
# 8. Right to (5, 9)
# 9. Right to (6, 9)
# 10. Right to (7, 9)
# 11. Down to (7, 10) (warp to 3F West!)

def run_route():
    steps = [
        ("Left", 1, 12),
        ("Up", 1, 11),
        ("Up", 1, 10),
        ("Up", 1, 9),
        ("Right", 2, 9),
        ("Right", 3, 9),
        ("Right", 4, 9),
        ("Right", 5, 9),
        ("Right", 6, 9),
        ("Right", 7, 9),
        ("Down", None, None) # Warps to 3F West!
    ]
    
    for action, ex, ey in steps:
        if not move_with_verification(action, ex, ey):
            break

run_route()
