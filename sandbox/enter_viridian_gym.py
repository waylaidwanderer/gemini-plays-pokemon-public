import mgba
import time

def walk_back():
    print("Walking from (32, 10) back to (29, 8) via Column 18...")
    
    # Walk left to (18, 10)
    for _ in range(14):
        mgba.press_buttons(["Left"])
        time.sleep(0.1)
        
    print(f"At: {mgba.get_coordinates()}")
    
    # Walk UP to (18, 6)
    for _ in range(4):
        mgba.press_buttons(["Up"])
        time.sleep(0.1)
        
    print(f"At: {mgba.get_coordinates()}")
    
    # Walk Right to (26, 6)
    for _ in range(8):
        mgba.press_buttons(["Right"])
        time.sleep(0.1)
        
    print(f"At: {mgba.get_coordinates()}")
    
    # Walk Down to (26, 8)
    for _ in range(2):
        mgba.press_buttons(["Down"])
        time.sleep(0.1)
        
    print(f"At: {mgba.get_coordinates()}")
    
    # Walk Right to (29, 8)
    for _ in range(3):
        mgba.press_buttons(["Right"])
        time.sleep(0.1)
        
    pos = mgba.get_coordinates()
    print(f"Arrived at: {pos}")
    
    # Try to walk Right into (30, 8)
    mgba.press_buttons(["Right"])
    time.sleep(0.2)
    pos2 = mgba.get_coordinates()
    print(f"After trying to walk Right: {pos2}")
    
    # Talk to the NPC
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    print("Finished.")

walk_back()
