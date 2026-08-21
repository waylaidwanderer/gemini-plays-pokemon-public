import mgba
import time

def retrieve_key():
    print("Walking to Secret Key...")
    # Stand at (10, 5)
    # 1. Down to (10, 6)
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    print(f"At (10, 6): {mgba.get_coordinates()}")
    
    # 2. Left to (9, 6)
    mgba.press_buttons(["Left"]) # Turn left
    time.sleep(0.5)
    mgba.press_buttons(["Left"]) # Step left
    time.sleep(0.5)
    print(f"At (9, 6): {mgba.get_coordinates()}")
    
    # 3. Walk to (1, 6)
    for _ in range(8):
        mgba.press_buttons(["Left"])
        time.sleep(0.2)
    print(f"At (1, 6): {mgba.get_coordinates()}")
    
    # 4. Walk Up to (1, 4)
    for _ in range(2):
        mgba.press_buttons(["Up"])
        time.sleep(0.2)
    print(f"At (1, 4) Secret Key: {mgba.get_coordinates()}")
    
    # 5. Pick up key
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    print("Secret Key retrieved!")
    
    scr = mgba.take_screenshot()
    print(f"Screenshot: {scr}")

retrieve_key()
