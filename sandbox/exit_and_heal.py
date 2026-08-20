import mgba
import time

def main():
    print("Exiting Poké Mart and going to Pokémon Center...")
    
    # 1. Dismiss text
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # 2. Walk Down to exit Mart (from (3, 5))
    for _ in range(4):
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
        
    # Wait for warp/outside transition
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print("Outside Cinnabar coordinates:", pos)
    
    # We should be at (15, 12)
    if pos['y'] == 12:
        # Walk Left to (11, 12)
        dx = pos['x'] - 11
        print(f"Walking Left {dx} steps to Pokémon Center door...")
        for _ in range(dx):
            mgba.press_buttons(["Left"])
            time.sleep(0.5)
            
        # Walk Up into Pokémon Center
        print("Entering Pokémon Center...")
        mgba.press_buttons(["Up"])
        time.sleep(2.0) # Wait for enter warp
        
        pos_center = mgba.get_coordinates()
        print("Inside Pokémon Center coordinates:", pos_center)
        
        # Inside Pokémon Center, we land at (3, 8) or (3, 7) or (4, 8)
        # Nurse Joy is at (3, 3) or (3, 4). The counter is at Row 4.
        # Let's walk to (3, 4) or (3, 5) depending on the landing.
        # Let's walk Up to (3, 4) or (3, 5):
        pos_center = mgba.get_coordinates()
        if pos_center['x'] != 3:
            # Move horizontally to column 3
            dir_x = "Left" if pos_center['x'] > 3 else "Right"
            for _ in range(abs(pos_center['x'] - 3)):
                mgba.press_buttons([dir_x])
                time.sleep(0.5)
                
        pos_center = mgba.get_coordinates()
        # Move vertically to Row 5 (directly in front of Nurse Joy who is at Row 4)
        dy = pos_center['y'] - 5
        print(f"Walking Up {dy} steps to Nurse Joy...")
        for _ in range(dy):
            mgba.press_buttons(["Up"])
            time.sleep(0.5)
            
        pos_final = mgba.get_coordinates()
        print("At counter:", pos_final)
        
        # Interact with Nurse Joy and heal!
        print("Interacting with Nurse Joy...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Spam A to heal
        for _ in range(3):
            mgba.press_buttons(["A"])
            time.sleep(1.0)
            
        print("Waiting for healing jingle...")
        time.sleep(4.5)
        
        for _ in range(3):
            mgba.press_buttons(["A"])
            time.sleep(1.0)
            
        # Press B to make sure dialogue is closed
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        
        print("Healing complete!")
        mgba.take_screenshot()
        
    else:
        print("Unexpected coordinates outside!")
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
