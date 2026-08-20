import mgba
import time

def select_pokemon():
    print("Selecting POKeMON menu...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    # Take screenshot of the party list to see the order
    mgba.take_screenshot()

if __name__ == "__main__":
    select_pokemon()
