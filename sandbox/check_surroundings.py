import mgba
import time

def check_moves():
    initial_pos = mgba.get_coordinates()
    print("Initial Position:", initial_pos)
    
    # Try Left
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    pos_l = mgba.get_coordinates()
    print("After Left:", pos_l)
    if pos_l != initial_pos:
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        
    # Try Right
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    pos_r = mgba.get_coordinates()
    print("After Right:", pos_r)
    if pos_r != initial_pos:
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        
    # Try Up
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    pos_u = mgba.get_coordinates()
    print("After Up:", pos_u)
    if pos_u != initial_pos:
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
        
    # Try Down
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    pos_d = mgba.get_coordinates()
    print("After Down:", pos_d)
    if pos_d != initial_pos:
        # If we fell or moved, let's print it!
        pass

check_moves()
