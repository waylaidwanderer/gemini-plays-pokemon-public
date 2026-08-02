import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B2F Row 19 exploration from:", pos)

if pos['x'] == 2 and pos['y'] == 9:
    # 1. Navigate maze to (15, 18)
    print("Navigating maze to (15, 18)...")
    pos = move(["Right"])
    pos = move(["Down"])
    pos = move(["Down"])
    print("Stepping onto (4, 11) RIGHT spinner...")
    pos = move(["Right"])
    time.sleep(4.0)
    
    pos = mgba.get_coordinates()
    print("After slide 1:", pos)
    
    # We are at (8, 11). Walk to (10, 14)
    pos = move(["Right"])
    pos = move(["Right"])
    pos = move(["Down"])
    pos = move(["Down"])
    pos = move(["Down"])
    
    # Step onto (11, 14) DOWN spinner to slide to (15, 18)
    print("Stepping onto (11, 14) DOWN spinner...")
    pos = move(["Right"])
    time.sleep(4.0)
    pos = mgba.get_coordinates()
    print("Arrived at:", pos)

# We should be at (15, 18)
if pos['x'] == 15 and pos['y'] == 18:
    # 2. Slide to (11, 20) stopper via (13, 18) LEFT spinner
    print("Walking Left onto (13, 18) LEFT spinner...")
    pos = move(["Left"])
    pos = move(["Left"])
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print("Arrived at Row 20 stopper:", pos)

# We should be at (11, 20)
if pos['x'] == 11 and pos['y'] == 20:
    # 3. Walk Up 1 step to (11, 19)
    pos = move(["Up"])
    
    # 4. Walk Right along Row 19 as far as possible
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
