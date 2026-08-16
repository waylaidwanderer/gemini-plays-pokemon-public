import mgba
import time

print("--- SELF-HEALING SAFARI ZONE NAVIGATOR ---")

# Step-by-step path from (25, 24) to Area 2 (North) transition at (0, 5)
path = []

# (25, 24) -> (20, 24): LEFT 5 steps
path += ["Left"] * 5
# (20, 24) -> (20, 20): UP 4 steps (climb stairs)
path += ["Up"] * 4
# (20, 20) -> (12, 20): LEFT 8 steps
path += ["Left"] * 8
# (12, 20) -> (12, 22): DOWN 2 steps (descend stairs)
path += ["Down"] * 2
# (12, 22) -> (8, 22): LEFT 4 steps
path += ["Left"] * 4
# (8, 22) -> (8, 8): UP 14 steps
path += ["Up"] * 14
# (8, 8) -> (12, 8): RIGHT 4 steps
path += ["Right"] * 4
# (12, 8) -> (12, 6): UP 2 steps (climb stairs)
path += ["Up"] * 2
# (12, 6) -> (17, 6): RIGHT 5 steps
path += ["Right"] * 5
# (17, 6) -> (17, 8): DOWN 2 steps (descend stairs)
path += ["Down"] * 2
# (17, 8) -> (20, 8): RIGHT 3 steps
path += ["Right"] * 3
# (20, 8) -> (20, 3): UP 5 steps
path += ["Up"] * 5
# (20, 3) -> (7, 3): LEFT 13 steps
path += ["Left"] * 13
# (7, 3) -> (7, 5): DOWN 2 steps
path += ["Down"] * 2
# (7, 5) -> (0, 5): LEFT 7 steps
path += ["Left"] * 7

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
        # Do not advance step_idx so we retry the same step in the overworld!
    else:
        # Successfully moved! Advance to the next step
        step_idx += 1

print("Navigation paused or completed. Current Position:", get_pos())
mgba.take_screenshot()
