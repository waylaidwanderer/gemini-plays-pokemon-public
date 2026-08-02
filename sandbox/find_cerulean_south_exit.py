import mgba
import time

print("Starting Cerulean City South Exit Finder Script...")

pos = mgba.get_coordinates()
print(f"Starting position in Cerulean City: {pos}")

# Player is at (25, 27)
# Walk Left column by column along Row 27 and test stepping Down into Row 28!

found_gap = None

for test_x in range(pos['x'], -1, -1):
    curr = mgba.get_coordinates()
    # Move to test_x on Row 27
    if curr['x'] > test_x:
        mgba.press_buttons(["Left"] * (curr['x'] - test_x) + ["sleep 100"])
    
    p = mgba.get_coordinates()
    print(f"Testing Column {p['x']} at Row {p['y']}...")
    
    # Try stepping Down
    mgba.press_buttons(["Down", "sleep 300"])
    p_after = mgba.get_coordinates()
    
    if p_after['y'] > p['y']:
        print(f"FOUND SOUTH GAP AT Column {p['x']}! Moved to ({p_after['x']}, {p_after['y']})!")
        found_gap = (p['x'], p_after['y'])
        s = mgba.take_screenshot()
        print(f"South gap screenshot: {s}")
        
        # Walk Down to Route 5 exit at Row 35!
        down_seq = ["Down"] * 8 + ["sleep 1000"]
        mgba.press_buttons(down_seq)
        p_exit = mgba.get_coordinates()
        print(f"Position after walking South to exit: {p_exit}")
        s_exit = mgba.take_screenshot()
        print(f"Route 5 exit screenshot: {s_exit}")
        break

if not found_gap:
    print("No South gap found between Col 25 and Col 0 on Row 27.")
