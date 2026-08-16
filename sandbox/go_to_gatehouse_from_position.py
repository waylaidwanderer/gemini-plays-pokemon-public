import mgba
import time

print("--- EXTREMELY SHORT DIRECT GATEHOUSE ENTRY ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (20, 14).
# 1. Walk UP to (20, 13).
print("Step 1: Walking UP to (20, 13)")
mgba.press_buttons(["Up", "sleep 100", "Up"])
time.sleep(1.0)
print("Position after Step 1:", get_pos())

# 2. Walk Left 2 steps to (18, 13).
print("Step 2: Walking Left to (18, 13)")
mgba.press_buttons(["Left", "sleep 100", "Left", "sleep 100", "Left"])
time.sleep(1.0)
print("Position after Step 2:", get_pos())

# 3. Walk UP Column 18 until we warp or hit a wall.
print("Step 3: Walking UP Column 18")
for step in range(12):
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
