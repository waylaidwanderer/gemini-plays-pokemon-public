import mgba
import time

def main():
    pos = mgba.get_coordinates()
    print("Exiting 1F West on foot from:", pos)
    
    # We are at (5, 14). Walk DOWN Column 5 to entrance at (5, 27)
    print("Walking down to 1F West entrance doorway...")
    while pos["y"] < 27:
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("Current position:", pos)
        
    # Step DOWN to exit to overworld
    print("Exiting to overworld...")
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Exited to Cinnabar Island overworld:", pos)

if __name__ == "__main__":
    main()
