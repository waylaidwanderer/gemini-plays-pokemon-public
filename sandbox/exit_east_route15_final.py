import mgba
import time

def run():
    print("--- CORRECTED GATEHOUSE EAST EXIT ---")
    pos = mgba.get_coordinates()
    print("Start position on 2F:", pos)
    
    # We are standing on the 2F warp tile (7, 7). 
    # Walk Left to (6, 7) to walk off.
    print("Walking Left to (6, 7)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # Walk Right to (7, 7) to trigger the warp down
    print("Stepping onto stairs (Right)...")
    mgba.press_buttons(["Right"])
    time.sleep(2.0) # Wait for transition to complete
    
    land_pos = mgba.get_coordinates()
    print("Landed on 1F at:", land_pos)
    
    # From the landing at (6, 8) on 1F:
    # 1. Walk Down 1 step to (6, 9) (the corridor)
    print("Step 1: Down to (6, 9)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # 2. Walk Right 3 times to transition to Route 15 overworld
    print("Step 2: Right 3 times to transition...")
    for _ in range(3):
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        
    time.sleep(1.5) # Wait for overworld map transition
    print("Final position:", mgba.get_coordinates())
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
