import mgba
import time

def test():
    print("Testing walking UP onto stairs at (7, 10) from (7, 11)...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Start pos:", pos)
    
    # 1. Move to (7, 11)
    # Current is (5, 11)
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    print("Moved Right:", mgba.get_coordinates())
    
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    print("Moved Right:", mgba.get_coordinates())
    
    # 2. Walk UP onto stairs at (7, 10)
    mgba.press_buttons(["Up"])
    time.sleep(1.5) # Wait extra time in case of warp
    
    print("Position after walking UP:", mgba.get_coordinates())
    mgba.take_screenshot()

if __name__ == "__main__":
    test()
