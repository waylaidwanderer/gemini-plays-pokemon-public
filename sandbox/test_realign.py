import time
import bridge

print("Starting vertical street search...")

# Ensure we are at row 21
coords = bridge.get_coordinates()
if coords[1] != 21:
    print("Walking DOWN to row 21...")
    bridge.press_buttons(["Down"])
    time.sleep(1.0)
    coords = bridge.get_coordinates()
print(f"Current Coords: {coords}")

# Loop left from our current column down to 0
curr_x = coords[0]
for x in range(curr_x, -1, -1):
    # Walk left to column x on row 21
    coords = bridge.get_coordinates()
    while coords[0] > x:
        bridge.press_buttons(["Left"])
        time.sleep(0.5)
        coords = bridge.get_coordinates()
    print(f"At column {x}: current coords {coords}")
    
    # Try to walk Down
    print(f"Probing Down at column {x}...")
    bridge.press_buttons(["Down"])
    time.sleep(0.5)
    coords_down = bridge.get_coordinates()
    
    if coords_down[1] > 21:
        print(f"SUCCESS! Found down path at column {x}! Coords: {coords_down}")
        # Walk further down to confirm and reach row 25
        for _ in range(4):
            bridge.press_buttons(["Down"])
            time.sleep(0.5)
        coords_down2 = bridge.get_coordinates()
        print(f"Confirmed down path coords: {coords_down2}")
        break
    else:
        print(f"Column {x} is blocked. Moving back UP to row 21 to continue left...")
        # If we didn't move past 21, we might have stayed at 21, or moved to 21 from 20? 
        # But we were already at 21, so we must still be at 21. Let's make sure we are at row 21:
        if coords_down[1] < 21:
            bridge.press_buttons(["Down"])
            time.sleep(0.5)
        elif coords_down[1] > 21:
            bridge.press_buttons(["Up"])
            time.sleep(0.5)

