import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print("Exiting B1F West on foot from:", pos)
    
    # We are at (5, 11). Walk UP to (5, 10) to warp to 1F West
    mgba.press_buttons(["Up"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Landed on 1F West at:", pos)
    
    # Walk DOWN Column 5 to the entrance doorway at (5, 27)
    print("Walking down to 1F West entrance doorway...")
    while pos["y"] < 27:
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("Current position:", pos)
        
    # Step DOWN to exit to Cinnabar overworld
    print("Exiting to overworld...")
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Exited to Cinnabar Island overworld:", pos)

if __name__ == "__main__":
    main()
