import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print(f"probe_around: Starting from {pos}")
    
    # Try Up
    print("Testing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    pos_up = mgba.get_coordinates()
    print(f"After UP: {pos_up}")
    if pos_up != pos:
        # Move back
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        
    # Try Down
    print("Testing DOWN...")
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    pos_down = mgba.get_coordinates()
    print(f"After DOWN: {pos_down}")
    if pos_down != pos:
        # Move back
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        
    # Try Left
    print("Testing LEFT...")
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    pos_left = mgba.get_coordinates()
    print(f"After LEFT: {pos_left}")
    if pos_left != pos:
        # Move back
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        
    # Try Right
    print("Testing RIGHT...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    pos_right = mgba.get_coordinates()
    print(f"After RIGHT: {pos_right}")
    if pos_right != pos:
        # Move back
        mgba.press_buttons(["Left"])
        time.sleep(0.4)

if __name__ == "__main__":
    main()
