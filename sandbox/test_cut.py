import bridge
import time
import sys
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is not None:
        return pos[0], pos[1]
    return None

def main():
    print("=== DEBUGGING CUT SEQUENCE ===")
    pos = get_pos()
    print("Position:", pos)
    
    # 1. Open Start Menu
    print("Opening Start Menu...")
    bridge.press_buttons(["Start", "sleep 600"])
    img1 = mgba.take_screenshot()
    print("Screenshot 1 taken.")
    
    # 2. Align to POKEDEX by pressing Up 6 times
    print("Aligning to POKEDEX...")
    bridge.press_buttons(["Up", "Up", "Up", "Up", "Up", "Up", "sleep 300"])
    img2 = mgba.take_screenshot()
    print("Screenshot 2 taken.")
    
    # 3. Select POKEMON
    print("Selecting POKEMON...")
    bridge.press_buttons(["Down", "A", "sleep 1000"])
    img3 = mgba.take_screenshot()
    print("Screenshot 3 taken.")
    
    # 4. Select TRUFFLE (Paras) in slot 2
    print("Selecting Paras...")
    bridge.press_buttons(["Down", "A", "sleep 1000"])
    img4 = mgba.take_screenshot()
    print("Screenshot 4 taken.")
    
    # 5. Check options
    print("Pressing A to see if CUT option is there...")
    bridge.press_buttons(["A", "sleep 1000"])
    img5 = mgba.take_screenshot()
    print("Screenshot 5 taken.")
    
    # 6. Exit menus
    print("Exiting menus...")
    bridge.press_buttons(["B", "sleep 500", "B", "sleep 500", "B", "sleep 500"])
    
if __name__ == "__main__":
    main()
