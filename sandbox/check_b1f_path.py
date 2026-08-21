import mgba
import time

def walk_to_target():
    # Current position is (3, 11)
    print("Starting B1F Secret Key retrieval path...")
    
    # 1. Walk Right to (10, 11)
    for _ in range(7):
        mgba.press_buttons(["Right"])
        time.sleep(0.1)
    pos = mgba.get_coordinates()
    print(f"Reached coordinates: {pos}")
    
    # 2. Walk Up to (10, 5)
    for _ in range(6):
        mgba.press_buttons(["Up"])
        time.sleep(0.1)
    pos = mgba.get_coordinates()
    print(f"Reached coordinates: {pos}")
    
    # 3. Walk Left to (1, 5)
    for _ in range(9):
        mgba.press_buttons(["Left"])
        time.sleep(0.1)
    pos = mgba.get_coordinates()
    print(f"Reached coordinates: {pos}")
    
    # Take a screenshot to verify if we reached (1, 5) or got blocked
    screenshot_file = mgba.take_screenshot()
    print(f"Screenshot taken: {screenshot_file}")

walk_to_target()
