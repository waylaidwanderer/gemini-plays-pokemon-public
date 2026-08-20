import mgba
import time

def find_3f_entrance():
    print("Finding the entrance to the 3F eastern room...")
    # Currently at (13, 12).
    
    # 1. Walk to (12, 7)
    mgba.press_buttons(["Left", "sleep 300"])
    for i in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
    print("At:", mgba.get_coordinates())
    
    # We will test columns 14, 15, 16, 17 on row 7 to see if we can walk Down.
    columns_to_test = [14, 15, 16, 17]
    
    for col in columns_to_test:
        pos = mgba.get_coordinates()
        # Walk to col
        while pos['x'] < col:
            mgba.press_buttons(["Right"])
            time.sleep(0.4)
            pos = mgba.get_coordinates()
        while pos['x'] > col:
            mgba.press_buttons(["Left"])
            time.sleep(0.4)
            pos = mgba.get_coordinates()
            
        print(f"Testing column {col}...")
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        if new_pos['y'] > 7:
            print(f"SUCCESS! Column {col} is open to the south!")
            mgba.take_screenshot()
            return
            
    print("All tested columns are blocked.")
    mgba.take_screenshot()

find_3f_entrance()
