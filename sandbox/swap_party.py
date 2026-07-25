import mgba
import time

def swap():
    print("Opening menu...")
    mgba.press_buttons(["Start"])
    time.sleep(0.5)
    
    print("Selecting POKéMON...")
    mgba.press_buttons(["Down", "A"])
    time.sleep(0.5)
    
    print("Selecting first Pokémon (SHELLBY)...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    
    print("Selecting SWITCH option...")
    mgba.press_buttons(["Down", "A"])
    time.sleep(0.5)
    
    print("Selecting second Pokémon (TESLA) to swap...")
    mgba.press_buttons(["Down", "A"])
    time.sleep(0.5)
    
    print("Closing menus...")
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    print("Done!")

swap()
