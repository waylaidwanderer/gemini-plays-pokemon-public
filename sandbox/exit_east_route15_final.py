import mgba
import time

def run():
    print("--- STEP-BY-STEP GATEHOUSE EAST EXIT ---")
    pos = mgba.get_coordinates()
    print("Start position on 2F:", pos)
    
    # We are at (6, 8) on 2F.
    # 1. Step Right to (7, 8) to trigger warp down
    print("Stepping onto stairs (Right)...")
    mgba.press_buttons(["Right"])
    time.sleep(3.0) # BIG DELAY to ensure transition is 100% complete!
    
    land_pos = mgba.get_coordinates()
    print("Landed on 1F at:", land_pos)
    
    # 2. Walk DOWN to (6, 9) on 1F (the corridor)
    print("Step 1: Down to (6, 9)...")
    mgba.press_buttons(["Down"])
    time.sleep(1.0) # Wait for move to finish
    print("Position:", mgba.get_coordinates())
    
    # 3. Walk Right 3 times to transition to Route 15 overworld
    print("Step 2: Right 3 times to transition...")
    for i in range(3):
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        print(f"Right {i+1} position:", mgba.get_coordinates())
        
    time.sleep(2.0) # Wait for overworld map transition
    print("Final position:", mgba.get_coordinates())
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
