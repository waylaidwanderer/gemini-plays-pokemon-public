import mgba
import time

def main():
    print("Verifying Bag items carefully...")
    # Currently we are on TOWN MAP in the Bag.
    # Let's scroll up 8 times to see the middle of the Bag list
    mgba.press_buttons(["Up", "sleep 200"] * 8 + ["sleep 500"])
    
    screenshot = mgba.take_screenshot()
    print(f"Bag Middle Page Screenshot: {screenshot}")
    
    # Scroll up 5 more times to hit the absolute top
    mgba.press_buttons(["Up", "sleep 200"] * 5 + ["sleep 500"])
    
    screenshot_top = mgba.take_screenshot()
    print(f"Bag Top Page Screenshot: {screenshot_top}")

if __name__ == "__main__":
    main()
