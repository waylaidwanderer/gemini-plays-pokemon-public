import mgba
import time

def enter_gym():
    print("Entering Viridian Gym from (20, 35)...")
    
    # 1. Walk Right to Column 32 on Row 35
    for _ in range(12):
        mgba.press_buttons(["Right"])
        time.sleep(0.12)
        
    pos = mgba.get_coordinates()
    print(f"At Column 32: {pos}")
    
    # 2. Walk UP all the way to enter the Gym
    # We are at (32, 35) and need to reach (32, 7)
    # That is exactly 28 steps UP.
    for i in range(30):
        mgba.press_buttons(["Up"])
        time.sleep(0.12)
        pos = mgba.get_coordinates()
        # If we enter the Gym, the coordinates will reset/change dramatically
        if pos['y'] < 5 or pos['y'] > 35: 
            print(f"Successfully entered Gym! Position: {pos}")
            break
            
    print(f"Final Position: {mgba.get_coordinates()}")

enter_gym()
