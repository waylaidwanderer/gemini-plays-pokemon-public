import mgba
import time

def run():
    print("--- EXITING ROUTE 15 GATEHOUSE EAST ---")
    pos = mgba.get_coordinates()
    print("Current position on 2F:", pos)
    
    # We are at (7, 6). Step DOWN to (7, 7) to trigger the stairs warp to 1F
    print("Stepping onto stairs...")
    mgba.press_buttons(["Down"])
    time.sleep(1.2) # wait for warp transition to fully complete!
    
    print("Position after warp (should be 7, 7 on 1F):", mgba.get_coordinates())
    
    # Walk DOWN 2 steps on 1F to (7, 9) to walk off the warp tile
    print("Walking DOWN to corridor...")
    mgba.press_buttons(["Down", "sleep 300", "Down"])
    time.sleep(0.5)
    print("Position in 1F corridor:", mgba.get_coordinates())
    
    # Walk RIGHT 3 steps to exit the gatehouse
    print("Walking RIGHT to transition to Route 15 overworld...")
    for _ in range(3):
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
        
    time.sleep(1.5) # Wait for overworld map transition
    print("Final position:", mgba.get_coordinates())
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
