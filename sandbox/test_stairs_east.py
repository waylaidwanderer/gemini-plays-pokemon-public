import mgba
import time

def test_east_walls():
    print("Testing walking directions from (18, 7)...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Start pos:", pos)
    
    # Try Left
    print("Trying Left...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    print("Pos after Left:", mgba.get_coordinates())
    
    # Try Right
    print("Trying Right...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    print("Pos after Right:", mgba.get_coordinates())
    
    # Try Down
    print("Trying Down...")
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    print("Pos after Down:", mgba.get_coordinates())
    
    mgba.take_screenshot()

if __name__ == "__main__":
    test_east_walls()
