import mgba
import time

print("--- FINAL STEPS TO GOLD TEETH ---")

# Path from current position (21, 24) to (19, 26) facing UP
path = ["Down", "Down", "Left", "Left", "Up"]

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

# Reach end of path!
if step_idx == len(path):
    print("Successfully reached (19, 26) facing UP! Pressing A to pick up Gold Teeth...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Clear "ACE picked up GOLD TEETH!"
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("Gold Teeth successfully retrieved!")

print("Final Position:", get_pos())
mgba.take_screenshot()
