import time
import mgba

print("Running go_east.py...")

# Start coordinates
start_coords = mgba.get_coordinates()
print(f"Start coordinates: {start_coords}")

x, y = start_coords['x'], start_coords['y']

# Walk East along Row 22. Max 15 steps.
for step in range(15):
    print(f"Step {step+1}: walking Right...")
    mgba.press_buttons(["Right"])
    time.sleep(0.6)
    
    new_coords = mgba.get_coordinates()
    print(f"Current coordinates: {new_coords}")
    
    # Check if we transitioned to a different map or changed coordinates
    if new_coords['x'] != x or new_coords['y'] != y:
        # We moved!
        # Check if we transitioned to Area 1 (East). 
        # Typically Area 1 (East) starts at x=0, and since we came from Center (which is on the left), 
        # if x becomes 0 or 1, we definitely transitioned!
        if new_coords['x'] < x and new_coords['x'] <= 1:
            print("MAP TRANSITION DETECTED!")
            break
        x, y = new_coords['x'], new_coords['y']
    else:
        print("We did not move. Might be a wall, or a battle has started.")
        mgba.take_screenshot()
        break

print("Finished go_east.py.")
