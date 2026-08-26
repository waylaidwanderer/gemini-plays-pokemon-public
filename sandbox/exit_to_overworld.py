import mgba
import time

def main():
    print("Escaping from battle first...")
    # We are in battle. The cursor is on FIGHT. Select RUN (Down, Right, A)
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1500"])
    
    # Dismiss any "Got away safely!" text
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 200"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Current position after escape:", pos)
    
    # We are at (5, 14) on 1F West. Walk DOWN Column 5 to entrance at (5, 27)
    print("Walking down to 1F West entrance doorway...")
    while pos["y"] < 27:
        # Check if we get into a battle during the walk
        # (the loop handles menus/battles in handle_any_menu_or_battle, but we keep it simple here)
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
