import mgba
import time

def toggle_b1f():
    print("Toggling B1F switch to State B...")
    # Currently at (5, 11)
    
    # 1. Down to (5, 13)
    for _ in range(2):
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
    print(f"At (5, 13): {mgba.get_coordinates()}")
    
    # 2. Left to (1, 13)
    for _ in range(4):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
    print(f"At (1, 13): {mgba.get_coordinates()}")
    
    # 3. Up to (1, 11)
    for _ in range(2):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
    print(f"At (1, 11): {mgba.get_coordinates()}")
    
    # 4. Face Right
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    print("Facing Right towards the Mewtwo statue switch...")
    
    # 5. Press A to toggle
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Take screenshot of dialogue
    scr1 = mgba.take_screenshot()
    print(f"Dialogue screenshot: {scr1}")
    
    # Clear dialogue
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    print(f"After toggle: {mgba.get_coordinates()}")
    scr2 = mgba.take_screenshot()
    print(f"After toggle screenshot: {scr2}")

toggle_b1f()
