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
    bridge.press_buttons(["A", "sleep 2500"]) # Wait for animation
    
    # Close any open dialogue boxes or menus
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 300"])
        
    # Test if tree is cut
    pos_before = get_pos()
    if pos_before != (26, 14):
        print(f"Error: Not at (26, 14), we are at {pos_before}")
        return False
        
    pos_after = walk_step_robust("Up")
    if pos_after == (26, 13):
        print(f"SUCCESS!!! Pokémon {pkmn_idx} Option {option_idx} CUT the tree! Position is {pos_after}")
        return True
    else:
        print(f"Option {option_idx} on Pokémon {pkmn_idx} did NOT cut the tree. Position remains {pos_after}")
        return False

def main():
    pos = get_pos()
    if pos != (26, 14):
        print(f"Not at (26, 14), navigating there first. Currently at {pos}")
        bridge.press_buttons(["B", "sleep 200"])
        # Simple walk to (26, 14)
        if pos is not None:
            if pos[0] < 26: bridge.press_buttons(["Right", "sleep 400"])
            elif pos[0] > 26: bridge.press_buttons(["Left", "sleep 400"])
            pos = get_pos()
            if pos is not None:
                if pos[1] < 14: bridge.press_buttons(["Down", "sleep 400"])
                elif pos[1] > 14: bridge.press_buttons(["Up", "sleep 400"])
                
    # We will test Option 1 (Down once) for all 5 Pokémon.
    # We will also test Option 2 (Down twice) for Pokémon 1 (TRUFFLE) just in case.
    test_list = [
        (1, 1), # Pokémon 1, Option 1
        (1, 2), # Pokémon 1, Option 2
        (0, 1), # Pokémon 0, Option 1
        (2, 1), # Pokémon 2, Option 1
        (3, 1), # Pokémon 3, Option 1
        (4, 1), # Pokémon 4, Option 1
    ]
    
    for pkmn_idx, option_idx in test_list:
        if try_cut_combination(pkmn_idx, option_idx):
            break

if __name__ == "__main__":
    main()
