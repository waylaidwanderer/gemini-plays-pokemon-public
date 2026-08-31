import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print("Initial Position:", pos)
    
    if pos['x'] == 12 and pos['y'] == 11:
        print("Facing Right to look at the statue at (13, 11)...")
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        
        # Press A once to see if dialogue opens
        print("Pressing A to check for secret switch...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Take screenshot to see if a textbox opened
        scr = mgba.take_screenshot()
        print("Screenshot saved to:", scr)
        
        # Press B to close textbox if it opened
        mgba.press_buttons(["B"])
        time.sleep(0.5)

if __name__ == "__main__":
    main()
