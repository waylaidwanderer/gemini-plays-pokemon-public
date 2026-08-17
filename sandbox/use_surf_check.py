import mgba
import time

def use_surf_check():
    print("Opening start menu...")
    mgba.press_buttons(["Start", "sleep 300"])
    
    print("Forcing cursor to top (POKEDEX)...")
    mgba.press_buttons(["Up", "Up", "Up", "Up", "Up", "Up", "sleep 300"])
    
    print("Moving to POKEMON...")
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 600"])
    
    print("Selecting SHELLBY...")
    mgba.press_buttons(["A", "sleep 400"])
    
    print("Taking screenshot of SHELLBY submenu...")
    mgba.take_screenshot()

use_surf_check()
