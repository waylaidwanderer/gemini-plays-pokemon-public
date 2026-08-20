import mgba
import time

def enter_eastern_room():
    print("Dismissing battle and testing columns 16 and 17 to enter the eastern room...")
    # Currently at (16, 7) on the 'Got away safely!' screen.
    
    # 1. Dismiss battle screen
    mgba.press_buttons(["A"])
    time.sleep(0.6)
    
    pos = mgba.get_coordinates()
    print("At:", pos)
    
    # 2. Try to walk Down on column 16
    if pos['x'] == 16 and pos['y'] == 7:
        print("Testing column 16 going Down...")
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        pos2 = mgba.get_coordinates()
        print("Position after Down at 16:", pos2)
        if pos2['y'] == 8:
            print("SUCCESS! Column 16 is the entrance!")
            mgba.take_screenshot()
            return
            
    # 3. If column 16 is blocked, walk Right to (17, 7)
    pos = mgba.get_coordinates()
    if pos['x'] == 16 and pos['y'] == 7:
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("At:", pos)
        
    # 4. Try to walk Down on column 17
    if pos['x'] == 17 and pos['y'] == 7:
        print("Testing column 17 going Down...")
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        pos2 = mgba.get_coordinates()
        print("Position after Down at 17:", pos2)
        if pos2['y'] == 8:
            print("SUCCESS! Column 17 is the entrance!")
            mgba.take_screenshot()
            return
            
    print("Both column 16 and 17 are blocked.")
    mgba.take_screenshot()

enter_eastern_room()
