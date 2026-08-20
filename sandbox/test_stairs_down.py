import mgba
import time

def test_stairs():
    print("Testing stairs at (6, 12) on 3F...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # Walk Left to (6, 11)
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    print("Position after Left:", mgba.get_coordinates())
    
    # Walk Down onto (6, 12)
    mgba.press_buttons(["Down"])
    time.sleep(2.0) # wait for warp
    
    print("Position after Down:", mgba.get_coordinates())
    mgba.take_screenshot()

if __name__ == "__main__":
    test_stairs()
