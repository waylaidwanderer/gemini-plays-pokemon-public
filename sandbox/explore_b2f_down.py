import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B2F Row 19 test from (15, 18):", pos)

if pos['x'] == 15 and pos['y'] == 18:
    # 1. Slide to (11, 20) stopper via (13, 18) LEFT spinner
    print("Walking Left onto (13, 18) LEFT spinner...")
    pos = move(["Left"])
    pos = move(["Left"])
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print("Arrived at Row 20 stopper:", pos)

# We should be at (11, 20)
if pos['x'] == 11 and pos['y'] == 20:
    # 2. Walk Up 1 step to (11, 19)
    pos = move(["Up"])
    
    # 3. Walk Right along Row 19 as far as possible
    print("Walking Right along Row 19...")
    path = [pos]
    for i in range(15):
        old_pos = pos
        pos = move(["Right"])
        if pos == old_pos:
            print(f"Blocked going Right along Row 19 at: {pos}")
            break
        path.append(pos)
        
    print(f"Row 19 Path: {path}")

mgba.take_screenshot()
