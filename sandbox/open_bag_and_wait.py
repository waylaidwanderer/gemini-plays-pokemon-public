import mgba
import time

def open_bag():
    # Press B a few times to clear any potential menus or dialogues
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200"])
    
    # Open start menu
    mgba.press_buttons(["Start", "sleep 500"])
    
    # Go to ITEM (down twice from POKEDEX)
    mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "A", "sleep 500"])
    
    print("Bag should be open now!")

open_bag()
