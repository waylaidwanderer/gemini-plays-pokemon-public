import mgba
import time

def clear_battle_and_toggle():
    print("Clearing battle text and heading to switch...")
    # Press A to clear "Got away safely!"
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"Overworld coordinate: {pos}")
    
    # We should be at (10, 7) in the overworld now.
    # 1. Walk Down to (10, 11)
    # (10, 7) to (10, 11) is 4 steps Down.
    for _ in range(4):
        mgba.press_buttons(["Down"])
        time.sleep(0.05)
    pos = mgba.get_coordinates()
    print(f"Reached coordinates: {pos}")
    
    # 2. Walk Left to (3, 11)
    for _ in range(7):
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
    pos = mgba.get_coordinates()
    print(f"Reached coordinates: {pos}")
    
    # 3. Toggle Switch
    # Press A to open prompt
    print("Interacting with switch...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    
    # Press A to select YES
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    
    # Press B (or A) to close the text box
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    print("Switch successfully toggled and closed!")
    
    # 4. Walk Right to (10, 11)
    for _ in range(7):
        mgba.press_buttons(["Right"])
        time.sleep(0.05)
    pos = mgba.get_coordinates()
    print(f"Reached coordinates: {pos}")
    
    # 5. Walk Up to (10, 5)
    for _ in range(6):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
    pos = mgba.get_coordinates()
    print(f"Reached coordinates: {pos}")
    
    # 6. Try to walk Left to (9, 5)
    mgba.press_buttons(["Left"])
    time.sleep(0.05)
    pos = mgba.get_coordinates()
    print(f"Coordinates after trying to walk Left: {pos}")
    
    screenshot_file = mgba.take_screenshot()
    print(f"Screenshot taken: {screenshot_file}")

clear_battle_and_toggle()
