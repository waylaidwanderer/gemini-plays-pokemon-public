import mgba
import time

def walk_to_route1():
    print("Walking north to Route 1...")
    # Right 2 times to (9, 13)
    for _ in range(2):
        mgba.press_buttons(["Right"])
        time.sleep(0.15)
        
    print(f"At: {mgba.get_coordinates()}")
    
    # Up 14 times to transition to Route 1 (y=35 on Route 1, which corresponds to y=0 in Pallet Town)
    for i in range(20):
        mgba.press_buttons(["Up"])
        time.sleep(0.15)
        pos = mgba.get_coordinates()
        if pos['y'] >= 30: # If y coordinate jumps to Route 1 (where south is y=35)
            print(f"Transitioned to Route 1! Position: {pos}")
            break

walk_to_route1()
