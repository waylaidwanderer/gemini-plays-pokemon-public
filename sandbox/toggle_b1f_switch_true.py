import mgba
import time

def toggle_switch_from_front():
    print("Walking from (10, 4) to (2, 12) to toggle switch...")
    
    # 1. Walk Down to (10, 11)
    for _ in range(7):
        mgba.press_buttons(["Down"])
        time.sleep(0.05)
    print(f"Reached (10, 11): {mgba.get_coordinates()}")
    
    # 2. Walk Left to (3, 11)
    for _ in range(7):
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
    print(f"Reached (3, 11): {mgba.get_coordinates()}")
    
    # 3. Walk Down to (3, 12)
    mgba.press_buttons(["Down"])
    time.sleep(0.05)
    
    # 4. Walk Left to (2, 12)
    mgba.press_buttons(["Left"])
    time.sleep(0.05)
    print(f"At (2, 12): {mgba.get_coordinates()}")
    
    # 5. Face UP (first Up press turns)
    mgba.press_buttons(["Up"])
    time.sleep(0.1)
    
    # Take screenshot before pressing A
    mgba.take_screenshot()
    
    # Press A to open prompt
    print("Pressing A (1) to open switch prompt...")
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    scr1 = mgba.take_screenshot()
    print(f"Screenshot 1 (A pressed): {scr1}")
    
    # Press A to select YES
    print("Pressing A (2) to select YES...")
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    scr2 = mgba.take_screenshot()
    print(f"Screenshot 2 (YES selected): {scr2}")
    
    # Press B to close dialogue
    print("Pressing B to close dialogue...")
    mgba.press_buttons(["B"])
    time.sleep(0.8)
    scr3 = mgba.take_screenshot()
    print(f"Screenshot 3 (dialogue closed): {scr3}")

toggle_switch_from_front()
