import mgba
import time

print("--- DIRECT ATTEMPT TO ENTER GATEHOUSE VIA COLUMN 18 ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (20, 16).
# 1. Walk Left to Column 18.
print("Step 1: Walking Left to Column 18")
for _ in range(2):
    pos = get_pos()
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    if get_pos() == pos:
        mgba.press_buttons(["Left"])
        time.sleep(0.4)

# 2. Walk UP Column 18 until we warp or hit a wall
print("Step 2: Walking UP Column 18")
for step in range(15):
    pos = get_pos()
    print(f"Current Position: {pos}. Pressing Up...")
    
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    new_pos = get_pos()
    if new_pos == pos:
        # Turned but didn't step, or bumped. Try once more.
        print("Position unchanged. Pressing Up again...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        new_pos = get_pos()
        
    print(f"New Position after Up: {new_pos}")
    
    # If we warped into the Gatehouse, x will be small (like 3 or 4)
    if new_pos and new_pos['x'] < 10:
        print("Successfully warped inside the Gatehouse!")
        break
        
    # If we are stuck or bumped, let's stop and print
    if new_pos == pos:
        print(f"Blocked at {pos} on Column 18!")
        break

pos_now = get_pos()
# 3. If we are inside the Gatehouse, speak to the clerk!
if pos_now and pos_now['x'] < 10:
    print("Inside Gatehouse. Walking to clerk...")
    # Walk to (3, 3) facing UP
    # We enter at (3, 5). Walk UP 2 steps to (3, 3)
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Talk to clerk
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Clear dialogue (press A 12 times)
    print("Paying and entering Safari Zone...")
    for _ in range(12):
        mgba.press_buttons(["A"])
        time.sleep(0.6)
        
    time.sleep(2.0) # wait for warp into Safari Zone Center at (15, 25)

mgba.take_screenshot()
print("Final Position:", get_pos())
