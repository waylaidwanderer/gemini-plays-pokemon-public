import mgba
import time

def use_surf():
    print("Opening start menu...")
    mgba.press_buttons(["Start", "sleep 300"])
    
    print("Forcing cursor to top (POKEDEX)...")
    mgba.press_buttons(["Up", "Up", "Up", "Up", "Up", "Up", "sleep 300"])
    
    print("Moving to POKEMON...")
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 600"])
    
    print("Selecting SHELLBY...")
    mgba.press_buttons(["A", "sleep 400"])
    
    print("Selecting SURF (Option 1)...")
    mgba.press_buttons(["A", "sleep 800"])
    
    print("Clearing 'ACE got on SHELLBY!' textbox...")
    mgba.press_buttons(["A", "sleep 500"])
    
    # Take a screenshot to verify we are surfing
    img = mgba.take_screenshot()
    print(f"Screenshot taken: {img}")

use_surf()
