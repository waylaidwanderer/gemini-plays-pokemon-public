import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print("Initial Position on 2F West:", pos)
    
    print("Stepping Left to (6, 10)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    
    print("Stepping Left to (5, 10)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    
    pos2 = mgba.get_coordinates()
    print("Position at (5, 10):", pos2)
    
    print("Pressing Up on (5, 10) to trigger warp...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5)
    
    pos3 = mgba.get_coordinates()
    print("Position after Up on (5, 10):", pos3)
    
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
