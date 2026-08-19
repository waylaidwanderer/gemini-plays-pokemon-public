import mgba
import time

def enter_mansion_final():
    print("Navigating to Pokémon Mansion from (15, 6)...")
    # Path: Up to (15, 4), Left to (6, 4), Up to (6, 3) to enter.
    
    # 1. Walk Up to row 4 (2 steps Up)
    for i in range(2):
        pos = mgba.get_coordinates()
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        print(f"Step Up {i+1}: {pos} -> {new_pos}")
        if new_pos == pos:
            print("Hit obstacle going Up! Let's analyze.")
            break
            
    # 2. Walk Left to column 6 (9 steps Left)
    pos = mgba.get_coordinates()
    if pos['y'] == 4:
        for i in range(9):
            pos = mgba.get_coordinates()
            mgba.press_buttons(["Left"])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            print(f"Step Left {i+1}: {pos} -> {new_pos}")
            if new_pos == pos:
                print("Hit obstacle going Left! Let's analyze.")
                break
                
    # 3. Walk Up to enter Mansion at (6, 3)
    pos = mgba.get_coordinates()
    if pos['x'] == 6 and pos['y'] == 4:
        print("At Mansion entrance! Entering...")
        mgba.press_buttons(["Up"])
        time.sleep(1.0)
        print("Position after entering:", mgba.get_coordinates())
        
    mgba.take_screenshot()

enter_mansion_final()
