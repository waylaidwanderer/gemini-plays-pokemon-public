import mgba
import time

# We are currently at (31, 28) in Celadon City.
# Let's walk Left and test columns 30 down to 22 on Row 28.
# For each column, we try to go UP into Row 27.
# We will use robust delays and double-read coordinates to be 100% sure.

def get_stable_coords():
    # Read coordinates twice with a tiny delay to ensure stability
    pos1 = mgba.get_coordinates()
    time.sleep(0.1)
    pos2 = mgba.get_coordinates()
    while pos1 != pos2:
        pos1 = pos2
        time.sleep(0.1)
        pos2 = mgba.get_coordinates()
    return pos1

pos = get_stable_coords()
print(f"Starting scan from stable position: {pos}")

found_warps = []

for x in range(30, 21, -1):
    # Walk to (x, 28)
    pos = get_stable_coords()
    while pos['x'] > x:
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        pos = get_stable_coords()
    while pos['x'] < x:
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        pos = get_stable_coords()
        
    print(f"At stable ({pos['x']}, {pos['y']}), testing column {x} by pressing UP...")
    
    # Press UP
    mgba.press_buttons(["Up"])
    time.sleep(0.8) # generous time for transition/animation
    
    pos_after = get_stable_coords()
    print(f"  Coordinates after UP: {pos_after}")
    
    if pos_after['y'] == 27 and pos_after['x'] == x:
        # Pavement, no warp
        print(f"  Pavement at ({x}, 27). Stepping back Down.")
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
    elif pos_after['y'] == 28 and pos_after['x'] == x:
        # Blocked (wall/obstacle)
        print(f"  Wall/Obstacle at ({x}, 27).")
    else:
        # Warp! Coordinates changed to a completely different map/location
        print(f"  !!! WARP FOUND at ({x}, 27) -> Destination: {pos_after}")
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

print("=== OVERWORLD SCAN COMPLETED ===")
print(f"Found warps on Row 27 (cols 22-30): {found_warps}")
