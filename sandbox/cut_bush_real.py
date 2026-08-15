import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Starting CUT sequence from GUSTY sub-menu...")
    
    # 1. Close GUSTY's options sub-menu (returns to POKÉMON menu with cursor on GUSTY / slot 3)
    # Use generous sleep to let menu close completely!
    print("Closing GUSTY sub-menu...")
    bridge.press_buttons(["B", "sleep 1000"])
    
    # 2. Press UP once to select TRUFFLE (slot 2)
    print("Moving from GUSTY to TRUFFLE...")
    bridge.press_buttons(["Up", "sleep 400"])
    
    # 3. Press A to select TRUFFLE
    print("Opening TRUFFLE menu...")
    bridge.press_buttons(["A", "sleep 1200"])
    
    # 4. Press A to select CUT (first option)
    print("Executing CUT...")
    bridge.press_buttons(["A", "sleep 3500"])
    
    # 5. Walk UP through the cut bush to (26, 12)
    print("Walking UP through the cut bush...")
    bridge.press_buttons(["Up", "sleep 600", "Up", "sleep 600"])
    
    pos = get_pos()
    print(f"Final Position after CUT and walk: {pos}")

if __name__ == "__main__":
    main()
