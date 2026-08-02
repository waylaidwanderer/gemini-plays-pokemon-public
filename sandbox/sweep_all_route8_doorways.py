import mgba
import time

print("Starting Exhaustive Route 8 Doorway Sweep...")

# Exit current building from (2, 3)
# Walk Down 4 steps onto exit mat
mgba.press_buttons(["Down", "Down", "Down", "Down", "sleep 1000"])

pos = mgba.get_coordinates()
print(f"Position after exiting building: {pos}")

s_out = mgba.take_screenshot()
print(f"Outside screenshot: {s_out}")

# Now outside on Route 8 around (13, 16) / (13, 17)
# Let's walk West along Row 16/17 towards Col 9, Col 5, Col 0
# and test stepping Up into every building tile!

doorways_found = []

# Probe West from Col 13 to Col 0
curr_x = pos['x']
curr_y = pos['y']

# Walk Left step by step and probe Up at each column
for target_x in range(curr_x, -1, -1):
    # Walk to target_x on current row
    p = mgba.get_coordinates()
    if p['x'] > target_x:
        mgba.press_buttons(["Left"] * (p['x'] - target_x) + ["sleep 200"])
    
    p_check = mgba.get_coordinates()
    print(f"Probing column {p_check['x']} at row {p_check['y']}...")
    
    # Try stepping Up
    mgba.press_buttons(["Up", "sleep 500"])
    p_after = mgba.get_coordinates()
    
    # Check if we warped into an interior map (e.g., y changed drastically or x changed)
    if p_after['y'] < 10 and p_after['x'] < 10:
        print(f"FOUND DOORWAY at Route 8 ({p_check['x']}, {p_check['y']}) -> Interior ({p_after['x']}, {p_after['y']})!")
        s_interior = mgba.take_screenshot()
        print(f"Interior screenshot: {s_interior}")
        doorways_found.append((p_check['x'], p_check['y'], p_after['x'], p_after['y'], s_interior))
        # Exit back out
        mgba.press_buttons(["Down", "sleep 1000"])
    else:
        # If we just walked Up on overworld, step back Down
        if p_after['y'] < p_check['y']:
            mgba.press_buttons(["Down", "sleep 200"])

print("Probe completed! Doorways found:", doorways_found)
