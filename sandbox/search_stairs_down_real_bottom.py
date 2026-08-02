import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting bottom area search from {pos}")

if pos['x'] == 1 and pos['y'] == 9:
    # 1. Walk to (3, 13)
    pos = move(['Right'])  # (2, 9)
    pos = move(['Right'])  # (3, 9)
    pos = move(['Down'])   # (3, 10)
    pos = move(['Down'])   # (3, 11)
    pos = move(['Down'])   # (3, 12)
    pos = move(['Down'])   # (3, 13)
    
    # List of steps to test all bottom-left walkable tiles
    steps_to_test = [
        'Left',   # (2, 13)
        'Left',   # (1, 13)
        'Up',     # (1, 12)
        'Up',     # (1, 11)
        'Down',   # (1, 12)
        'Down',   # (1, 13)
        'Right',  # (2, 13)
        'Right',  # (3, 13)
        'Right',  # (4, 13)
    ]
    
    for step in steps_to_test:
        old_pos = mgba.get_coordinates()
        pos = move([step])
        time.sleep(0.2)
        new_pos = mgba.get_coordinates()
        if abs(new_pos['x'] - old_pos['x']) > 5 or abs(new_pos['y'] - old_pos['y']) > 5:
            print(f"MAP TRANSITION DETECTED! Spawned at: {new_pos}")
            break

mgba.take_screenshot()
