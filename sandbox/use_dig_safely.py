import mgba
import time

def main():
    print("Selecting POKEMON and using DIG...")
    # Currently, cursor is on OPTION.
    # Press Up 4 times to reach POKEMON
    mgba.press_buttons([
        "Up", "sleep 350",
        "Up", "sleep 350",
        "Up", "sleep 350",
        "Up", "sleep 350",
        "A", "sleep 1200" # Enter POKEMON
    ])
    
    # Move to Slot 6 (TRUFFLE)
    mgba.press_buttons([
        "Down", "sleep 250",
        "Down", "sleep 250",
        "Down", "sleep 250",
        "Down", "sleep 250",
        "Down", "sleep 250",
        "A", "sleep 1000" # Select TRUFFLE
    ])
    
    # Select DIG (Option 1)
    mgba.press_buttons([
        "A", "sleep 3500" # Use DIG
    ])
    
    pos = mgba.get_coordinates()
    print("DIG executed. Current position:", pos)

if __name__ == "__main__":
    main()
