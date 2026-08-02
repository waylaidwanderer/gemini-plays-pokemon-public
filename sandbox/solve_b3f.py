import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B3F navigation from:", pos)

if pos['x'] == 25 and pos['y'] == 6:
    # 1. Walk Down 1 step to Row 7
    pos = move(["Down"])
    
    # 2. Walk Left 23 steps to Column 2
    print("Walking Left to Column 2...")
    for _ in range(23):
        pos = move(["Left"])
        
    # 3. Walk Down 2 steps to (2, 9)
    print("Walking Down to (2, 9)...")
    pos = move(["Down"])
    pos = move(["Down"])
    
    pos = mgba.get_coordinates()
    print("Final position at start of maze:", pos)

mgba.take_screenshot()
