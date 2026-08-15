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
    print("Clearing Oak warning and using CUT properly on TRUFFLE...")
    
    # 1. Clear Oak text box (returns to overworld at (26, 14))
    bridge.press_buttons(["B", "sleep 1000"])
    
    # 2. Open START menu (cursor is guaranteed to be on POKÉMON / slot 2)
    bridge.press_buttons(["Start", "sleep 1000"])
    
    # 3. Press A to open POKÉMON menu (cursor is on TRUFFLE / slot 2)
    bridge.press_buttons(["A", "sleep 1200"])
    
    # 4. Press A to select TRUFFLE (slot 2)
    bridge.press_buttons(["A", "sleep 1000"])
    
    # 5. Move DOWN once from DIG to CUT
    print("Moving cursor from DIG to CUT...")
    bridge.press_buttons(["Down", "sleep 300"])
    
    # 6. Press A to execute CUT
    print("Executing CUT...")
    bridge.press_buttons(["A", "sleep 3500"])
    
    # 7. Walk UP 2 steps through the cut bush to (26, 12)
    print("Walking UP through the cut bush...")
    bridge.press_buttons(["Up", "sleep 600", "Up", "sleep 600"])
    
    pos = get_pos()
    print(f"Final Position after CUT: {pos}")

if __name__ == "__main__":
    main()
