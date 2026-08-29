import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print(f"probe_around: Start coordinates: {pos}")
    
    # We are at (1, 11)
    # Walk Up to (1, 10)
    print("Moving Up to (1, 10)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    pos = mgba.get_coordinates()
    print(f"At: {pos}")
    
    # Try Up to (1, 9)
    print("Testing UP from (1, 10)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    pos_up = mgba.get_coordinates()
    print(f"After UP: {pos_up}")
    if pos_up != pos:
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        
    # Try Right to (2, 10)
    print("Testing RIGHT from (1, 10)...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    pos_right = mgba.get_coordinates()
    print(f"After RIGHT: {pos_right}")
    if pos_right != pos:
        mgba.press_buttons(["Left"])
        time.sleep(0.4)

if __name__ == "__main__":
    main()
