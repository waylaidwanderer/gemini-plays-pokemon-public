import mgba
import time

def check():
    # Dismiss any menus or dialogues first
    mgba.press_buttons(["B", "sleep 200"])
    
    # 1. Open start menu
    print("Opening start menu...")
    mgba.press_buttons(["Start", "sleep 500"])
    mgba.take_screenshot()
    
    # 2. Let's go down to Trainer Card
    # On start menu, default is POKEDEX.
    # Menu layout:
    # 1. POKEDEX
    # 2. POKEMON
    # 3. ITEM
    # 4. ACE (Trainer name)
    # 5. SAVE
    # 6. OPTION
    # 7. EXIT
    # To get to Trainer name: Down, Down, Down.
    print("Going to Trainer Card...")
    mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "A", "sleep 500"])
    screenshot_path = mgba.take_screenshot()
    print("Trainer Card screenshot:", screenshot_path)
    
    # Exit Trainer Card
    mgba.press_buttons(["B", "sleep 500"])
    
    # 3. Go to ITEM (it was position 3, so from Trainer Card (position 4) we press Up once)
    print("Going to ITEM menu...")
    mgba.press_buttons(["Up", "sleep 200", "A", "sleep 500"])
    mgba.take_screenshot()
    
    # Scroll down to see all items (max 20 items, 7 displayed at once)
    for i in range(3):
        print(f"Scrolling down items page {i+1}...")
        mgba.press_buttons(["Down", "Down", "Down", "Down", "Down", "Down", "Down", "sleep 300"])
        mgba.take_screenshot()
        
    # Exit item menu
    mgba.press_buttons(["B", "sleep 500"])
    # Exit start menu
    mgba.press_buttons(["Start", "sleep 500"])
    print("Check complete!")

check()
