import mgba
import time

def leave():
    print("Leaving Viridian...")
    # Up 3 times to (22, 4)
    for _ in range(3):
        mgba.press_buttons(["Up"])
        time.sleep(0.15)
        
    print(f"At: {mgba.get_coordinates()}")
    
    # Left 4 times to (18, 4)
    for _ in range(4):
        mgba.press_buttons(["Left"])
        time.sleep(0.15)
        
    print(f"At: {mgba.get_coordinates()}")
    
    # Down 31 times to transition to Route 1 (y=35)
    for i in range(35):
        mgba.press_buttons(["Down"])
        time.sleep(0.12)
        pos = mgba.get_coordinates()
        if pos['y'] >= 35:
            print(f"Transitioned! Position: {pos}")
            break

leave()
