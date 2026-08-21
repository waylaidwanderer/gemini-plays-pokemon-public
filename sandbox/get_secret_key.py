import mgba
import time

def clear_battle_and_get_key():
    print("Starting master route from current battle screen...")
    
    # Press A to clear "Got away safely!"
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"Overworld coordinate: {pos}")
    
    # We should be at (9, 11) or close. Let's walk to (10, 11)
    if pos['x'] != 10:
        steps = 10 - pos['x']
        if steps > 0:
            for _ in range(steps):
                mgba.press_buttons(["Right"])
                time.sleep(0.05)
        elif steps < 0:
            for _ in range(-steps):
                mgba.press_buttons(["Left"])
                time.sleep(0.05)
    
    pos = mgba.get_coordinates()
    print(f"Arrived at bypass column: {pos}")
    
    # Walk Up to (10, 6)
    # y = 11 to y = 6 is 5 steps Up.
    for _ in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
    pos = mgba.get_coordinates()
    print(f"At Row 6 entry: {pos}")
    
    # Walk Left to (1, 6) through the open Row 6 Column 9 gate
    # x = 10 to x = 1 is 9 steps Left.
    for _ in range(9):
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
    pos = mgba.get_coordinates()
    print(f"Bypassed Column 9 to West side: {pos}")
    
    # Walk Up to (1, 4)
    # y = 6 to y = 4 is 2 steps Up.
    for _ in range(2):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
    pos = mgba.get_coordinates()
    print(f"Arrived at Secret Key tile: {pos}")
    
    # Press A to pick up the Secret Key
    print("Interacting with Secret Key...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Dismiss any text box
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # Verify our final position and take a screenshot
    final_pos = mgba.get_coordinates()
    print(f"Final coordinates: {final_pos}")
    scr = mgba.take_screenshot()
    print(f"Screenshot taken: {scr}")

clear_battle_and_get_key()
