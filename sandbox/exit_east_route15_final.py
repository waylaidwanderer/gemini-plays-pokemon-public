import mgba
import time

def run():
    print("--- DYNAMIC 1F EAST ROOM EXIT VERSION 2 ---")
    pos = mgba.get_coordinates()
    print("Start position on 2F:", pos)
    
    # We are at (6, 7). Step Right to (7, 7) to trigger warp down
    print("Stepping onto stairs (Right)...")
    mgba.press_buttons(["Right"])
    time.sleep(2.0) # Wait for transition to complete
    
    land_pos = mgba.get_coordinates()
    print("Landed on 1F at:", land_pos)
    
    # Path on 1F:
    # 1. Walk Left to (6, 7)
    print("Step 1: Left to (6, 7)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # 2. Walk Down to (6, 8)
    print("Step 2: Down to (6, 8)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # 3. Walk Down to (6, 9)
    print("Step 3: Down to (6, 9)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # 4. Walk Right 3 times to transition to Route 15 overworld
    print("Step 4: Right 3 times to transition...")
    for _ in range(3):
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        
    time.sleep(1.5) # Wait for transition
    print("Final position:", mgba.get_coordinates())
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
