import mgba
import time

print("--- DIRECT ESCAPE TO GATEHOUSE FROM (25, 8) ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (25, 8) facing UP.
# 1. Walk Down 1 step to (25, 9).
print("Step 1: Walking Down to (25, 9)")
mgba.press_buttons(["Down", "sleep 100", "Down"])
time.sleep(1.0)
print("Position after Step 1:", get_pos())

# 2. Walk Left 7 steps to Column 18 on Row 9: (18, 9).
print("Step 2: Walking Left to (18, 9)")
mgba.press_buttons(["Left"])
time.sleep(0.4)
for _ in range(6):
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
print("Position after Step 2:", get_pos())

# 3. Walk UP Column 18 until we warp or hit a wall.
print("Step 3: Walking UP Column 18 to enter Gatehouse")
for step in range(10):
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
        
    if new_pos == pos:
        print(f"Blocked at {pos} on Column 18!")
        break

pos_now = get_pos()
# 4. Speak to the clerk and enter the Safari Zone
if pos_now and pos_now['x'] < 10:
    print("Inside Gatehouse. Walking to clerk...")
    # Walk to (3, 3) facing UP. We enter at (3, 5).
    mgba.press_buttons(["Up", "sleep 100", "Up"])
    time.sleep(1.0)
    
    # Talk to clerk
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Clear dialogue
    print("Paying and entering Safari Zone...")
    for _ in range(12):
        mgba.press_buttons(["A"])
        time.sleep(0.6)
        
    time.sleep(2.0) # wait for warp

mgba.take_screenshot()
print("Final Position inside Safari:", get_pos())
