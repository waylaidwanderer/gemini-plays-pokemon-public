import mgba
import time

def get_stable_coords():
    pos1 = mgba.get_coordinates()
    time.sleep(0.1)
    pos2 = mgba.get_coordinates()
    while pos1 != pos2:
        pos1 = pos2
        time.sleep(0.1)
        pos2 = mgba.get_coordinates()
    return pos1

# We start at (22, 34) on the overworld
pos = get_stable_coords()
print(f"Starting position: {pos}")

# 1. Walk UP column 22 to Row 22
while pos['y'] > 22:
    mgba.press_buttons(["Up"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"Reached Row 22: {pos}")

# 2. Walk Left to Column 23
while pos['x'] > 23:
    mgba.press_buttons(["Left"])
    time.sleep(0.35)
    pos = get_stable_coords()

# We will scan columns 23 down to 10 on Row 22
found_warps = []

for x in range(23, 9, -1):
    # Walk to (x, 22)
    pos = get_stable_coords()
    while pos['x'] > x:
        mgba.press_buttons(["Left"])
        time.sleep(0.35)
        pos = get_stable_coords()
    while pos['x'] < x:
        mgba.press_buttons(["Right"])
        time.sleep(0.35)
        pos = get_stable_coords()
        
    print(f"At stable ({pos['x']}, {pos['y']}), testing column {x} by pressing UP...")
    
    # Press UP
    mgba.press_buttons(["Up"])
    time.sleep(0.8) # generous time for transition/animation
    
    pos_after = get_stable_coords()
    print(f"  Coordinates after UP: {pos_after}")
    
    if pos_after['y'] == 21 and pos_after['x'] == x:
        # Pavement, no warp
        print(f"  Pavement at ({x}, 21). Stepping back Down.")
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
    elif pos_after['y'] == 22 and pos_after['x'] == x:
        # Blocked
        print(f"  Wall/Obstacle at ({x}, 21).")
    else:
        # Warp! Coordinates changed to a completely different map/location
        print(f"  !!! WARP FOUND at ({x}, 21) -> Destination: {pos_after}")
        found_warps.append((x, pos_after))
        
        # Take screenshot of the interior
        scr = mgba.take_screenshot()
        print(f"  Screenshot of interior saved at {scr}")
        
        # Exit back to overworld
        print("  Exiting back to overworld...")
        mgba.press_buttons(["Down"])
        time.sleep(1.2) # wait for warp transition
        
        pos_exit = get_stable_coords()
        print(f"  Returned to overworld at: {pos_exit}")

print("=== ROW 22 WARP SCAN COMPLETED ===")
print(f"Found warps on Row 21 (cols 10-23): {found_warps}")
