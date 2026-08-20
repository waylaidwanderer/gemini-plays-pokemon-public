import mgba
import time

def explore_3f_east():
    print("Dismissing battle text and exploring 3F East...")
    # Currently at (7, 11) in 'Got away safely!' screen.
    
    # 1. Dismiss textbox
    mgba.press_buttons(["A"])
    time.sleep(0.6)
    
    # 2. Walk Right from (7, 11) to (12, 11) (5 steps Right)
    for i in range(5):
        pos = mgba.get_coordinates()
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        print(f"Step Right {i+1}: {pos} -> {new_pos}")
        if new_pos == pos:
            print("Hit obstacle going Right! Let's analyze.")
            break
            
    mgba.take_screenshot()

explore_3f_east()
