import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.12)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.12)
        p2 = mgba.get_coordinates()
    return p1

# We start at (28, 15)
print("Start Position:", mgba.get_coordinates())

# Let's test walking Down into Row 16 from columns 28 down to 19 on Row 15.
# We are currently at (28, 15).
pos = mgba.get_coordinates()

# Let's walk Left along Row 15 and test "Down" at each column!
gaps_found = []

for col in range(28, 18, -1):
    # Ensure we are at (col, 15)
    curr = mgba.get_coordinates()
    while curr['x'] > col:
        mgba.press_buttons(["Left"])
        curr = wait_for_movement()
    while curr['x'] < col:
        mgba.press_buttons(["Right"])
        curr = wait_for_movement()
        
    print(f"Testing Column {col} at {curr}...")
    
    # Try moving Down to Row 16
    mgba.press_buttons(["Down"])
    p_down = wait_for_movement()
    
    if p_down['y'] > 15:
        print(f"-> FOUND GAP AT COLUMN {col}! Landed at {p_down}")
        gaps_found.append(col)
        # Walk back Up to Row 15
        mgba.press_buttons(["Up"])
        wait_for_movement()
    else:
        print("-> Blocked.")

print("Gaps found on Row 16 at columns:", gaps_found)

# Let's take a screenshot
screenshot_path = mgba.take_screenshot()
print("Final Screenshot:", screenshot_path)
