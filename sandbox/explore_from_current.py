import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Current pos: {pos}")

if pos['x'] == 10 and pos['y'] == 12:
    # Test Left
    print("Testing Left...")
    pos = move(['Left'])
    if pos['x'] < 10:
        print("Left is walkable!")
        pos = move(['Right']) # Return
    else:
        print("Left is blocked")
        
    # Test Right
    print("Testing Right...")
    pos = move(['Right'])
    if pos['x'] > 10:
        print("Right is walkable!")
        pos = move(['Left']) # Return
    else:
        print("Right is blocked")
        
    # Test Up
    print("Testing Up...")
    pos = move(['Up'])
    if pos['y'] < 12:
        print("Up is walkable!")
        pos = move(['Down']) # Return
    else:
        print("Up is blocked")
        
    # Test Down
    print("Testing Down...")
    pos = move(['Down'])
    if pos['y'] > 12:
        print("Down is walkable!")
        pos = move(['Up']) # Return
    else:
        print("Down is blocked")

mgba.take_screenshot()
