import mgba
import time

def test_row14_to_gatehouse():
    print("Testing Row 14 walk LEFT...")
    # Currently at (20, 14)
    while True:
        curr = mgba.get_coordinates()
        if curr is None:
            time.sleep(0.5)
            continue
        cx, cy = curr['x'], curr['y']
        if cx == 1:
            print("SUCCESS! Reached Column 1 on Row 14!")
            break
            
        mgba.press_buttons(["Left"])
        time.sleep(0.45)
        
        after = mgba.get_coordinates()
        if after['x'] == cx and after['y'] == cy:
            print(f"Blocked walking LEFT at {curr}")
            break

test_row14_to_gatehouse()
mgba.take_screenshot()
