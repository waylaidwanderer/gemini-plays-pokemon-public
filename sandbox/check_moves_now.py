import mgba
import time

def run():
    print("--- CHECKING SHELLBY'S MOVES ---")
    
    # 1. Open Start menu
    mgba.press_buttons(["Start", "sleep 500"])
    
    # Reset menu cursor to top
    for i in range(7):
        mgba.press_buttons(["Up", "sleep 100"])
        
    # 2. Select POKEMON (Down 1 time from POKEDEX)
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 600"])
    
    # 3. Select SHELLBY (slot 6, press Down 5 times)
    for i in range(5):
        mgba.press_buttons(["Down", "sleep 150"])
        
    # Press A to select SHELLBY
    mgba.press_buttons(["A", "sleep 500"])
    
    # 4. Select STATS (Down 2 times from top option which is SURF/USE)
    # Wait, if she knows SURF, the options are:
    # 1. SURF
    # 2. STATS
    # 3. SWITCH
    # 4. CANCEL
    # So STATS is Down 1 time!
    # Let's press Down twice to be safe or press Down once?
    # Wait, let's look at the check_moves_now.py:
    # "# 7. Press Down twice to highlight STATS (Option 3)"
    # Ah! In check_moves_now.py, STATS was option 3 because for TRUFFLE, the options are:
    # 1. CUT
    # 2. DIG
    # 3. STATS
    # 4. SWITCH
    # 5. CANCEL
    # But for SHELLBY, the only overworld move she knows is Surf. So her options are:
    # 1. SURF
    # 2. STATS
    # 3. SWITCH
    # 4. CANCEL
    # So STATS is indeed option 2 (Down once)!
    # Wait, to be safe, let's just press Down once, and if it's STATS, press A.
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 1000"])
    
    # Take screenshot of page 1 of stats
    path_s1 = mgba.take_screenshot()
    print("Stats Page 1:", path_s1)
    
    # 5. Press A to go to page 2 (moves)
    mgba.press_buttons(["A", "sleep 1000"])
    
    # Take screenshot of page 2 of stats
    path_s2 = mgba.take_screenshot()
    print("Stats Page 2 (Moves):", path_s2)
    
    # 6. Exit back to overworld by pressing B multiple times
    for i in range(5):
        mgba.press_buttons(["B", "sleep 300"])
        
    print("--- SHELLBY MOVES CHECK COMPLETE ---")

if __name__ == "__main__":
    run()
