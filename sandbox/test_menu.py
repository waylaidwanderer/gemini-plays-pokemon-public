import mgba
import time

def test():
    # Clear any menus
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200", "B", "sleep 200"])
    
    # Open start menu
    mgba.press_buttons(["Start", "sleep 500"])
    
    # Press Up 10 times to guarantee we are at the top (POKEDEX)
    for _ in range(10):
        mgba.press_buttons(["Up", "sleep 100"])
        
    # Press Down twice to go to ITEM
    mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200"])
    
    # Press A to open the bag
    mgba.press_buttons(["A", "sleep 500"])
    
    # Take screenshot of first page of bag
    mgba.take_screenshot()
    print("Screenshot of first page of bag taken!")
    
    # Scroll down 7 times to see next page of bag
    for _ in range(7):
        mgba.press_buttons(["Down", "sleep 100"])
    mgba.take_screenshot()
    print("Screenshot of second page of bag taken!")
    
    # Close bag and menu
    mgba.press_buttons(["B", "sleep 300", "Start", "sleep 300"])

test()
