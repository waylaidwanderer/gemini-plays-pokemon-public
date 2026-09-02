import mgba
import time

def walk_to_gym_corridor():
    print("Walking to Row 8 near Gym...")
    
    # 1. Walk Left to Column 19 on Row 28
    # Currently at (32, 28)
    for _ in range(13):
        mgba.press_buttons(["Left"])
        time.sleep(0.15)
        
    print(f"At Column 19: {mgba.get_coordinates()}")
    
    # 2. Walk UP to Row 5 on Column 19
    # (19, 28) -> (19, 5) is 23 steps UP
    for _ in range(23):
        mgba.press_buttons(["Up"])
        time.sleep(0.15)
        
    print(f"At Row 5: {mgba.get_coordinates()}")
    
    # 3. Walk Right to Column 27 on Row 5
    for _ in range(8):
        mgba.press_buttons(["Right"])
        time.sleep(0.15)
        
    print(f"At Column 27: {mgba.get_coordinates()}")
    
    # 4. Walk Down to Row 6, Left to Column 26, Down to Row 8
    mgba.press_buttons(["Down"])
    time.sleep(0.15)
    mgba.press_buttons(["Left"])
    time.sleep(0.15)
    mgba.press_buttons(["Down"])
    time.sleep(0.15)
    mgba.press_buttons(["Down"])
    time.sleep(0.15)
    
    pos = mgba.get_coordinates()
    print(f"Arrived at Row 8 Column 26: {pos}")
    
    # Take a screenshot to inspect
    sc = mgba.take_screenshot()
    print(f"Screenshot taken: {sc}")

walk_to_gym_corridor()
