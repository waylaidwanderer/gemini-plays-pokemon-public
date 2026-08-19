import mgba
import time

def use_dig():
    print("Opening START menu...")
    mgba.press_buttons(["Start", "sleep 500"])
    
    print("Selecting POKéMON...")
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 800"])
    
    # We are in the party screen. Let's find TRUFFLE.
    # Usually TRUFFLE is in slot 2 or we can find him.
    # Let's take a screenshot to confirm or navigate.
    # To be safe, let's walk down the party list and check names or select.
    # Let's just press Down once to go to slot 2, then select.
    # Wait, let's check our party. SHELLBY (Blastoise) is slot 1, TRUFFLE is slot 2.
    print("Selecting TRUFFLE (slot 2)...")
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 800"])
    
    # TRUFFLE's menu should have DIG as the first option or we can select it.
    # According to our notes, Option 1 is DIG.
    print("Selecting DIG...")
    mgba.press_buttons(["A", "sleep 2000"])
    
    print("Checking if DIG succeeded...")
    pos = mgba.get_coordinates()
    print("Position after DIG attempt:", pos)
    mgba.take_screenshot()

use_dig()
