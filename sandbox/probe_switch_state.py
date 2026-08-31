import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print("Initial position:", pos)
    
    # Walk to (3, 11)
    if pos['x'] != 3 or pos['y'] != 11:
        print("Walking to (3, 11)...")
        if pos['x'] > 3:
            mgba.press_buttons(["Left"])
        elif pos['x'] < 3:
            mgba.press_buttons(["Right"])
        time.sleep(0.5)
        
        pos = mgba.get_coordinates()
        if pos['y'] > 11:
            mgba.press_buttons(["Up"])
        elif pos['y'] < 11:
            mgba.press_buttons(["Down"])
        time.sleep(0.5)
        
    pos = mgba.get_coordinates()
    print("Position at (3, 11):", pos)
    
    # Face UP
    print("Turning UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Press A to probe switch
    print("Pressing A to probe the switch at (3, 10)...")
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
