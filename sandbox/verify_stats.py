import mgba
import time

def main():
    print("Closing battle textbox...")
    mgba.press_buttons(["A", "sleep 500"])
    
    print("Opening main menu...")
    mgba.press_buttons(["Start", "sleep 500"])
    
    # Pokémon is the second option, so press Down once and A
    print("Opening POKéMON menu...")
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 1000"])
    
    # Take screenshot of POKéMON menu
    img_party = mgba.take_screenshot()
    print(f"Party list screenshot: {img_party}")
    
    # TESLA is in slot 1, so press A to select, then A to select STATS
    print("Opening TESLA stats...")
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 500"])
    img_tesla_stats1 = mgba.take_screenshot()
    print(f"TESLA stats page 1: {img_tesla_stats1}")
    
    # Press A to go to page 2 (moves and PP)
    mgba.press_buttons(["A", "sleep 500"])
    img_tesla_stats2 = mgba.take_screenshot()
    print(f"TESLA stats page 2: {img_tesla_stats2}")
    
    # Press B to go back to party list
    mgba.press_buttons(["B", "sleep 500"])
    
    # Highlight TRUFFLE in slot 5 (Pikachu, Wartortle, Pidgey, Rattata, Paras)
    # We are currently at slot 1, so press Down 4 times
    print("Navigating to TRUFFLE...")
    mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200", "Down", "sleep 200"])
    
    # Select TRUFFLE and open STATS
    print("Opening TRUFFLE stats...")
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 500"])
    img_truffle_stats1 = mgba.take_screenshot()
    print(f"TRUFFLE stats page 1: {img_truffle_stats1}")
    
    # Press A to go to page 2 (moves and PP)
    mgba.press_buttons(["A", "sleep 500"])
    img_truffle_stats2 = mgba.take_screenshot()
    print(f"TRUFFLE stats page 2: {img_truffle_stats2}")
    
    # Close all menus
    print("Closing menus...")
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200", "B", "sleep 200"])
    print("Done!")

if __name__ == "__main__":
    main()
