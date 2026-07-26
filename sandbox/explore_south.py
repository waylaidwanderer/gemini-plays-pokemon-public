import mgba
import time

def travel_to_route5():
    print("Starting travel to Route 5...")
    pos = mgba.get_coordinates()
    print(f"Initial position: {pos}")

    # 1. Walk Up 8 steps to row 18
    mgba.press_buttons(["Up"] * 8)
    time.sleep(0.5)
    print("Position after walking Up 8:", mgba.get_coordinates())

    # 2. Walk Left 3 steps to column 2
    mgba.press_buttons(["Left"] * 3)
    time.sleep(0.5)
    print("Position after walking Left 3:", mgba.get_coordinates())

    # 3. Walk Down 12 steps to row 30
    mgba.press_buttons(["Down"] * 12)
    time.sleep(0.5)
    print("Position after walking Down 12:", mgba.get_coordinates())

    # 4. Walk Right 18 steps to column 20
    mgba.press_buttons(["Right"] * 18)
    time.sleep(0.5)
    print("Position after walking Right 18:", mgba.get_coordinates())

    # 5. Walk Down 5 steps to try and enter Route 5!
    mgba.press_buttons(["Down"] * 5)
    time.sleep(0.5)
    print("Final position:", mgba.get_coordinates())

    screenshot_file = mgba.take_screenshot()
    print("Screenshot:", screenshot_file)

if __name__ == "__main__":
    travel_to_route5()
