import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B3F downward exploration from:", pos)

if pos['x'] == 9 and pos['y'] == 7:
    # Walk Down 2 steps to (9, 9)
    pos = move(["Down"])
    pos = move(["Down"])
    
mgba.take_screenshot()
