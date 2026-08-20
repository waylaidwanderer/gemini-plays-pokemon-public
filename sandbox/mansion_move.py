import mgba
import time

def walk_to_2f_from_3f():
    print("Walking from (22, 7) on 3F back to the 2F stairs at (7, 10)...")
    # Current position: (22, 7) on 3F.
    
    # 1. Walk Left to column 7 (15 steps Left)
    for i in range(15):
        pos = mgba.get_coordinates()
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        print(f"Step Left {i+1}: {pos} -> {new_pos}")
        if new_pos == pos:
            # If we get into a battle, we handle it or stop
            print("Hit obstacle or battle going Left!")
            break
            
    # 2. Walk Down to (7, 10) (3 steps Down)
    pos = mgba.get_coordinates()
    if pos['x'] == 7:
        for i in range(3):
            pos = mgba.get_coordinates()
            mgba.press_buttons(["Down"])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            print(f"Step Down {i+1}: {pos} -> {new_pos}")
            if new_pos == pos:
                print("Hit obstacle going Down!")
                break
                
    # 3. Step onto stairs warp to go to 2F
    # Note: On 3F, stepping onto the stairs warp at (7, 10) will trigger the warp.
    # If we are at (7, 10) on 3F and face Down/Up or try to move, it warps us to 2F.
    # Let's do a step Up or Down to trigger the warp if we are at (7, 10).
    pos = mgba.get_coordinates()
    if pos['x'] == 7 and pos['y'] == 10:
        print("At stairs warp! Stepping Down to trigger warp...")
        mgba.press_buttons(["Down"])
        time.sleep(1.2)
        print("Warp complete! New Position:", mgba.get_coordinates())
        
    mgba.take_screenshot()

walk_to_2f_from_3f()
