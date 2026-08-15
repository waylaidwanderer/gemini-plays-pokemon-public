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
    print("Clearing Oak warning and using CUT from the current POKÉMON menu...")
    
    # 1. Clear Oak text box (remains on POKÉMON menu, cursor on TRUFFLE)
    bridge.press_buttons(["B", "sleep 1000"])
    
    # 2. Press A to select TRUFFLE (slot 2)
    print("Selecting TRUFFLE...")
    bridge.press_buttons(["A", "sleep 1200"])
    
    # 3. Move DOWN once from DIG to CUT
    print("Moving cursor from DIG to CUT...")
    bridge.press_buttons(["Down", "sleep 300"])
    
    # 4. Press A to execute CUT
    print("Executing CUT...")
    bridge.press_buttons(["A", "sleep 4000"])
    
    # 5. Walk UP 2 steps through the cut bush to (26, 12)
    print("Walking UP through the cut bush...")
    bridge.press_buttons(["Up", "sleep 600", "Up", "sleep 600"])
    
    pos = get_pos()
    print(f"Final Position after CUT: {pos}")

if __name__ == "__main__":
    main()
