import mgba
import time

def walk_left_to(target_x):
    pos = mgba.get_coordinates()
    print(f"Starting walk from {pos} to x={target_x}...")
    while pos['x'] > target_x:
        mgba.press_buttons(["Left"])
        time.sleep(0.35)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # try again with slightly longer wait
            time.sleep(0.5)
            mgba.press_buttons(["Left"])
            time.sleep(0.35)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print(f"Blocked at {pos}")
                break
        pos = new_pos
        print(f"Walked to {pos}")
    
    # Take screenshot at the end
    scr = mgba.take_screenshot()
    print(f"Final screenshot saved at {scr}")

walk_left_to(31)
