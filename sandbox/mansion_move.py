import mgba
import time

def walk_to_3f_state_a():
    print("Dismissing textbox and walking to 3F stairs at (7, 10)...")
    # Current position: (2, 12) on 'Who wouldn't?' screen.
    
    # 1. Dismiss textbox
    mgba.press_buttons(["A"])
    time.sleep(0.6)
    
    # 2. Walk Right to (3, 12)
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # 3. Walk Up to (3, 11)
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    print("Position:", mgba.get_coordinates())
    
    # 4. Walk Right to (7, 11) (4 steps Right)
    for i in range(4):
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        print("Position:", mgba.get_coordinates())
        
    # 5. Walk Up to step onto stairs at (7, 10) and warp!
    print("Stepping onto 3F stairs...")
    mgba.press_buttons(["Up"])
    time.sleep(1.2)
    
    print("Warp complete! Position on 3F:", mgba.get_coordinates())
    mgba.take_screenshot()

walk_to_3f_state_a()
