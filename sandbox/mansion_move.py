import mgba
import time

def move_to_mansion():
    print("Navigating to Pokémon Mansion entrance at (6, 3)...")
    
    # Path: Right to column 17, Up to row 3, Left to column 6.
    # We are currently at (11, 12).
    
    # 1. Walk Right to column 17 (6 steps Right)
    for i in range(6):
        pos = mgba.get_coordinates()
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        print(f"Step Right {i+1}: {pos} -> {new_pos}")
        if new_pos == pos:
            print("Hit obstacle going Right! Let's analyze.")
            break
            
    # 2. Walk Up to row 3 (9 steps Up)
    pos = mgba.get_coordinates()
    if pos['x'] >= 17:
        for i in range(9):
            pos = mgba.get_coordinates()
            mgba.press_buttons(["Up"])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            print(f"Step Up {i+1}: {pos} -> {new_pos}")
            if new_pos == pos:
                print("Hit obstacle going Up! Let's analyze.")
                break
                
    # 3. Walk Left to column 6 (from x to 6)
    pos = mgba.get_coordinates()
    if pos['y'] == 3:
        while pos['x'] > 6:
            mgba.press_buttons(["Left"])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            print(f"Step Left: {pos} -> {new_pos}")
            if new_pos == pos:
                print("Hit obstacle going Left! Let's analyze.")
                break
            pos = new_pos
            
    # 4. Walk Up to enter Mansion at (6, 3) -> transition!
    pos = mgba.get_coordinates()
    if pos['x'] == 6 and pos['y'] == 3:
        print("At Mansion entrance! Entering...")
        mgba.press_buttons(["Up"])
        time.sleep(1.0)
        print("Position after entering:", mgba.get_coordinates())
        
    mgba.take_screenshot()

move_to_mansion()
