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

# Starting at (5, 8) on 3F West (State B)
# 1. Warp DOWN to 2F West
success = walk_step("Down", {"x": 5, "y": 9})
if success:
    success = walk_step("Down", {"x": 5, "y": 10})
if success:
    print("Stepping UP to warp DOWN to 2F West...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print(f"Warped DOWN to 2F West! Landing position: {pos}")
    
    # 2. Walk RIGHT along Row 11 (open in State B!) directly to 2F East
    # From (5, 11) walk right to (16, 11)
    steps_right = []
    for x in range(6, 17):
        steps_right.append(("Right", {"x": x, "y": 11}))
    for d, c in steps_right:
        if not walk_step(d, c):
            success = False
            break
            
    if success:
        print("Reached (16, 11)! Testing if stairs at (15, 11) are open in State B...")
        # Try to walk LEFT onto stairs at (15, 11)
        if walk_step("Left", {"x": 15, "y": 11}):
            print("SUCCESS! Stairs at (15, 11) are OPEN in State B!")
            # Warp UP to 3F East!
            time.sleep(1.5)
            pos = mgba.get_coordinates()
            print(f"Warped UP to 3F East! Current position: {pos}")
        else:
            print("FAILED! Stairs at (15, 11) are CLOSED in State B.")
else:
    print("Failed to warp down.")
