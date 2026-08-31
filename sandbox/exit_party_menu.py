import mgba
import time

def main():
    print("Pressing B to exit POKéMON Party menu...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    print("Pressing B again...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)
    print("Current position:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
