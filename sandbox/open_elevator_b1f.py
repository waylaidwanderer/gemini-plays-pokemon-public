import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B1F hidden warp test from:", pos)

if pos['x'] == 25 and pos['y'] == 15:
    # 1. Walk Up 4 steps to Row 11
    print("Walking Up to Row 11...")
    for _ in range(4):
        pos = move(["Up"])
        
    # 2. Walk Left 2 steps to Column 23 (Row 11)
    print("Walking Left to Column 23...")
    for _ in range(2):
        pos = move(["Left"])
        
    # 3. Walk Up 8 steps to Row 3 (at Column 23)
    print("Walking Up to Row 3...")
    for _ in range(8):
        pos = move(["Up"])
        
    # 4. Walk Right 1 step to (24, 3)
    pos = move(["Right"])
    
    # 5. Step Up onto (24, 2) to test hidden warp!
    print("Stepping onto (24, 2) warp...")
    pos = move(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Final position after warp attempt:", pos)

mgba.take_screenshot()
