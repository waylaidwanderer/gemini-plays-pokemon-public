import mgba
import time

def main():
    print("Coordinates before press:", mgba.get_coordinates())
    # Let's press A
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    scr = mgba.take_screenshot()
    print("Screenshot after A press:", scr)
    # Let's press B to close in case it opened
    mgba.press_buttons(["B"])
    time.sleep(0.5)

if __name__ == "__main__":
    main()
