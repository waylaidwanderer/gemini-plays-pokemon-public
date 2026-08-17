import mgba
import time

def run():
    print("--- SEARCHING NORTHWEST FUCHSIA ---")
    pos = mgba.get_coordinates()
    print("Start position:", pos)
    
    # We are at (1, 32). Let's walk UP to row 0.
    # At each step, we will probe Left. If x changes, we found a path!
    # From 32 to 0 is 32 steps.
    for i in range(32):
        # Move Up
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        curr = mgba.get_coordinates()
        print(f"Row {curr['y']}: {curr}")
        
        # Try to step Left
        mgba.press_buttons(["Left"])
        time.sleep(0.3)
        left_pos = mgba.get_coordinates()
        if left_pos['x'] < curr['x']:
            print(f"-> FOUND GATE OR EXIT AT ROW {curr['y']}! x changed to {left_pos['x']}")
            # Step back Right
            mgba.press_buttons(["Right"])
            time.sleep(0.3)
            
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
