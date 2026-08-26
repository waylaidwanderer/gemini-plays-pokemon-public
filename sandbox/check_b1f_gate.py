import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print("Testing B1F East Row 11 gate from:", pos)
    
    # We are at (10, 7) or (10, 4) depending on current position
    # Walk DOWN to Row 11 on Column 10
    while pos["y"] < 11:
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("After Down:", pos)
        
    while pos["y"] > 11:
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("After Up:", pos)
        
    # Try walking LEFT to Column 8 on Row 11
    print("Trying to walk LEFT through gate at (10, 11)...")
    for i in range(3):
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("After Left:", pos)

if __name__ == "__main__":
    main()
