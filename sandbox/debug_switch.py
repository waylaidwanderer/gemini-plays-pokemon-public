import mgba
import time

def find_b1f_switch_interaction():
    print("Finding the exact interaction tile and direction for B1F switch...")
    
    # 1. Walk from (10, 6) down to (10, 11)
    for _ in range(5):
        mgba.press_buttons(["Down"])
        time.sleep(0.05)
    print(f"Reached bypass landing: {mgba.get_coordinates()}")
    
    # Let's try (2, 12) facing Up first.
    # Walk to (2, 12):
    # From (10, 11): Down to (10, 12), Left to (2, 12)
    mgba.press_buttons(["Down"])
    time.sleep(0.05)
    for _ in range(8):
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
    print(f"At (2, 12) position: {mgba.get_coordinates()}")
    
    # Face Up (first Up press turns in place)
    mgba.press_buttons(["Up"])
    time.sleep(0.1)
    
    # Take screenshot before pressing A
    mgba.take_screenshot()
    
    # Press A to test interaction
    print("Pressing A at (2, 12) facing Up...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    scr1 = mgba.take_screenshot()
    print(f"Screenshot at (2, 12) facing Up: {scr1}")
    
    # Clear dialogue if it opened
    # We will press B to see if we can close it
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # Now let's try (1, 11) facing Right.
    # Walk from (2, 12) to (1, 11):
    # Up to (2, 11)? No, (2, 11) is the statue!
    # So we must go: Left to (1, 12), Up to (1, 11)
    mgba.press_buttons(["Left"])
    time.sleep(0.05)
    mgba.press_buttons(["Up"])
    time.sleep(0.05)
    print(f"At (1, 11) position: {mgba.get_coordinates()}")
    
    # Face Right (first Right press turns in place)
    mgba.press_buttons(["Right"])
    time.sleep(0.1)
    
    # Press A to test interaction
    print("Pressing A at (1, 11) facing Right...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    scr2 = mgba.take_screenshot()
    print(f"Screenshot at (1, 11) facing Right: {scr2}")
    
    # Press B to clear
    mgba.press_buttons(["B"])
    time.sleep(0.5)

find_b1f_switch_interaction()
