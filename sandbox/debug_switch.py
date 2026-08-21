import mgba
import time

def debug_switch():
    print("Debugging B1F switch interaction...")
    
    # 1. Walk from (10, 4) down to (10, 11)
    for _ in range(7):
        mgba.press_buttons(["Down"])
        time.sleep(0.05)
    print(f"Reached coordinates: {mgba.get_coordinates()}")
    
    # 2. Walk Left to (3, 11)
    for _ in range(7):
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
    print(f"At switch position: {mgba.get_coordinates()}")
    
    # Take a screenshot before pressing A
    scr0 = mgba.take_screenshot()
    print(f"Screenshot before pressing A: {scr0}")
    
    # Press A to open prompt
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    scr1 = mgba.take_screenshot()
    print(f"Screenshot 1 (A pressed): {scr1}")
    
    # Press A to confirm
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    scr2 = mgba.take_screenshot()
    print(f"Screenshot 2 (second A pressed): {scr2}")
    
    # Press B to close dialog
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    scr3 = mgba.take_screenshot()
    print(f"Screenshot 3 (dialogue closed): {scr3}")

debug_switch()
