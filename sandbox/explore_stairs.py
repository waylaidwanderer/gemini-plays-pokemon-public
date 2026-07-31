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

# Currently at B1F (23, 3)
print("Start Position B1F:", mgba.get_coordinates())

# 1. Walk onto (23, 2) stairs to warp DOWN to B2F (27, 8)
mgba.press_buttons(["Up"])
time.sleep(3.0)
wait_for_movement()
print("Warped DOWN to B2F:", mgba.get_coordinates())

# 2. On B2F, walk DOWN onto (27, 8) stairs to warp DOWN to B3F (27, 8)
mgba.press_buttons(["Down"])
time.sleep(3.0)
wait_for_movement()
print("Warped DOWN to B3F:", mgba.get_coordinates())

# 3. We are at B3F (27, 8). Let's walk to (24, 15) to explore!
# Path to (24, 15) from (27, 8):
# Down to (27, 14)
# Left 3 to (24, 14)
# Down to (24, 15)
mgba.press_buttons(["Down", "Down", "Down", "Down", "Down", "Down"])
wait_for_movement()
mgba.press_buttons(["Left", "Left", "Left"])
wait_for_movement()
mgba.press_buttons(["Down"])
wait_for_movement()
print("At (24, 15):", mgba.get_coordinates())

# 4. Explore Columns 25-28, Rows 11-13
# We will walk to Column 25, 26, 27, 28 and try walking UP at each!
walkable_up = []

for col in range(25, 29):
    # Walk to (col, 14)
    # Walk Up to Row 14 first
    curr = mgba.get_coordinates()
    while curr['y'] > 14:
        mgba.press_buttons(["Up"])
        curr = wait_for_movement()
    # Walk to column col
    while curr['x'] < col:
        mgba.press_buttons(["Right"])
        curr = wait_for_movement()
    while curr['x'] > col:
        mgba.press_buttons(["Left"])
        curr = wait_for_movement()
        
    print(f"Testing Column {col} at {curr}...")
    
    # Try walking UP
    mgba.press_buttons(["Up"])
    p_up = wait_for_movement()
    
    if p_up['y'] < 14:
        print(f"-> Walkable UP at column {col}! Landed at: {p_up}")
        walkable_up.append(col)
        # Walk back Down to Row 14
        mgba.press_buttons(["Down"])
        wait_for_movement()
    else:
        print("-> Blocked.")

print("Walkable UP columns:", walkable_up)

# Take screenshot to verify B3F layout
screenshot_path = mgba.take_screenshot()
print("Screenshot on B3F:", screenshot_path)
