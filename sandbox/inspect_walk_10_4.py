import mgba
import time

def inspect_walk_from_10_4():
    print("Testing immediate step-by-step movement from (10, 4)...")
    
    # Current position is (10, 4) facing LEFT
    
    # 1. Try to walk Left 1 step
    mgba.press_buttons(["Left"])
    time.sleep(0.1)
    pos = mgba.get_coordinates()
    print(f"Position after Left: {pos}")
    
    # If we moved Left, walk back Right
    if pos['x'] == 9:
        mgba.press_buttons(["Right"])
        time.sleep(0.1)
        print("Walked back to (10, 4)")
        
    # 2. Try to walk Up 1 step
    mgba.press_buttons(["Up"])
    time.sleep(0.1)
    pos = mgba.get_coordinates()
    print(f"Position after Up: {pos}")
    
    # If we moved Up, walk back Down
    if pos['y'] == 3:
        mgba.press_buttons(["Down"])
        time.sleep(0.1)
        print("Walked back to (10, 4)")
        
    # 3. Try to walk Down 1 step
    mgba.press_buttons(["Down"])
    time.sleep(0.1)
    pos = mgba.get_coordinates()
    print(f"Position after Down: {pos}")
    
    # If we moved Down, walk back Up
    if pos['y'] == 5:
        mgba.press_buttons(["Up"])
        time.sleep(0.1)
        print("Walked back to (10, 4)")

inspect_walk_from_10_4()
