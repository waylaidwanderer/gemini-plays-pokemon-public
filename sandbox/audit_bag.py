import mgba
import time

def main():
    print("Auditing entire bag items...")
    # First, let's press B to make sure we are not in any sub-menu
    mgba.press_buttons(["B", "sleep 300"])
    
    # Scroll up to the very top of the bag (press Up 15 times)
    mgba.press_buttons(["Up"] * 15 + ["sleep 500"])
    
    # Take screenshot of page 1
    p1 = mgba.take_screenshot()
    print(f"Bag Page 1: {p1}")
    
    # Scroll down 4 times to page 2
    mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 500"])
    p2 = mgba.take_screenshot()
    print(f"Bag Page 2: {p2}")
    
    # Scroll down 4 times to page 3
    mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 500"])
    p3 = mgba.take_screenshot()
    print(f"Bag Page 3: {p3}")
    
    # Scroll down 4 times to page 4
    mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 500"])
    p4 = mgba.take_screenshot()
    print(f"Bag Page 4: {p4}")

if __name__ == "__main__":
    main()
