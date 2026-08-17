import mgba
import time

def run():
    print("--- STARTING TEACH STRENGTH SCRIPT ---")
    
    # 1. Open Start menu from overworld
    mgba.press_buttons(["Start", "sleep 500"])
    
    # Reset menu cursor to top (POKEDEX)
    for i in range(7):
        mgba.press_buttons(["Up", "sleep 100"])
        
    # 2. Select ITEM (Down 2 times from POKEDEX)
    mgba.press_buttons(["Down", "Down", "sleep 200", "A", "sleep 600"])
    
    # 3. We are in the bag now. Scroll down to HM04 (7th item, press Down 6 times)
    for i in range(6):
        mgba.press_buttons(["Down", "sleep 150"])
        
    # Take screenshot of selected item to verify we are on HM04
    path_bag = mgba.take_screenshot()
    print("Screenshot on HM04 item:", path_bag)
    
    # 4. Press A to select HM04
    mgba.press_buttons(["A", "sleep 400"])
    
    # 5. Select "USE" (it is the first option, so just press A)
    mgba.press_buttons(["A", "sleep 600"])
    
    # 6. We should be on the "Choose a POKéMON" party menu.
    # SHELLBY is in slot 6, so press Down 5 times to select SHELLBY.
    for i in range(5):
        mgba.press_buttons(["Down", "sleep 150"])
        
    path_party = mgba.take_screenshot()
    print("Screenshot on SHELLBY in party:", path_party)
    
    # 7. Press A to select SHELLBY
    mgba.press_buttons(["A", "sleep 1000"])
    
    # 8. Dialogue text "HM04 contains STRENGTH. Teach it to a POKéMON?"
    # Press A to advance/say Yes
    mgba.press_buttons(["A", "sleep 1000"])
    
    # 9. "Delete an older move to make room for STRENGTH?"
    # Yes/No prompt: YES is the default first option. Press A to select YES.
    mgba.press_buttons(["A", "sleep 1000"])
    
    # 10. We should now be in the move selection screen showing SHELLBY's moves.
    # The moves should be:
    # 1. SURF
    # 2. HYDRO PUMP
    # 3. ICE BEAM
    # 4. BITE
    # Let's select BITE in slot 4 (press Down 3 times).
    for i in range(3):
        mgba.press_buttons(["Down", "sleep 150"])
        
    path_moves = mgba.take_screenshot()
    print("Screenshot on move selection (BITE):", path_moves)
    
    # 11. Press A to delete BITE
    mgba.press_buttons(["A", "sleep 1000"])
    
    # Dialogue: "1, 2 and... Poof! SHELLBY forgot BITE! And... SHELLBY learned STRENGTH!"
    # Press A several times with pauses to dismiss the text boxes.
    for i in range(5):
        mgba.press_buttons(["A", "sleep 800"])
        
    # Exit back to overworld by pressing B multiple times
    for i in range(4):
        mgba.press_buttons(["B", "sleep 300"])
        
    path_final = mgba.take_screenshot()
    print("Final overworld screenshot:", path_final)
    print("--- TEACH STRENGTH SCRIPT COMPLETE ---")

if __name__ == "__main__":
    run()
