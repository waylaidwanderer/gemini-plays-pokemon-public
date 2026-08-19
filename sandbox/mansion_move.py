import mgba
import time

def walk_to_2f_stairs():
    print("Navigating from 1F entrance at (5, 27) to 2F stairs at (7, 10)...")
    
    # 1. Walk Up to row 10 (17 steps Up)
    for i in range(17):
        pos = mgba.get_coordinates()
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        print(f"Step Up {i+1}: {pos} -> {new_pos}")
        if new_pos == pos:
            print("Hit obstacle going Up! Let's analyze.")
            break
            
    # 2. Walk Right to column 7 (from 5 to 7 is 2 steps Right)
    pos = mgba.get_coordinates()
    if pos['y'] == 10:
        for i in range(2):
            pos = mgba.get_coordinates()
            mgba.press_buttons(["Right"])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            print(f"Step Right {i+1}: {pos} -> {new_pos}")
            if new_pos == pos:
                print("Hit obstacle going Right! Let's analyze.")
                break
                
    # 3. Enter stairs at (7, 10) by walking Up or standing on it
    # Note: Stairs at (7, 10) is a warp. Let's walk Up or stand.
    pos = mgba.get_coordinates()
    if pos['x'] == 7 and pos['y'] == 10:
        print("At stairs! Stepping Up to warp...")
        mgba.press_buttons(["Up"])
        time.sleep(1.0)
        print("Position after warp:", mgba.get_coordinates())
        
    mgba.take_screenshot()

walk_to_2f_stairs()
