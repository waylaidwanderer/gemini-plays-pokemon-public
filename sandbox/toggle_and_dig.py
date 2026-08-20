import mgba
import time

def check_party():
    print("Backing out of stats screen to party menu...")
    # Press B to close stats screen
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    # Take screenshot of party menu to see the order of Pokemon!
    mgba.take_screenshot()

if __name__ == "__main__":
    check_party()
