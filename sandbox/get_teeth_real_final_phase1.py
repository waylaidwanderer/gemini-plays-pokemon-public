import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        bridge.press_buttons(["B", "sleep 200"])
        return get_pos()
    bridge.press_buttons([direction, "sleep 400"])
    new_pos = get_pos()
    if new_pos is None:
        bridge.press_buttons(["B", "sleep 200"])
        return get_pos()
    return new_pos

def try_cut_combination(pkmn_idx, option_idx):
    print(f"\n--- Testing Pokémon {pkmn_idx} with Option {option_idx} ---")
    
    # Ensure menu is closed
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])
        
    # Face UP
    bridge.press_buttons(["Up", "sleep 400"])
    
    # Open Start menu
    bridge.press_buttons(["Start", "sleep 400"])
    
    # Align cursor to POKÉDEX
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 150"])
        
    # Select POKÉMON (Down once, then A)
    bridge.press_buttons(["Down", "sleep 200", "A", "sleep 800"])
    
    # Select Pokémon pkmn_idx
    for _ in range(pkmn_idx):
        bridge.press_buttons(["Down", "sleep 150"])
    bridge.press_buttons(["A", "sleep 500"])
    
    # Select option_idx
    for _ in range(option_idx):
        bridge.press_buttons(["Down", "sleep 150"])
    bridge.press_buttons(["A", "sleep 2000"]) # Wait for potential CUT animation
    
    # Close any open dialogue boxes or menus
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 300"])
        
    # Test if tree is cut by trying to walk UP
    print("Testing if tree is cut...")
    pos_before = get_pos()
    if pos_before is None:
        return False
        
    pos_after = walk_step_robust("Up")
    if pos_after is not None and pos_after[1] < pos_before[1]:
        print(f"SUCCESS!!! Pokémon {pkmn_idx} Option {option_idx} CUT the tree! Arrived at {pos_after}")
        return True
    else:
        print("Tree is NOT cut.")
        return False

def main():
    pos = get_pos()
    if pos != (26, 14):
        print(f"Not at (26, 14), navigating there first. Currently at {pos}")
        # Navigate to (26, 14)
        # Assuming we are very close
        bridge.press_buttons(["B", "sleep 200"])
        # Walk to (26, 14)
        if pos is not None:
            if pos[0] < 26: bridge.press_buttons(["Right", "sleep 400"])
            elif pos[0] > 26: bridge.press_buttons(["Left", "sleep 400"])
            pos = get_pos()
            if pos is not None:
                if pos[1] < 14: bridge.press_buttons(["Down", "sleep 400"])
                elif pos[1] > 14: bridge.press_buttons(["Up", "sleep 400"])
    
    # Try all combinations of Pokémon (0-4) and options (0-2)
    # Total combinations = 15. Each takes about 6-8 seconds.
    # To avoid exceeding 100 buttons, we can test 3-4 combinations per run,
    # but we can do it strategically.
    # Let's test pkmn 1 (TRUFFLE) option 0 and 1 first.
    # pkmn 1 is index 1.
    # Let's run a focused search!
    
    # Standard order:
    # Index 1 is TRUFFLE. Let's test index 1 option 0, 1, 2.
    # Index 2 is GUSTY. Let's test index 2 option 0, 1.
    # Index 3 is NIBBLES. Let's test index 3 option 0, 1.
    
    test_list = [
        (1, 0), # TRUFFLE option 0
        (1, 1), # TRUFFLE option 1 (likely CUT)
        (1, 2), # TRUFFLE option 2
        (2, 0), # GUSTY option 0
        (2, 1), # GUSTY option 1
    ]
    
    for pkmn_idx, option_idx in test_list:
        if try_cut_combination(pkmn_idx, option_idx):
            break

if __name__ == "__main__":
    main()
