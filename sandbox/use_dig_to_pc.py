import time
import sys
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def use_dig_from_pokedex():
    print("Closing POKÉDEX and opening POKÉMON menu...")
    # Currently inside POKÉDEX. Press B twice to return to overworld.
    bridge.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    
    # Open Start menu (cursor is guaranteed to be on POKÉDEX)
    bridge.press_buttons(["Start", "sleep 500"])
    
    # Press DOWN once to select POKÉMON
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 1200"])
    
    # Now we are inside Choose a POKÉMON menu.
    # To be 100% sure we select TRUFFLE (slot 2):
    # Let's align party list cursor by pressing DOWN 5 times with sleep (loops back to SHELLBY slot 1)
    # Actually, in the Choose a POKÉMON menu, the cursor memory is preserved.
    # But since the menu wraps, let's do:
    # Open TRUFFLE (slot 2): if the cursor was on SHELLBY, we press Down once and A.
    # If the cursor was on TRUFFLE, we press A directly.
    # To be safe, let's assume the cursor starts at the top (SHELLBY) as it does when freshly opened,
    # or let's just use our knowledge that TRUFFLE is slot 2.
    # If we press UP 5 times, it aligns to slot 1 (SHELLBY).
    # Wait, if we press UP 5 times on Choose a POKÉMON, does it wrap?
    # Yes, we saw "UP on slot 1 wraps to slot 5".
    # But wait! If the cursor was on slot 5, pressing UP 5 times:
    # 5 -> 4 (Up 1) -> 3 (Up 2) -> 2 (Up 3) -> 1 (Up 4) -> 5 (Up 5).
    # So it wraps.
    # But if we press UP 4 times from slot 5:
    # 5 -> 4 -> 3 -> 2 -> 1. It lands on slot 1!
    # If we start on slot 2, pressing UP 4 times:
    # 2 -> 1 -> 5 -> 4 -> 3. It lands on slot 3.
    # This is tricky because of cursor memory.
    # But wait! There is an easier way.
    # We can just select the first Pokémon (SHELLBY), open its menu, press B.
    # And then we will know exactly where the cursor is!
    # Actually, let's just press DOWN once and A.
    # If the cursor starts on SHELLBY (slot 1), pressing Down once selects TRUFFLE (slot 2).
    # Let's try this first:
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 800"])
    
    # Open options menu for the selected Pokémon.
    # Press A to select first option (DIG or SURF/STATS)
    bridge.press_buttons(["A", "sleep 4000"]) # Select DIG and wait for warp!

def main():
    pos = get_pos()
    print(f"Starting at: {pos}")
    
    # We are currently inside POKÉDEX menu (so pos is None or 10, 24)
    use_dig_from_pokedex()
    
    pos = get_pos()
    print(f"Warped! Position outside: {pos}")
    
    # 2. Enter the Pokémon Center
    if pos == (19, 28):
        print("Entering Pokémon Center...")
        bridge.press_buttons(["Up", "sleep 1500"])
        
    pos = get_pos()
    print(f"Position inside Pokémon Center: {pos}")
    
    # 3. Navigate to the PC at (13, 4)
    if pos is not None and pos[1] >= 7:
        print("Navigating to PC...")
        bridge.press_buttons(["Up", "sleep 400", "Up", "sleep 400", "Up", "sleep 400"]) # to (3, 5) or (4, 5)
        # Walk to PC
        bridge.press_buttons(["Right", "sleep 400", "Right", "sleep 400", "Right", "sleep 400", 
                              "Right", "sleep 400", "Right", "sleep 400", "Right", "sleep 400",
                              "Right", "sleep 400", "Right", "sleep 400", "Right", "sleep 400"]) # to (13, 5)
        bridge.press_buttons(["Up", "sleep 500"]) # to (13, 4)
        
        print("Facing UP towards PC...")
        bridge.press_buttons(["Up", "sleep 500"])
        
        # 4. Open the PC menu and go to Withdraw Item
        print("Opening PC menu...")
        bridge.press_buttons(["A", "sleep 1200"]) # Turn on PC
        bridge.press_buttons(["A", "sleep 1200"]) # Progress boot text
        bridge.press_buttons(["Down", "sleep 500", "A", "sleep 1200"]) # Select ACE's PC
        bridge.press_buttons(["A", "sleep 1500"]) # Select WITHDRAW ITEM
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final Position: {pos}")
    
    # Take screenshot of final screen
    img = mgba.take_screenshot()
    print(f"Screenshot of PC menu: {img}")

if __name__ == "__main__":
    main()
