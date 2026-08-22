import mgba
import time

def select_pkmn_and_dig():
    # 1. Open Start Menu
    print("Opening Start Menu...")
    mgba.press_buttons(["Start"])
    time.sleep(1.0)
    
    # 2. Go to PKMN (usually 2nd option, press Down once from Pokedex)
    print("Selecting PKMN...")
    mgba.press_buttons(["Down", "sleep 100", "A"])
    time.sleep(1.5)
    
    # Let's take a screenshot of the party to see where TRUFFLE is
    mgba.take_screenshot()
    
    # Let's search for TRUFFLE in the party list.
    # We can try to scroll down to select the 2nd, 3rd, etc. Pokémon
    # Usually TRUFFLE is the last Pokémon (6th) or first/second depending on deposits.
    # Let's write code to try each index in the party menu to find the one with DIG.
    # Or we can just try index 2 first (press Down once), index 3 (press Down twice), etc.
    # Wait, let's write a loop that tries to find DIG on each Pokémon in the party!
    # For each index from 0 to 5:
    #   - Press A on the Pokémon.
    #   - If a menu with "DIG" / "CUT" / "STATS" / "SWITCH" appears, check if DIG is there and select it.
    #   - If not, press B to go back and try the next Pokémon.
    
    # Wait, let's keep it simple: let's press Down 5 times to go to the 6th Pokémon, which is usually our utility Paras (TRUFFLE)!
    # Let's verify: "TRUFFLE (Paras) (the 6th Pokemon in our party)" (from Turn 52925)
    # Yes! TRUFFLE is the 6th Pokémon in our party!
    # So we press Down 5 times, then A.
    print("Navigating to 6th Pokémon (TRUFFLE)...")
    for _ in range(5):
        mgba.press_buttons(["Down"])
        time.sleep(0.2)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Take screenshot of the submenu
    mgba.take_screenshot()
    
    # Inside the submenu:
    # According to Progression_And_Party_Stats.md:
    # "Option 1: DIG
    #  Option 2: CUT"
    # So "DIG" is the very first option!
    # We just press A!
    print("Selecting DIG...")
    mgba.press_buttons(["A"])
    time.sleep(3.0)

select_pkmn_and_dig()
print("Current position after DIG:", mgba.get_coordinates())
mgba.take_screenshot()
