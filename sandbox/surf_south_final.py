import mgba
import time

def run_from_battle():
    print("Coordinates did not change. Waiting for transition...")
    time.sleep(1.5)
    # Press B to clear text
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    # Press Right, Down, A to run
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A"])
    time.sleep(1.2) # Wait for escape animation or text
    # Press B again to clear "Got away safely!"
    mgba.press_buttons(["B"])
    time.sleep(0.5)

def surf_south(steps=18):
    consecutive_failures = 0
    for i in range(steps):
        pos_before = mgba.get_coordinates()
        print(f"Step {i+1}: Current Position = {pos_before}")
        
        # Press Down to move south
        mgba.press_buttons(["Down"])
        time.sleep(0.4) # Wait for animation
        
        pos_after = mgba.get_coordinates()
        if pos_after == pos_before:
            consecutive_failures += 1
            print(f"Failed to move from {pos_before}. Consecutive failures: {consecutive_failures}")
            if consecutive_failures >= 3:
                print("Stuck or blocked for 3 steps. Exiting to let player inspect.")
                break
            # Try to handle battle
            run_from_battle()
        else:
            consecutive_failures = 0
            print(f"Moved successfully to {pos_after}")

surf_south(18)
