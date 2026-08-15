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
    print("Currently on GUSTY's stats screen. Performing CUT sequence...")
    
    # 1. Close stats screen (returns to POKÉMON menu with cursor on GUSTY / slot 3)
    bridge.press_buttons(["B", "sleep 600"])
    
    # 2. Press UP once to select TRUFFLE (slot 2)
    print("Moving from GUSTY to TRUFFLE...")
    bridge.press_buttons(["Up", "sleep 200"])
    
    # 3. Press A to select TRUFFLE
    bridge.press_buttons(["A", "sleep 1000"])
    
    # 4. Press A to select CUT (first option)
    print("Executing CUT...")
    bridge.press_buttons(["A", "sleep 3000"])
    
    # 5. Walk UP through the cut bush to (26, 12)
    print("Walking UP through the cut bush...")
    bridge.press_buttons(["Up", "sleep 500", "Up", "sleep 500"])
    
    pos = get_pos()
    print(f"Final Position after CUT and walk: {pos}")

if __name__ == "__main__":
    main()
