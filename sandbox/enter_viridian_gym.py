import mgba
import time

def enter_gym_safe():
    print("Executing safe path around the NPC and through the fence gap...")
    
    # 1. Walk Left from (26, 8) to Column 19
    for _ in range(7):
        mgba.press_buttons(["Left"])
        time.sleep(0.15)
        
    print(f"At: {mgba.get_coordinates()}")
    
    # 2. Walk Down to Row 10
    for _ in range(2):
        mgba.press_buttons(["Down"])
        time.sleep(0.15)
        
    print(f"At Row 10: {mgba.get_coordinates()}")
    
    # 3. Walk Right to Column 32
    for _ in range(13):
        mgba.press_buttons(["Right"])
        time.sleep(0.15)
        
    print(f"At Column 32: {mgba.get_coordinates()}")
    
    # 4. Walk UP into the Gym
    # (32, 10) -> (32, 7) is 3 steps UP
    for i in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.15)
        pos = mgba.get_coordinates()
        if pos['y'] < 5 or pos['y'] > 35:
            print(f"Entered Gym! Position: {pos}")
            break
            
    print(f"Final Position: {mgba.get_coordinates()}")

enter_gym_safe()
