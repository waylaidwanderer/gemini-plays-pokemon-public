import mgba
import time

def main():
    pos1 = mgba.get_coordinates()
    print("Initial Position on 1F West:", pos1)
    
    print("Stepping Up to (7, 10) on 1F West...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5) # Wait for warp
    
    pos2 = mgba.get_coordinates()
    print("Position after Up:", pos2)
    
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
