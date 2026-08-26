import mgba
import time
from PIL import Image

def main():
    print("Checking field moves for all party Pokemon...")
    # Press B to ensure clean state
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    
    # Open Start menu
    mgba.press_buttons(["Start", "sleep 800"])
    
    # Select POKEMON
    mgba.press_buttons(["Up", "sleep 150"] * 10)
    mgba.press_buttons(["Down", "sleep 250", "A", "sleep 1200"])
    
    # Scan all 6 slots
    for slot in range(6):
        print(f"Checking Slot {slot+1}...")
        if slot > 0:
            mgba.press_buttons(["Down", "sleep 250"])
            
        # Select Pokemon
        mgba.press_buttons(["A", "sleep 800"])
        
        # Take screenshot of submenu
        s = mgba.take_screenshot()
        print(f"Slot {slot+1} submenu:", s)
        
        # Press B to close submenu
        mgba.press_buttons(["B", "sleep 500"])
        
    # Close Pokemon menu and Start menu
    mgba.press_buttons(["B", "sleep 500", "B", "sleep 500"])

if __name__ == "__main__":
    main()
