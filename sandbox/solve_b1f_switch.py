import mgba
import time

def retrieve_secret_key_final():
    print("Executing final retrieval of Secret Key from (6, 10)...")
    
    # Starting at (6, 10) in State B
    # 1. Walk UP Column 6 to (6, 5)
    for step in range(1, 6):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
    print(f"At (6, 5): {mgba.get_coordinates()}")
    
    # 2. Walk Left to (1, 5)
    for step in range(1, 6):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
    print(f"At (1, 5): {mgba.get_coordinates()}")
    
    # 3. Face UP towards Secret Key
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print(f"Facing UP at: {mgba.get_coordinates()}")
    
    # 4. Press A to retrieve the Secret Key
    print("Retrieving Secret Key...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Clear dialogue
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    print(f"Final state: {mgba.get_coordinates()}")
    scr = mgba.take_screenshot()
    print(f"Final screenshot: {scr}")

retrieve_secret_key_final()
