import mgba
import time

def walk_to_2f():
    print("Navigating from 3F (10, 7) back to 2F via row 10...")
    # Current position: (10, 7) on 3F.
    
    # 1. Walk Down to (10, 10) (3 steps Down)
    for i in range(3):
        pos = mgba.get_coordinates()
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        print(f"Step Down {i+1}: {pos} -> {new_pos}")
        if new_pos == pos:
            print("Hit obstacle going Down!")
            break
            
    # 2. Walk Left to (7, 10) (3 steps Left)
    pos = mgba.get_coordinates()
    if pos['y'] == 10:
        for i in range(3):
            pos = mgba.get_coordinates()
            mgba.press_buttons(["Left"])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            print(f"Step Left {i+1}: {pos} -> {new_pos}")
            if new_pos == pos:
                print("Hit obstacle going Left!")
                break
                
    # 3. Step onto stairs warp to go to 2F
    pos = mgba.get_coordinates()
    if pos['x'] == 7 and pos['y'] == 10:
        print("At stairs warp! Stepping Down to trigger warp...")
        mgba.press_buttons(["Down"])
        time.sleep(1.2)
        print("Warp complete! New Position:", mgba.get_coordinates())
        
    mgba.take_screenshot()

walk_to_2f()
