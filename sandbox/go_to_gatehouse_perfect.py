import mgba
import time

print("--- EXECUTING INTELLIGENT STEP-BY-STEP PATH TO SAFARI ZONE ---")

# Complete path from (25, 26) to entering Gatehouse at (18, 3)
path = []

# 1. Walk LEFT 1 step to (24, 26)
path += ["Left"]
# 2. Walk UP 12 steps to (24, 14)
path += ["Up"] * 12
# 3. Walk RIGHT 11 steps to (35, 14)
path += ["Right"] * 11
# 4. Walk UP 5 steps to (35, 9)
path += ["Up"] * 5
# 5. Walk LEFT 17 steps to (18, 9)
path += ["Left"] * 17
# 6. Walk RIGHT 19 steps to Column 37 (Row 7 bypass)
path += ["Right"] * 19
# 7. Walk UP 7 steps to Row 2
path += ["Up"] * 7
# 8. Walk LEFT 15 steps to Column 22
path += ["Left"] * 15
# 9. Walk DOWN 2 steps to Row 4
path += ["Down"] * 2
# 10. Walk LEFT 4 steps to Column 18
path += ["Left"] * 4
# 11. Enter Gatehouse (UP 2 steps)
path += ["Up"] * 2

def get_pos():
    return mgba.get_coordinates()

# Execute the path step-by-step
step_idx = 0
button_presses = 0

while step_idx < len(path):
    if button_presses >= 95:
        print("Approaching 100-button limit for single script execution. Stopping to save state.")
        break
        
    dir = path[step_idx]
    pos_before = get_pos()
    
    print(f"Step {step_idx+1}/{len(path)}: Pressing {dir}")
    mgba.press_buttons([dir])
    button_presses += 1
    time.sleep(0.4)
    
    pos_after = get_pos()
    
    # Check if we got blocked (e.g. by a moving NPC)
    if pos_before == pos_after:
        print(f"Blocked at {pos_before} when trying to go {dir}! Waiting and retrying...")
        time.sleep(1.0) # Wait for NPC to move
    else:
        # Successfully moved! Advance to the next step
        step_idx += 1

print("Navigation paused or completed. Current Position:", get_pos())
mgba.take_screenshot()
