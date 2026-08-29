import mgba
import time

def walk_to_1f():
    current_pos = mgba.get_coordinates()
    print(f"Starting at: {current_pos}")
    
    # 1. Walk from (9, 9) to (7, 10) on 3F West to warp to 2F West
    # Path: Left 2 to (7, 9), Down to (7, 10)
    steps_3f = ["Left", "Left", "Down"]
    for s in steps_3f:
        mgba.press_buttons([s])
        time.sleep(0.3)
        
    pos_2f = mgba.get_coordinates()
    print(f"Arrived on 2F West: {pos_2f}")
    
    # 2. Walk on 2F West from landing (usually (7, 11)) to (5, 10) to warp to 1F West
    # Path from (7, 11): Left 2 to (5, 11), Up to (5, 10)
    # Wait, let's step-by-step walk left and up
    mgba.press_buttons(["Left"])
    time.sleep(0.3)
    mgba.press_buttons(["Left"])
    time.sleep(0.3)
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    
    pos_1f = mgba.get_coordinates()
    print(f"Arrived on 1F West: {pos_1f}")

walk_to_1f()
