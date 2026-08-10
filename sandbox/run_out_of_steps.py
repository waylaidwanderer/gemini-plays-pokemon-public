import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

print("Starting run_out_of_steps.py...")

step_count = 0
while True:
    cx, cy = get_pos()
    
    # If cy changed dramatically (we got warped to the Gatehouse at y=0 or y=3/4), we stop!
    if cy < 10:
        print(f"Warped to Gatehouse! Position is ({cx}, {cy}). Stopping.")
        # Clear dialogs by pressing B a few times
        for _ in range(10):
            mgba.press_buttons(["B", "sleep 300"])
        break
        
    # Alternate walking Left and Right to consume steps
    target_dir = "Left" if step_count % 2 == 0 else "Right"
    print(f"Step {step_count}: Position ({cx}, {cy}). Walking {target_dir}...")
    mgba.press_buttons([target_dir, "sleep 300"])
    step_count += 1
    
    # Check for wild battle or "Time's up" text
    nx, ny = get_pos()
    if nx == cx and ny == cy:
        print("Stuck! Checking for battle or dialog...")
        # Press Down, Right, A to RUN from battle, and B to clear text
        mgba.press_buttons(["B", "sleep 200", "Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1200"])
        for _ in range(5):
            mgba.press_buttons(["B", "sleep 200"])
            
print("Finished run_out_of_steps.py.")
