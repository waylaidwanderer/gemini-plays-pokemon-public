import time
import bridge

print("Running go_safari.py (robust pathfinding around Safari Center barriers)...")

# Current position: (18, 18) facing DOWN
# Step 1: Walk LEFT to find a column where we can go DOWN
print("Probing left to find a down-ward path...")
coords = bridge.get_coordinates()
curr_x = coords[0]

found_path = False
for x in range(curr_x - 1, -1, -1):
    # Walk left to column x on row 18
    coords = bridge.get_coordinates()
    while coords[0] > x:
        bridge.press_buttons(["Left"])
        time.sleep(0.5)
        coords = bridge.get_coordinates()
    print(f"At column {x}: coords {coords}")
    
    # Try to walk DOWN to row 23
    print(f"Probing DOWN at column {x}...")
    # Press Down 5 times to see if we can reach row 23
    for _ in range(5):
        bridge.press_buttons(["Down"])
        time.sleep(0.5)
    
    coords_down = bridge.get_coordinates()
    if coords_down[1] >= 22:
        print(f"SUCCESS! Found down path at column {x}! Coords: {coords_down}")
        found_path = True
        break
    else:
        print(f"Column {x} is blocked. Returning UP to row 18 to continue left...")
        # Walk back UP to row 18
        coords = bridge.get_coordinates()
        while coords[1] < 18:
            bridge.press_buttons(["Up"])
            time.sleep(0.5)
            coords = bridge.get_coordinates()

if found_path:
    # We are at row 22 or 23 on some column x.
    # Now walk DOWN to row 23 if we are not there yet
    coords = bridge.get_coordinates()
    while coords[1] < 23:
        bridge.press_buttons(["Down"])
        time.sleep(0.5)
        coords = bridge.get_coordinates()
    print(f"At Row 23: {coords}")
    
    # Now walk RIGHT all the way to column 29/30 to transition to Area 1 East
    print("Walking RIGHT to transition to Area 1 East...")
    for _ in range(30): # Walk plenty of steps to ensure transition
        bridge.press_buttons(["Right"])
        time.sleep(0.5)
        
    coords_final = bridge.get_coordinates()
    print(f"Transitioned successfully! Coords inside Area 1 (East): {coords_final}")
else:
    print("ERROR: Could not find any down path on the left!")

