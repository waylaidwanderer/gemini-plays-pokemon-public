import mgba
import time

def enter_mansion():
    print("Exiting Pokemon Lab...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # 1. Walk Down to exit Lab
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    mgba.press_buttons(["Down"])
    time.sleep(1.5) # Wait for warp outside
    
    pos = mgba.get_coordinates()
    print("Outside Pokemon Lab. Position:", pos)
    
    # 2. Walk North to find Pokemon Mansion entrance
    # We should be at (3, 8) or adjacent. Walk Up as far as we can!
    print("Walking North to find Mansion entrance...")
    for step in range(10):
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        curr = mgba.get_coordinates()
        print(f"Step {step+1}: position: {curr}")
        
        # If the map changed to Pokémon Mansion 1F, we successfully warped!
        # The coordinates inside Mansion 1F entrance are usually around (9, 27) or similar.
        # But we'll definitely detect a map transition or different coords.
        # Let's check if the coordinates are in the Mansion range or if we are blocked.
        
    mgba.take_screenshot()

if __name__ == "__main__":
    enter_mansion()
