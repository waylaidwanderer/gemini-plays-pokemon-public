import mgba
import time

def main():
    print("Starting debug DIG...")
    
    # Press B multiple times to ensure we are in overworld
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
    
    # 1. Open Start menu
    mgba.press_buttons(["Start", "sleep 800"])
    s1 = mgba.take_screenshot()
    print("Start menu open:", s1)
    
    # 2. Reset cursor to top by pressing UP 10 times
    mgba.press_buttons(["Up", "sleep 150"] * 10)
    s2 = mgba.take_screenshot()
    print("Cursor reset to POKEDEX:", s2)
    
    # 3. Move DOWN once to POKEMON and enter
    mgba.press_buttons(["Down", "sleep 300", "A", "sleep 1000"])
    s3 = mgba.take_screenshot()
    print("Pokemon menu open:", s3)
    
    # 4. Move DOWN 5 times to Slot 6 (TRUFFLE)
    mgba.press_buttons([
        "Down", "sleep 250",
        "Down", "sleep 250",
        "Down", "sleep 250",
        "Down", "sleep 250",
        "Down", "sleep 250"
    ])
    s4 = mgba.take_screenshot()
    print("Cursor on Slot 6:", s4)
    
    # 5. Press A to enter TRUFFLE's sub-menu
    mgba.press_buttons(["A", "sleep 1000"])
    s5 = mgba.take_screenshot()
    print("TRUFFLE submenu open:", s5)
    
    # 6. Press A to use DIG
    mgba.press_buttons(["A", "sleep 3500"])
    s6 = mgba.take_screenshot()
    print("After DIG:", s6)

if __name__ == "__main__":
    main()
