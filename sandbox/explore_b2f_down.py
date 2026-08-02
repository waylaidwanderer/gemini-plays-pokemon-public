import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B2F maze navigation from (2, 9):", pos)

if pos['x'] == 2 and pos['y'] == 9:
    # 1. Walk to (3, 11)
    pos = move(["Right"])
    pos = move(["Down"])
    pos = move(["Down"])
    
    # 2. Step onto (4, 11) RIGHT spinner
    print("Stepping onto (4, 11) RIGHT spinner...")
    pos = move(["Right"])
    time.sleep(4.0)
    pos = mgba.get_coordinates()
    print("Position after slide 1:", pos)

# We should be at (8, 11) or (10, 11)
if pos['x'] in [8, 9, 10] and pos['y'] == 11:
    # Walk to (10, 14)
    dist = 10 - pos['x']
    if dist > 0:
        print(f"Walking Right {dist} steps...")
        for _ in range(dist):
            pos = move(["Right"])
            
    print("Walking Down to Row 14...")
    for _ in range(3):
        pos = move(["Down"])
        
    # Step onto (11, 14) DOWN spinner
    print("Stepping onto (11, 14) DOWN spinner...")
    pos = move(["Right"])
    time.sleep(4.0)
    pos = mgba.get_coordinates()
    print("Position after slide 2:", pos)

# We should be at (15, 18)
if pos['x'] == 15 and pos['y'] == 18:
    # Walk Left onto (13, 18) LEFT spinner
    print("Walking Left onto (13, 18) LEFT spinner...")
    pos = move(["Left"])
    pos = move(["Left"])
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print("Arrived at Row 20 stopper:", pos)

# We should be at (11, 20)
if pos['x'] == 11 and pos['y'] == 20:
    # Walk Right along Row 20 as far as possible
    print("Walking Right along Row 20...")
    for i in range(15):
        old_pos = pos
        pos = move(["Right"])
        if pos == old_pos:
            print(f"Blocked going Right along Row 20 at: {pos}")
            break

mgba.take_screenshot()
