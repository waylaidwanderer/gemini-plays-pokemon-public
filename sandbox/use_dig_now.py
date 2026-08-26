import mgba
import time

def main():
    print("Exiting OPTION menu...")
    mgba.press_buttons(["B", "sleep 800"])
    
    print("Opening Start menu...")
    mgba.press_buttons(["Start", "sleep 800"])
    
    # Cursor should default to OPTION. Press Up 4 times to go to POKEMON.
    print("Moving cursor to POKEMON...")
    mgba.press_buttons([
        "Up", "sleep 250",
        "Up", "sleep 250",
        "Up", "sleep 250",
        "Up", "sleep 250",
        "A", "sleep 1200" # Enter POKEMON
    ])
    
    # Move Down 5 times to TRUFFLE
    print("Moving cursor to TRUFFLE (Slot 6)...")
    mgba.press_buttons([
        "Down", "sleep 250",
        "Down", "sleep 250",
        "Down", "sleep 250",
        "Down", "sleep 250",
        "Down", "sleep 250",
        "A", "sleep 1000" # Enter TRUFFLE submenu
    ])
    
    # Use DIG (Option 1)
    print("Using DIG...")
    mgba.press_buttons(["A", "sleep 3500"])
    
    pos = mgba.get_coordinates()
    print("DIG sequence completed. Current position:", pos)

if __name__ == "__main__":
    main()
