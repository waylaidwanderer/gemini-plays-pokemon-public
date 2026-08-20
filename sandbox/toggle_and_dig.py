import mgba
import time

def exit_and_show():
    print("Exiting stats screen...")
    # Press B to close stats screen
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    # Press B again just in case we are in another submenu
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print("Coordinates:", pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    exit_and_show()
