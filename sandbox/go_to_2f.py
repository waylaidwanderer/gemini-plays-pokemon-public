import mgba
import time

def warp_via_7_10():
    print("Testing warp via stairs at (7, 10) on 3F...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Initial position:", pos)
    
    # 1. Walk Right to (7, 11)
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    curr = mgba.get_coordinates()
    print("Position after Right:", curr)
    
    if curr['x'] != 7 or curr['y'] != 11:
        print("Failed to reach (7, 11)!")
        mgba.take_screenshot()
        return False
        
    # 2. Press Up to turn UP (since we are facing RIGHT)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print("Position after turning Up:", mgba.get_coordinates())
    
    # 3. Press Up to step onto (7, 10) stairs
    mgba.press_buttons(["Up"])
    time.sleep(2.5) # Wait for warp
    
    final_pos = mgba.get_coordinates()
    print("Position after warp attempt:", final_pos)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    warp_via_7_10()
