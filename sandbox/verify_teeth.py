import mgba
import time

def main():
    print("Verifying Bag items step-by-step...")
    # Currently we are on MOON STONE x 2 (Page 1)
    # Scroll down 4 times to Page 2
    mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 500"])
    p2 = mgba.take_screenshot()
    print(f"Bag Page 2: {p2}")
    
    # Scroll down 4 times to Page 3
    mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 500"])
    p3 = mgba.take_screenshot()
    print(f"Bag Page 3: {p3}")
    
    # Scroll down 4 times to Page 4
    mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 500"])
    p4 = mgba.take_screenshot()
    print(f"Bag Page 4: {p4}")

if __name__ == "__main__":
    main()
