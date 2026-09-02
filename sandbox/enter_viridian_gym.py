import mgba
import time

def enter_gym_from_30():
    print("Walking east on Row 30 to Column 32...")
    # Walk Right to x=32
    for _ in range(15):
        pos = mgba.get_coordinates()
        if pos['x'] >= 32:
            break
        mgba.press_buttons(["Right"])
        time.sleep(0.15)
        
    pos = mgba.get_coordinates()
    print(f"At: {pos}")
    
    # Walk UP to enter Gym (needs about 23 steps)
    for i in range(25):
        mgba.press_buttons(["Up"])
        time.sleep(0.15)
        pos = mgba.get_coordinates()
        if pos['y'] < 5 or pos['y'] > 35: # map transitioned
            print(f"Entered Gym! Position: {pos}")
            break
            
    print(f"Final Position: {mgba.get_coordinates()}")

enter_gym_from_30()
