import mgba
import time

def run():
    print("--- STEP-BY-STEP GATEHOUSE EAST EXIT ---")
    pos = mgba.get_coordinates()
    print("Start position on 2F:", pos)
    
    # 1. Step Right to (7, 8) to trigger warp down to 1F
    print("Stepping onto stairs (Right)...")
    mgba.press_buttons(["Right"])
    time.sleep(1.8) # Wait for transition to complete
    
    print("Position after warp:", mgba.get_coordinates())
    
    # 2. Walk UP 2 steps to (7, 5) (the exit doormat)
    print("Walking UP 2 steps to exit doormat...")
    mgba.press_buttons(["Up", "sleep 300", "Up"])
    time.sleep(1.0)
    print("Position on 1F exit doormat:", mgba.get_coordinates())
    
    # 3. Walk RIGHT 2 steps to transition to Route 15 overworld
    print("Walking RIGHT 2 steps to transition...")
    mgba.press_buttons(["Right", "sleep 400", "Right"])
    time.sleep(2.0) # Wait for overworld map transition
    
    print("Final position:", mgba.get_coordinates())
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
