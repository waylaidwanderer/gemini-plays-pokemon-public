import mgba
import time

def enter_gym():
    print("Starting Viridian Gym entry script...")
    
    for attempt in range(100):
        pos = mgba.get_coordinates()
        print(f"Attempt {attempt}: Current position: {pos}")
        
        # Try to walk right
        mgba.press_buttons(["Right"])
        time.sleep(0.2)
        pos = mgba.get_coordinates()
        
        if pos['x'] >= 30:
            print("Successfully moved past the NPC!")
            # Walk to (32, 8)
            for _ in range(5):
                if pos['x'] < 32:
                    mgba.press_buttons(["Right"])
                    time.sleep(0.2)
                    pos = mgba.get_coordinates()
            print(f"Reached door column: {pos}")
            
            # Walk UP to enter the Gym
            mgba.press_buttons(["Up", "Up"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            print(f"Final position: {new_pos}")
            return True
            
        # Step left to give him space
        mgba.press_buttons(["Left"])
        time.sleep(0.2)
        # Step right back to (29, 8)
        mgba.press_buttons(["Right"])
        time.sleep(0.2)

    print("Failed to move past the NPC.")
    return False

enter_gym()
