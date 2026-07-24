import mgba
import time

def main():
    print("Opening main menu...")
    mgba.press_buttons(["Start", "sleep 500"])
    
    # Pokémon is the second option, so press Down once and A
    print("Opening POKéMON menu...")
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 1000"])
    
    # Take screenshot of Pokémon menu
    img1 = mgba.take_screenshot()
    print(f"Pokémon menu screenshot saved to: {img1}")
    
    # TRUFFLE is 2nd, so press Down once to highlight TRUFFLE, then A
    print("Selecting TRUFFLE...")
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 500"])
    
    # In the sub-menu, SWITCH is the 2nd option, so press Down once, then A
    print("Selecting SWITCH...")
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 500"])
    
    # Now select SHELLBY (1st Pokémon), so press Up once, then A
    print("Swapping with SHELLBY...")
    mgba.press_buttons(["Up", "sleep 200", "A", "sleep 1000"])
    
    # Take screenshot to verify swap
    img2 = mgba.take_screenshot()
    print(f"Swap verified, screenshot saved to: {img2}")
    
    # Close menu
    print("Closing menus...")
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200", "B", "sleep 200"])
    print("Done!")

if __name__ == "__main__":
    main()
