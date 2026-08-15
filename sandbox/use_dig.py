import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Executing automatic DIG search and use...")
    
    # Ensure menu is closed
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    
    for i in range(5):
        print(f"\n--- Checking Pokémon {i+1} ---")
        
        # Open main menu
        bridge.press_buttons(["Start", "sleep 400"])
        
        # Select POKÉMON (Down twice, then A)
        bridge.press_buttons(["Down", "sleep 150", "Down", "sleep 150", "A", "sleep 800"])
        
        # Move cursor to Pokémon i
        for _ in range(i):
            bridge.press_buttons(["Down", "sleep 150"])
            
        # Press A to open option menu
        bridge.press_buttons(["A", "sleep 500"])
        
        # Press A to select first option (either DIG/field move or STATS)
        print("Selecting first option...")
        bridge.press_buttons(["A", "sleep 1500"])
        
        # Check if we warped to Fuchsia City (y near 28, x near 19)
        pos = get_pos()
        print(f"Coordinates: {pos}")
        if pos is not None and pos[1] == 28:
            print("SUCCESS! Warped out of Safari Zone using DIG!")
            return
            
        # If we didn't warp, we are probably in the Stats screen or still in the menu.
        # Press B twice to cancel out back to overworld
        print("Not warped, cancelling...")
        bridge.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
        time.sleep(0.5)

    print("Checked all 5 Pokémon. None of them used DIG.")

if __name__ == "__main__":
    main()
