import mgba
import time

def walk_left_on_row6():
    print("Walking LEFT along Row 6...")
    # Currently at (12, 6)
    while True:
        curr = mgba.get_coordinates()
        if curr is None:
            time.sleep(0.5)
            continue
        cx, cy = curr['x'], curr['y']
        if cx == 3:
            print("Reached Column 3 on Row 6!")
            break
            
        mgba.press_buttons(["Left"])
        time.sleep(0.45)
        
        after = mgba.get_coordinates()
        if after['x'] == cx and after['y'] == cy:
            print(f"Blocked walking LEFT at {curr}")
            break

walk_left_on_row6()
mgba.take_screenshot()
