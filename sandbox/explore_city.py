import mgba
import time

def explore():
    # We start at (13, 16). Let's walk to the center-right of Cerulean City:
    # 1. Down to (13, 19)
    # 2. Right to (25, 19)
    # 3. Take screenshot 1
    mgba.press_buttons(["Down", "Down", "Down"])
    time.sleep(0.5)
    mgba.press_buttons(["Right"] * 12)
    time.sleep(1.0)
    print("At center-right:", mgba.get_coordinates())
    img1 = mgba.take_screenshot()
    
    # 4. Walk Down to the Poke Mart area (25, 25)
    # 5. Take screenshot 2
    mgba.press_buttons(["Down"] * 6)
    time.sleep(1.0)
    print("At Mart area:", mgba.get_coordinates())
    img2 = mgba.take_screenshot()

    # 6. Walk Left to the Bike Shop area (13, 25)
    # 7. Take screenshot 3
    mgba.press_buttons(["Left"] * 12)
    time.sleep(1.0)
    print("At Bike Shop area:", mgba.get_coordinates())
    img3 = mgba.take_screenshot()

explore()
