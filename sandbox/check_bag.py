import mgba
import time

def check_bag():
    print("Opening START menu...")
    mgba.press_buttons(["Start"])
    time.sleep(0.5)
    
    # Take screenshot of start menu
    scr = mgba.take_screenshot()
    print("Start menu screenshot saved to:", scr)
    
    # We are on the start menu. Let's move down to ITEM.
    # Usually, ITEM is 2nd option. Let's press Down once and check.
    mgba.press_buttons(["Down"])
    time.sleep(0.2)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # We are in the bag now. Take screenshot of Page 1.
    scr = mgba.take_screenshot()
    print("Bag Page 1 screenshot saved to:", scr)
    
    # Scroll down 7 times to see page 2
    for _ in range(7):
        mgba.press_buttons(["Down"])
        time.sleep(0.2)
        
    scr = mgba.take_screenshot()
    print("Bag Page 2 screenshot saved to:", scr)
    
    # Scroll down another 7 times to see page 3
    for _ in range(7):
        mgba.press_buttons(["Down"])
        time.sleep(0.2)
        
    scr = mgba.take_screenshot()
    print("Bag Page 3 screenshot saved to:", scr)
    
    # Close bag and menu
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300", "B"])
    print("Finished checking bag.")

if __name__ == "__main__":
    check_bag()
