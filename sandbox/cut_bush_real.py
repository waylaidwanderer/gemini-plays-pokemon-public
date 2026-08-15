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
    print("Closing Trainer Card and using CUT...")
    
    # 1. Close Trainer Card (returns to START menu with cursor on ACE)
    bridge.press_buttons(["B", "sleep 600"])
    
    # 2. From ACE (4), move UP 2 times to POKÉMON (2)
    print("Moving from ACE to POKÉMON...")
    bridge.press_buttons(["Up", "sleep 200", "Up", "sleep 200"])
    
    # 3. Open POKÉMON menu
    bridge.press_buttons(["A", "sleep 1200"])
    
    # 4. Move from SHELLBY (slot 1) to TRUFFLE (slot 2) and select
    print("Selecting TRUFFLE...")
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 1000"])
    
    # 5. Select CUT (first option)
    print("Executing CUT...")
    bridge.press_buttons(["A", "sleep 3000"])
    
    # 6. Walk UP through the cut bush to (26, 12)
    print("Walking UP through the cut bush...")
    bridge.press_buttons(["Up", "sleep 500", "Up", "sleep 500"])
    
    pos = get_pos()
    print(f"Final Position after CUT and walk: {pos}")

if __name__ == "__main__":
    main()
