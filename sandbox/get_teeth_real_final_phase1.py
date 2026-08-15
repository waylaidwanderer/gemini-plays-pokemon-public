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

def main():
    pos = get_pos()
    print(f"Initial Position: {pos}")
    if pos != (26, 14):
        print("Error: We must start at (26, 14)!")
        return
        
    # Let's test Pokémon 1 (TRUFFLE) with Option 1 (which should be CUT)
    print("Testing Pokémon 1 with Option 1...")
    
    # Face UP
    bridge.press_buttons(["Up", "sleep 400"])
    
    # Open Start menu
    bridge.press_buttons(["Start", "sleep 400"])
    
    # Align cursor to POKÉDEX
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 150"])
        
    # Select POKÉMON
    bridge.press_buttons(["Down", "sleep 200", "A", "sleep 800"])
    
    # Select 2nd Pokémon (TRUFFLE)
    bridge.press_buttons(["Down", "sleep 200", "A", "sleep 500"])
    
    # Select Option 1 (Down once, then A)
    bridge.press_buttons(["Down", "sleep 200", "A", "sleep 3000"]) # Wait 3s for CUT animation
    
    # Dismiss any text
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 300"])
        
    # Try to walk UP
    print("Testing if tree is cut...")
    pos_after = walk_step_robust("Up")
    print(f"Position after testing: {pos_after}")
    
    if pos_after == (26, 13):
        print("SUCCESS!!! Pokémon 1 Option 1 CUT the tree!")
    else:
        print("Option 1 did NOT cut the tree.")

if __name__ == "__main__":
    main()
