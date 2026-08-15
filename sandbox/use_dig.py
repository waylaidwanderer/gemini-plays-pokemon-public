import time
import bridge

def main():
    print("Opening main menu...")
    bridge.press_buttons(["Start", "sleep 300"])
    
    # Cursor starts on POKEDEX. Pokémon is Down, Down, A
    print("Navigating to POKÉMON...")
    bridge.press_buttons(["Down", "sleep 150", "Down", "sleep 150", "A", "sleep 600"])
    
    # We are in the Pokémon menu. Let's try to find DIG on each Pokémon (1 to 5)
    # The party size is 5.
    for i in range(5):
        print(f"Checking Pokémon {i+1}...")
        # Select Pokémon i
        bridge.press_buttons(["A", "sleep 500"])
        
        # Take a screenshot of the menu options (e.g. DIG, HP, etc.)
        img = bridge.take_screenshot()
        print(f"Option menu for Pokémon {i+1} saved: {img}")
        
        # In Gen 1, when you select a Pokémon in the overworld, if they have an HM/field move,
        # it is listed at the top (e.g., CUT, DIG, SURF, FLASH, TELEPORT, SOFTBOILED, MILK DRINK).
        # We can press Down twice and press B to cancel if they don't have DIG,
        # or we can check if DIG is there.
        # Let's cancel and try the next one.
        # But wait! If they have DIG, it will be the first option!
        # If they don't, the first option might be "STATS" or "SWITCH".
        # Let's press B to close the option menu for this Pokémon
        bridge.press_buttons(["B", "sleep 300"])
        
        # Move cursor to the next Pokémon (Down once)
        bridge.press_buttons(["Down", "sleep 200"])
        
    # Exit Pokémon menu
    bridge.press_buttons(["B", "sleep 300"])
    bridge.press_buttons(["Start", "sleep 300"])
    print("Party check complete.")

if __name__ == "__main__":
    main()
