import mgba
import time

def explore_3f_northeast():
    print("Navigating from (12, 11) to northeast of 3F at (17, 7)...")
    # Current position: (12, 11) on 3F.
    
    # 1. Walk Up to row 7 (4 steps Up)
    for i in range(4):
        pos = mgba.get_coordinates()
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        print(f"Step Up {i+1}: {pos} -> {new_pos}")
        if new_pos == pos:
            print("Hit obstacle going Up!")
            break
            
    # 2. Walk Right to column 17 (5 steps Right)
    pos = mgba.get_coordinates()
    if pos['y'] == 7:
        for i in range(5):
            pos = mgba.get_coordinates()
            mgba.press_buttons(["Right"])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            print(f"Step Right {i+1}: {pos} -> {new_pos}")
            if new_pos == pos:
                print("Hit obstacle going Right!")
                break
                
    mgba.take_screenshot()
    print("New Position:", mgba.get_coordinates())

explore_3f_northeast()
