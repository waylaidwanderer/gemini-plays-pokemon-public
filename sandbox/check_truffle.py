import mgba
import time
from PIL import Image

def main():
    print("Checking TRUFFLE's status...")
    # Press B to ensure clean state
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    
    # Open Start menu
    mgba.press_buttons(["Start", "sleep 800"])
    
    # Select POKEMON
    # We will press Down once from POKEDEX to POKEMON, and A.
    # To ensure we are on POKEDEX, let's press Up 10 times.
    mgba.press_buttons(["Up", "sleep 150"] * 10)
    mgba.press_buttons(["Down", "sleep 250", "A", "sleep 1200"])
    
    # Move to Slot 6 (TRUFFLE)
    mgba.press_buttons([
        "Down", "sleep 250",
        "Down", "sleep 250",
        "Down", "sleep 250",
        "Down", "sleep 250",
        "Down", "sleep 250",
        "A", "sleep 1000" # Select TRUFFLE
    ])
    
    # Take screenshot of TRUFFLE's submenu (should have STATS, SWITCH, CANCEL)
    s1 = mgba.take_screenshot()
    print("TRUFFLE submenu:", s1)
    
    # Move to STATS (usually the 1st option) and press A
    mgba.press_buttons(["A", "sleep 1500"])
    s2 = mgba.take_screenshot()
    print("TRUFFLE Stats Page 1:", s2)
    
    # Press A or B to exit stats
    mgba.press_buttons(["B", "sleep 500", "B", "sleep 500", "B", "sleep 500"])

if __name__ == "__main__":
    main()
