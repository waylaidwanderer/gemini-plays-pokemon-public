import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting explore_left_room_right_exit from {pos}")

if pos['x'] == 2 and pos['y'] == 7:
    # Walk Right 3 steps to (5, 7)
    for _ in range(3):
        pos = move(['Right'])
        
    # Walk Down 2 steps to (5, 9)
    for _ in range(2):
        pos = move(['Down'])
        
    # Walk Right 2 steps to (7, 9)
    for _ in range(2):
        pos = move(['Right'])
        
    # Let's see if we can walk Right further
    print("Testing if we can go further Right on Row 9...")
    test_pos = move(['Right'])
    if test_pos['x'] > 7:
        print("We can walk further Right! Labeled coordinates:", test_pos)
    else:
        print("Right is blocked at:", test_pos)
        
    # Let's test Up and Down from (7, 9)
    pos = mgba.get_coordinates()
    if pos['x'] == 7 and pos['y'] == 9:
        print("Testing Up from (7, 9)...")
        test_up = move(['Up'])
        if test_up['y'] == 8:
            print("Up is walkable to (7, 8)!")
            move(['Down']) # Return
        else:
            print("Up is blocked")
            
        print("Testing Down from (7, 9)...")
        test_down = move(['Down'])
        if test_down['y'] == 10:
            print("Down is walkable to (7, 10)!")
            move(['Up']) # Return
        else:
            print("Down is blocked")

mgba.take_screenshot()
