import mgba
import time

def enter_mansion_from_east():
    print("Walking Left along row 4 to column 6...")
    # We are currently at (19, 4).
    # Walk Left 13 steps.
    for i in range(13):
        pos = mgba.get_coordinates()
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        print(f"Step Left {i+1}: {pos} -> {new_pos}")
        if new_pos == pos:
            print("Hit obstacle going Left! Let's analyze.")
            break
            
    # Now we should be at (6, 4). Walk Up to enter the Mansion.
    pos = mgba.get_coordinates()
    if pos['x'] == 6 and pos['y'] == 4:
        print("At Mansion entrance! Entering...")
        mgba.press_buttons(["Up"])
        time.sleep(1.0)
        print("Position after entering:", mgba.get_coordinates())
        
    mgba.take_screenshot()

enter_mansion_from_east()
