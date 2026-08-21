import mgba
import time

def toggle_to_state_a():
    print("Walking to B1F switch and toggling to State A...")
    
    # Starting at (9, 11)
    # 1. Down to (9, 13)
    for _ in range(2):
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
    print(f"At (9, 13): {mgba.get_coordinates()}")
    
    # 2. Left to (1, 13)
    for _ in range(8):
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
    
    # 5. Toggle switch to State A
    print("Pressing A to toggle switch...")
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
    
    print(f"Position after toggle: {mgba.get_coordinates()}")
    scr2 = mgba.take_screenshot()
    print(f"Screenshot after toggle: {scr2}")

toggle_to_state_a()
