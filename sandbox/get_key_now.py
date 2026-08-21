import mgba
import time

def clear_and_get_key():
    print("Executing final bypass and retrieval of Secret Key...")
    
    # Starting at (1, 10)
    # 1. Walk Down to (1, 13)
    for _ in range(3):
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
    print(f"At (1, 13): {mgba.get_coordinates()}")
    
    # 2. Walk Right to (5, 13)
    for _ in range(4):
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
    print(f"At (5, 13): {mgba.get_coordinates()}")
    
    # 3. Walk Up to (5, 6)
    for _ in range(7):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
    print(f"At (5, 6): {mgba.get_coordinates()}")
    
    # 4. Walk Left to (1, 6)
    for _ in range(4):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
    print(f"At (1, 6): {mgba.get_coordinates()}")
    
    # 5. Walk Up to (1, 4)
    for _ in range(2):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
    print(f"At (1, 4) Secret Key tile: {mgba.get_coordinates()}")
    
    # 6. Press A to retrieve Secret Key
    print("Retrieving Secret Key...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Clear dialogue
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    print(f"Final position: {mgba.get_coordinates()}")
    scr = mgba.take_screenshot()
    print(f"Final screenshot: {scr}")

clear_and_get_key()
