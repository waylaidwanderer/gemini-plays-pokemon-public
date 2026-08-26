import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print("Starting escape_on_foot.py, current position:", pos)
    
    # We are at (10, 7) on B1F East.
    # Walk RIGHT to Column 12 on Row 7
    while pos["x"] < 12:
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("After Right:", pos)
        
    # Walk DOWN Column 12 to Row 11
    while pos["y"] < 11:
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("After Down:", pos)
        
    # Walk LEFT along Row 11 to B1F West
    print("Walking LEFT along Row 11 to B1F West...")
    while pos["x"] > 5:
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("After Left:", pos)

if __name__ == "__main__":
    main()
