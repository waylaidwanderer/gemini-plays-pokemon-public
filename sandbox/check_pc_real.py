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

def use_dig_from_overworld():
    print("Using DIG to return to Fuchsia Pokemon Center...")
    # Open Start menu
    bridge.press_buttons(["Start", "sleep 500"])
    
    # Align to POKÉDEX (press UP 6 times)
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 150"])
        
    # Select POKÉMON (Down once from POKÉDEX, A)
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 1200"])
    
    # Select TRUFFLE slot 2 (press Down once, A)
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 800"])
    
    # Select DIG (which is the first option for TRUFFLE, press A)
    bridge.press_buttons(["A", "sleep 4000"]) # Use DIG and wait for warp!

def main():
    # 1. Clear "Got away safely!" text by pressing B
    print("Clearing battle text...")
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    
    # 2. Use DIG
    use_dig_from_overworld()
    
    pos = get_pos()
    print(f"Position after DIG: {pos}")
    
    # We should be at (19, 28) outside the Pokemon Center. Enter it.
    if pos == (19, 28):
        print("Entering Pokémon Center...")
        bridge.press_buttons(["Up", "sleep 1500"])
        
    pos = get_pos()
    print(f"Inside Pokémon Center: {pos}")
    
    # 3. Walk to PC at (13, 4)
    # Inside Pokemon Center, we start at (3, 7) or (4, 7) on the doormat.
    if pos is not None and pos[1] >= 6:
        print("Navigating to PC...")
        # Walk up to Row 5
        bridge.press_buttons(["Up", "sleep 400", "Up", "sleep 400", "Up", "sleep 400"]) # to (3, 5) or (4, 5)
        # Walk to Column 13
        for _ in range(9):
            bridge.press_buttons(["Right", "sleep 400"])
        # Walk UP to stand in front of PC at (13, 4)
        bridge.press_buttons(["Up", "sleep 400"])
        # Face UP
        bridge.press_buttons(["Up", "sleep 500"])
        
    pos = get_pos()
    print(f"Standing in front of PC: {pos}")
    
    # 4. Turn on PC and open Withdraw menu
    print("Opening ACE's PC Withdraw menu...")
    bridge.press_buttons(["A", "sleep 1200"]) # Turn on PC
    bridge.press_buttons(["A", "sleep 1200"]) # Progress boot text "ACE turned on the PC!"
    bridge.press_buttons(["A", "sleep 1200"]) # Progress "Access whose PC?"
    bridge.press_buttons(["A", "sleep 1500"]) # Select ACE's PC
    bridge.press_buttons(["A", "sleep 1500"]) # Select WITHDRAW ITEM
    
    # Take screenshot of page 1 of PC Withdraw
    p1 = mgba.take_screenshot()
    print(f"PC Withdraw Page 1: {p1}")
    
    # Scroll down 10 times to see every single item in the PC, taking screenshots
    for i in range(5):
        bridge.press_buttons(["Down", "sleep 300"])
        p = mgba.take_screenshot()
        print(f"PC Scroll {i+1}: {p}")
        
    # Close PC menu safely by pressing B multiple times
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 400"])
        
    pos = get_pos()
    print(f"Final overworld position: {pos}")

if __name__ == "__main__":
    main()
