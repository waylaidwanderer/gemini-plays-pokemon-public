import mgba
import time

def main():
    print("0. Press A twice to advance text")
    mgba.press_buttons(["A", "sleep 1200", "A", "sleep 1200"])
    
    print("1. Press Right to go to PKMN")
    mgba.press_buttons(["Right", "sleep 300"])
    
    print("2. Press A to open PKMN menu")
    mgba.press_buttons(["A", "sleep 600"])
    
    print("3. Press Down to go to SHELLBY")
    mgba.press_buttons(["Down", "sleep 300"])
    
    print("4. Press A to select SHELLBY")
    mgba.press_buttons(["A", "sleep 600"])
    
    print("5. Press A to confirm SWITCH")
    mgba.press_buttons(["A", "sleep 600"])
    print("Switch sequence completed.")

if __name__ == "__main__":
    main()
