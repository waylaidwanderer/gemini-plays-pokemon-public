import mgba
import time

def run():
    print("--- EXITING ROUTE 15 GATEHOUSE EAST ---")
    pos = mgba.get_coordinates()
    print("Current position on 2F:", pos)
    
    # We are at (6, 8). Step RIGHT to (7, 8) to trigger the stairs warp to 1F
    print("Stepping onto stairs...")
    mgba.press_buttons(["Right"])
    time.sleep(1.5) # wait for warp transition to fully complete!
    
    print("Position after warp (should be 7, 7 on 1F):", mgba.get_coordinates())
    
    # Walk UP 2 steps on 1F to (7, 5) (the exit doormat)
    print("Walking UP to exit doormat...")
    mgba.press_buttons(["Up", "sleep 300", "Up"])
    time.sleep(0.5)
    print("Position on 1F exit doormat:", mgba.get_coordinates())
    
    # Walk RIGHT 2 steps to transition to Route 15 overworld
    print("Walking RIGHT to transition to Route 15 overworld...")
    mgba.press_buttons(["Right", "sleep 400", "Right"])
    time.sleep(1.5) # Wait for overworld map transition
    
    print("Final position:", mgba.get_coordinates())
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
