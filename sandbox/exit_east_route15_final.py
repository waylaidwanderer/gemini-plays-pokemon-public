import mgba
import time

def run():
    print("--- CORRECT GATEHOUSE EAST EXIT SCRIPT ---")
    pos = mgba.get_coordinates()
    print("Current position on 2F:", pos)
    
    # 1. Walk to the stairs at (6, 8) on the 2F
    # Currently at (7, 4)
    print("Walking to column 5...")
    mgba.press_buttons(["Left", "sleep 300", "Left"])
    time.sleep(0.5)
    
    print("Walking Down to Row 8...")
    for _ in range(4):
        mgba.press_buttons(["Down"])
        time.sleep(0.3)
        
    print("Stepping onto stairs (Right)...")
    mgba.press_buttons(["Right"])
    time.sleep(1.8) # Wait for transition to complete
    
    print("Position after warp (should be 7, 7 on 1F):", mgba.get_coordinates())
    
    # 2. Walk off the warp tile to the Left
    print("Walking Left to (6, 7)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # 3. Walk Down 2 steps to Row 9
    print("Walking Down 2 steps to Row 9...")
    mgba.press_buttons(["Down", "sleep 300", "Down"])
    time.sleep(0.5)
    print("Position:", mgba.get_coordinates())
    
    # 4. Walk Right 3 steps to exit to Route 15 overworld
    print("Walking Right to transition...")
    mgba.press_buttons(["Right", "sleep 400", "Right", "sleep 400", "Right"])
    time.sleep(2.0) # Wait for overworld map transition
    
    print("Final position:", mgba.get_coordinates())
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
