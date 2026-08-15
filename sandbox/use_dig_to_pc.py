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
    print("Exiting OPTIONS menu and using DIG...")
    
    # 1. Close OPTIONS menu (returns us to START menu with cursor on OPTION)
    bridge.press_buttons(["B", "sleep 600"])
    
    # 2. From OPTION (6), move UP 4 times to POKÉMON (2)
    print("Moving from OPTION to POKÉMON...")
    for _ in range(4):
        bridge.press_buttons(["Up", "sleep 200"])
        
    # 3. Open POKÉMON menu
    bridge.press_buttons(["A", "sleep 1200"])
    
    # 4. Move from SHELLBY (slot 1) to TRUFFLE (slot 2)
    print("Selecting TRUFFLE...")
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 1000"])
    
    # 5. Use DIG (first option in TRUFFLE menu)
    print("Using DIG...")
    bridge.press_buttons(["A", "sleep 4000"])
    
    pos = get_pos()
    print(f"Position after DIG attempt: {pos}")
    
    if pos is not None and pos[0] == 19 and pos[1] == 28:
        print("DIG successful! Emerged in Fuchsia City outside PC.")
    else:
        print("DIG failed or position is different.")

if __name__ == "__main__":
    main()
