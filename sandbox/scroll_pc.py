# Script to scroll down in ACE's PC and take screenshots of the items.
import time
import sys
import mgba

def scroll_and_snap():
    print("Scrolling and taking screenshots...")
    # Scroll down 6 times, taking a screenshot at each step
    for i in range(6):
        mgba.press_buttons(["Down", "sleep 300"])
        screenshot_file = mgba.take_screenshot()
        print(f"Scroll {i+1}: Took screenshot {screenshot_file}")
        time.sleep(0.5)

if __name__ == "__main__":
    scroll_and_snap()
