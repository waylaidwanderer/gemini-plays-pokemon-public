import mgba
import time

def run():
    print("--- GOING DOWN ROUTE 15 STAIRS ---")
    pos = mgba.get_coordinates()
    print("Start position on 2F:", pos)
    
    # We are at (1, 5). 
    # 1. Walk Right 4 steps to (5, 5)
    print("Walking Right 4 steps...")
    for _ in range(4):
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
        
    print("Position:", mgba.get_coordinates())
    
    # 2. Walk Down 3 steps to (5, 8)
    print("Walking Down 3 steps...")
    for _ in range(3):
        mgba.press_buttons(["Down"])
        time.sleep(0.3)
        
    print("Position:", mgba.get_coordinates())
    
    # 3. Walk Right 1 step to (6, 8) (staircase)
    print("Stepping onto stairs...")
    mgba.press_buttons(["Right"])
    time.sleep(1.0) # wait for transition
    
    print("Position after transition:", mgba.get_coordinates())
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
