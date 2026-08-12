import mgba
import time
from PIL import Image

def check():
    print("Closing any open dialogue first...")
    mgba.press_buttons(["B", "sleep 500", "B", "sleep 500"])
    
    print("Pressing Start...")
    mgba.press_buttons(["Start", "sleep 500"])
    
    print("Moving to ITEM...")
    # From top of start menu: ITEM is usually the second option (Below Pokedex)
    # Let's press Down once and A
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 500"])
    
    print("Taking screenshot of inventory...")
    scr = mgba.take_screenshot()
    img = Image.open(scr)
    img.save("inventory_page_real.png")
    print("Saved to inventory_page_real.png")
    
    # Close menu
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200"])

if __name__ == "__main__":
    check()
