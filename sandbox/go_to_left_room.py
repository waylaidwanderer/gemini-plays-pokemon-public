import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting go_to_left_room from {pos}")

if pos['x'] == 16 and pos['y'] == 13:
    # Walk Right 3 steps to (19, 13)
    for _ in range(3):
        pos = move(['Right'])
    # Walk Up 2 steps to (19, 11)
    for _ in range(2):
        pos = move(['Up'])
    # Walk Left 2 steps to step onto (17, 11) LEFT spinner
    pos = move(['Left'])
    print("Stepping onto LEFT spinner...")
    pos = move(['Left'])
    
    print("Waiting for slide...")
    time.sleep(5.0)
    print(f"Position after slide: {mgba.get_coordinates()}")

mgba.take_screenshot()
