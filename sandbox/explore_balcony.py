import mgba
import time

def main():
    print("Currently at:", mgba.get_coordinates())
    
    # 1. Step Down to (20, 16)
    print("Moving Down to (20, 16)")
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    print("Pos:", mgba.get_coordinates())
    
    # 2. Try Left to (19, 16)
    print("Trying Left to (19, 16)")
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    print("Pos:", mgba.get_coordinates())
    
    # 3. Try Down to (19, 17)
    print("Trying Down to (19, 17)")
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    print("Pos:", mgba.get_coordinates())
    
    # 4. Try Left to (18, 17)
    print("Trying Left to (18, 17)")
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    print("Pos:", mgba.get_coordinates())
    
    # Let's take a screenshot to inspect our position
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
