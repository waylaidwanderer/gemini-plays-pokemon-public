import mgba
import time

print("--- EXECUTING PHASE 4: RETRIEVING GOLD TEETH ---")

# Step-by-step path from Area 3 (West) (25, 2) to Gold Teeth at (19, 25)
path = []

# (25, 2) -> (25, 18): DOWN 16 steps
path += ["Down"] * 16
# (25, 18) -> (21, 18): LEFT 4 steps
path += ["Left"] * 4
# (21, 18) -> (21, 26): DOWN 8 steps
path += ["Down"] * 8
# (21, 26) -> (19, 26): LEFT 2 steps
path += ["Left"] * 2
# Face UP
path += ["Up"]

print(f"Total steps in path: {len(path)}")

def get_pos():
    return mgba.get_coordinates()

def handle_battle():
    print("Detected battle/blockage! Attempting to escape battle...")
    # Press B a few times to clear "appeared!" text
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    
    # Press Down, Right, A to select RUN
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.0)
    
    # Press B to clear "Got away safely!" text
    mgba.press_buttons(["B"])
    time.sleep(1.5) # Wait for overworld to load

# Execute the path step-by-step
step_idx = 0
button_presses = 0

while step_idx < len(path):
    if button_presses >= 85:
        print("Approaching 100-button limit for single script execution. Stopping to save state.")
        break
        
    dir = path[step_idx]
    pos_before = get_pos()
    
    print(f"Step {step_idx+1}/{len(path)}: Pressing {dir}")
    mgba.press_buttons([dir])
    button_presses += 1
    time.sleep(0.4)
    
    pos_after = get_pos()
    
    # Check if we successfully moved
    if pos_before == pos_after:
        # We didn't move. This must be a wild battle!
        handle_battle()
        button_presses += 6
        # Let's check our position again after escaping
        pos_check = get_pos()
        print("Position after escaping battle:", pos_check)
    else:
        # Successfully moved! Advance to the next step
        step_idx += 1

# If we reached the end of the path successfully, pick up the teeth!
if step_idx == len(path):
    print("Successfully reached (19, 26) facing UP! Picking up Gold Teeth...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Press A again to clear the text "ACE picked up GOLD TEETH!"
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("Gold Teeth successfully retrieved!")

print("Final Position:", get_pos())
mgba.take_screenshot()
