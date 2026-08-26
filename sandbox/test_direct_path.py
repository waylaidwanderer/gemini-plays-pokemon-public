import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print("Testing direct path from:", pos)
    
    # Walk Left from (12, 12) to (6, 12)
    for i in range(6):
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("After Left:", pos)
        
    # Walk UP from Column 6 to Row 3
    for i in range(9):
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("After Up:", pos)

if __name__ == "__main__":
    main()
