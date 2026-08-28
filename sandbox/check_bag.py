import mgba
import time

def check_bag():
    # Ensure any menus are dismissed
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200"])
    
    # Open start menu
    print("Opening Start Menu...")
    mgba.press_buttons(["Start", "sleep 400"])
    
    # POKEDEX is at slot 1, POKEMON at slot 2, ITEM at slot 3.
    # From top, press Down, Down, then A.
    print("Selecting ITEM...")
    mgba.press_buttons(["Down", "sleep 150", "Down", "sleep 150", "A", "sleep 400"])
    
    # Save first page of bag
    print("Taking page 1 screenshot...")
    mgba.take_screenshot()
    
    # Scroll down to page 2
    print("Scrolling down...")
    mgba.press_buttons(["Down", "Down", "Down", "Down", "Down", "Down", "Down", "sleep 300"])
    mgba.take_screenshot()
    
    # Scroll down to page 3
    print("Scrolling down again...")
    mgba.press_buttons(["Down", "Down", "Down", "Down", "Down", "Down", "Down", "sleep 300"])
    mgba.take_screenshot()
    
    # Dismiss menu
    print("Closing menus...")
    mgba.press_buttons(["B", "sleep 300", "Start", "sleep 300"])
    print("Bag check complete!")

check_bag()
