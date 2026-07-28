import mgba
import time

def main():
    print("Opening START menu...")
    mgba.press_buttons(["Start", "sleep 400"])
    
    # In START menu, cursor is initially on POKEDEX or POKEMON.
    # Let's move down to ITEM. ITEM is 2 steps down from POKEDEX.
    # POKEDEX -> POKEMON -> ITEM.
    # Let's press Down twice.
    mgba.press_buttons(["Down", "sleep 150", "Down", "sleep 150"])
    
    # Press A to open ITEM
    mgba.press_buttons(["A", "sleep 500"])
    
    # Take screenshot of Page 1 of ITEM bag
    scr1 = mgba.take_screenshot()
    print(f"Bag Page 1: {scr1}")
    
    # Scroll down 4 times to see the rest of the items
    for i in range(4):
        mgba.press_buttons(["Down", "sleep 150"])
    
    # Take screenshot of Page 2 of ITEM bag
    scr2 = mgba.take_screenshot()
    print(f"Bag Page 2: {scr2}")
    
    # Exit menu
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200", "B", "sleep 200"])
    print("Closed menus.")

if __name__ == "__main__":
    main()
