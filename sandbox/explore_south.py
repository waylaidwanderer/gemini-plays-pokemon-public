import mgba
import time

def travel_to_route5_row18():
    print("Starting travel to Route 5 via row 18...")
    
    # 1. Walk Up 9 steps from (9, 27) to (9, 18)
    mgba.press_buttons(["Up"] * 9)
    time.sleep(0.5)
    print("Position after walking Up 9:", mgba.get_coordinates())

    # 2. Walk Left 7 steps to column 2
    mgba.press_buttons(["Left"] * 7)
    time.sleep(0.5)
    print("Position after walking Left 7:", mgba.get_coordinates())

    # 3. Walk Down 12 steps to row 30
    mgba.press_buttons(["Down"] * 12)
    time.sleep(0.5)
    print("Position after walking Down 12:", mgba.get_coordinates())

    # 4. Walk Right 18 steps to column 20
    mgba.press_buttons(["Right"] * 18)
    time.sleep(0.5)
    print("Position after walking Right 18:", mgba.get_coordinates())

    # 5. Walk Down 5 steps to enter Route 5
    mgba.press_buttons(["Down"] * 5)
    time.sleep(0.5)
    print("Final position:", mgba.get_coordinates())

    screenshot_file = mgba.take_screenshot()
    print("Screenshot:", screenshot_file)

if __name__ == "__main__":
    travel_to_route5_row18()
