import mgba
import time

def main():
    print("Currently at:", mgba.get_coordinates())
    
    # Walk Down to Row 12
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("At Row 12:", pos)
    
    # Walk Right up to column 20, printing positions
    print("Walking Right along Row 12...")
    for _ in range(14):
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        print("Pos:", mgba.get_coordinates())
        
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
