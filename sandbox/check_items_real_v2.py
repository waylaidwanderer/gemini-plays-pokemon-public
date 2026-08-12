import mgba
import time
import shutil

def check():
    print("Closing any open dialogue first...")
    mgba.press_buttons(["B", "sleep 500", "B", "sleep 500"])
    
    print("Pressing Start...")
    mgba.press_buttons(["Start", "sleep 500"])
    
    print("Moving to ITEM...")
    # Let's move down to ITEM (ITEM is 2nd in start menu, below Pokedex)
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 500"])
    
    print("Taking screenshot of inventory...")
    scr = mgba.take_screenshot()
    print("Screenshot path returned:", scr)
    shutil.copy(scr, "inventory_page_real.png")
    print("Saved to inventory_page_real.png")
    
    # Close menu
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200"])

if __name__ == "__main__":
    check()
