import mgba
import time

print("--- SELF-HEALING SAFARI ZONE NAVIGATOR (PART 3) ---")

# Step-by-step path from Area 2 (North) (39, 31) to Area 3 (West) at (26, 0)
path = []

# (39, 31) -> (22, 31): LEFT 17 steps
path += ["Left"] * 17
# (22, 31) -> (22, 22): UP 9 steps (climbing Western Southern Plateau stairs at 22, 23)
path += ["Up"] * 9
# (22, 22) -> (16, 22): LEFT 6 steps on the plateau
path += ["Left"] * 6
# (16, 22) -> (16, 28): DOWN 6 steps (descending stairs at 16, 27)
path += ["Down"] * 6
# (16, 28) -> (12, 28): LEFT 4 steps
path += ["Left"] * 4
# (12, 28) -> (12, 30): DOWN 2 steps (bypassing the pond)
path += ["Down"] * 2
# (12, 30) -> (8, 30): LEFT 4 steps
path += ["Left"] * 4
# (8, 30) -> (8, 36): DOWN 6 steps (through statue gap at 8, 34 to 8, 35, and down to transition at 8, 36)
path += ["Down"] * 6

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

print("Navigation paused or completed. Current Position:", get_pos())
mgba.take_screenshot()
