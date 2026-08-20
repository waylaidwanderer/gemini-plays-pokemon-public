import mgba
import time

def walk_to_3f():
    print("Testing warp from 2F to 3F via stairs...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Initial pos on 2F:", pos)
    
    # Walk Down to (7, 11)
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    print("Step Down:", mgba.get_coordinates())
    
    # Walk Up back onto stairs at (7, 10)
    mgba.press_buttons(["Up"])
    time.sleep(2.0) # Wait for warp
    
    final_pos = mgba.get_coordinates()
    print("Position after warp attempt:", final_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    walk_to_3f()
