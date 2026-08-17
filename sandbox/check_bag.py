import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def check_bag_perfect():
    print("Opening start menu...")
    press_and_wait("Start", 0.5)
    
    print("Forcing cursor to top (POKEDEX)...")
    for _ in range(6):
        press_and_wait("Up", 0.2)
        
    print("Moving to ITEM...")
    press_and_wait("Down", 0.25)
    press_and_wait("Down", 0.25)
    press_and_wait("A", 0.8)
    
    # Take screenshot of Page 1
    p1 = mgba.take_screenshot()
    print("Bag Page 1:", p1)
    
    # Scroll down 4 times
    print("Scrolling down to Page 2...")
    for _ in range(4):
        press_and_wait("Down", 0.2)
    time.sleep(0.5)
    
    # Take screenshot of Page 2
    p2 = mgba.take_screenshot()
    print("Bag Page 2:", p2)
    
    # Scroll down 4 more times
    print("Scrolling down to Page 3...")
    for _ in range(4):
        press_and_wait("Down", 0.2)
    time.sleep(0.5)
    
    # Take screenshot of Page 3
    p3 = mgba.take_screenshot()
    print("Bag Page 3:", p3)
    
    # Exit bag and menu
    print("Exiting bag...")
    press_and_wait("B", 0.5)
    print("Exiting start menu...")
    press_and_wait("B", 0.5)
    print("Done!")

check_bag_perfect()
