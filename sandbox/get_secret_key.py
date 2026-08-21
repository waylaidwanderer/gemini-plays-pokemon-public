import mgba
import time

def walk_to_key_and_retrieve():
    print("Executing final B1F route to retrieve the Secret Key...")
    
    # Current position is (2, 12) facing UP
    # 1. Walk Right to (3, 12)
    mgba.press_buttons(["Right"])
    time.sleep(0.05)
    
    # 2. Walk Up to (3, 11)
    mgba.press_buttons(["Up"])
    time.sleep(0.05)
    print(f"Reached Row 11: {mgba.get_coordinates()}")
    
    # 3. Walk Right along Row 11 to (10, 11)
    for _ in range(7):
        mgba.press_buttons(["Right"])
        time.sleep(0.05)
    print(f"Reached Column 10 bypass: {mgba.get_coordinates()}")
    
    # 4. Walk Up to (10, 6)
    for _ in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
    print(f"Reached Row 6 entry: {mgba.get_coordinates()}")
    
    # 5. Walk Left through (9, 6) (open gate!) to (1, 6)
    mgba.press_buttons(["Left"]) # Turn left
    time.sleep(0.1)
    for _ in range(9):
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
    print(f"Reached West side Column 1: {mgba.get_coordinates()}")
    
    # 6. Walk Up to (1, 4)
    for _ in range(2):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
    print(f"Arrived at Secret Key tile: {mgba.get_coordinates()}")
    
    # 7. Press A to retrieve Secret Key
    print("Retrieving Secret Key...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Clear dialogue
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    print(f"Key retrieved! Current position: {mgba.get_coordinates()}")
    scr = mgba.take_screenshot()
    print(f"Final master screenshot: {scr}")

walk_to_key_and_retrieve()
