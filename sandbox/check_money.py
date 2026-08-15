import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("Opening START menu to check trainer card...")
    # Open START menu
    bridge.press_buttons(["Start", "sleep 500"])
    
    # We are on the first menu item (usually POKeDEX or POKeMON).
    # The menu layout is:
    # POKéDEX
    # POKéMON
    # ITEM
    # ACE (Trainer name)
    # SAVE
    # OPTION
    # EXIT
    # Let's move down to ACE. Since we usually don't have POKéDEX active? No, we got the POKéDEX on Turn 128!
    # So the menu is:
    # POKéDEX (1)
    # POKéMON (2)
    # ITEM (3)
    # ACE (4)
    # Save (5)
    # Option (6)
    # Exit (7)
    # So we press Down 3 times to reach ACE, then press A.
    bridge.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "A", "sleep 1500"])
    
    # Capture screenshot of trainer card
    mgba.take_screenshot()
    print("Trainer card screenshot captured.")
    
    # Close trainer card
    bridge.press_buttons(["B", "sleep 500", "Start", "sleep 500"])

if __name__ == "__main__":
    main()
