import mgba
import time

def check_bag():
    print("Opening Start Menu...")
    mgba.press_buttons(["Start", "sleep 500"])
    
    # Take screenshot of menu
    img1 = mgba.take_screenshot()
    print("Screenshot 1 saved to:", img1)
    
    # We are usually at top (Pokedex or Pokemon). Let's scroll down to ITEM.
    # From top: Pokedex -> Pokemon -> Item
    # Let's press Down 2 times, then A.
    mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "A", "sleep 500"])
    
    # Take screenshot of Item menu (page 1)
    img2 = mgba.take_screenshot()
    print("Screenshot 2 (Item Page 1) saved to:", img2)
    
    # Let's scroll down a few times to see page 2
    for i in range(4):
        mgba.press_buttons(["Down", "sleep 150"])
    mgba.press_buttons(["sleep 300"])
    
    img3 = mgba.take_screenshot()
    print("Screenshot 3 (Item Page 2) saved to:", img3)
    
    # Scroll down further
    for i in range(4):
        mgba.press_buttons(["Down", "sleep 150"])
    mgba.press_buttons(["sleep 300"])
    
    img4 = mgba.take_screenshot()
    print("Screenshot 4 (Item Page 3) saved to:", img4)
    
    # Close menu
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300", "B"])
    print("Closed menu.")

if __name__ == '__main__':
    check_bag()
