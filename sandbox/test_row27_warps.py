import mgba
import time

def walk_to(target_x, target_y):
    pos = mgba.get_coordinates()
    while pos['x'] != target_x or pos['y'] != target_y:
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        
        button = None
        if dy > 0:
            button = "Down"
        elif dy < 0:
            button = "Up"
        elif dx > 0:
            button = "Right"
        elif dx < 0:
            button = "Left"
            
        if not button:
            break
            
        mgba.press_buttons([button])
        time.sleep(0.35)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # Blocked
            return False
        pos = new_pos
    return True

# We want to test every column from 20 to 40 on Row 28
# For each column, we try to walk UP into Row 27
# If it warps, we note it, step back out, and continue.

found_warps = []

# Move to start of search range
print("Moving to start of search range (20, 28)...")
walk_to(20, 28)

for x in range(20, 41):
    pos = mgba.get_coordinates()
    print(f"Testing column {x}...")
    
    # 1. Walk to (x, 28)
    if not walk_to(x, 28):
        print(f"Cannot reach ({x}, 28)")
        continue
        
    # 2. Try to walk UP into Row 27
    mgba.press_buttons(["Up"])
    time.sleep(0.5) # longer delay to let map transition happen if any
    
    pos_after_up = mgba.get_coordinates()
    
    # Check if we moved/warped
    if pos_after_up['y'] == 27 and pos_after_up['x'] == x:
        # We stepped into Row 27, but did NOT warp.
        print(f"Pavement at ({x}, 27). Stepping back Down.")
        mgba.press_buttons(["Down"])
        time.sleep(0.35)
    elif pos_after_up['y'] == 28 and pos_after_up['x'] == x:
        # We bumped, so it's a solid wall.
        print(f"Wall at ({x}, 27).")
    else:
        # Coordinates changed to something else (usually small values inside like 3,7 or 2,7)
        # This is a WARP!
        print(f"!!! WARP DETECTED at ({x}, 27) -> Inside position: {pos_after_up}")
        found_warps.append((x, pos_after_up))
        
        # Take a screenshot inside
        screenshot_path = mgba.take_screenshot()
        print(f"Screenshot taken inside: {screenshot_path}")
        
        # Step back out of the warp
        print("Stepping back out to overworld...")
        mgba.press_buttons(["Down"])
        time.sleep(1.0) # wait for map transition back
        
        pos_after_exit = mgba.get_coordinates()
        print(f"Returned to overworld at: {pos_after_exit}")

print("--- SEARCH RESULTS ---")
print(f"Found warps: {found_warps}")
