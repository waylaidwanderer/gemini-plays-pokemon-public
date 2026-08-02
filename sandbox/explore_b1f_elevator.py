import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B1F elevator exploration from Game Corner:", pos)

if pos['x'] == 17 and pos['y'] == 5:
    # 1. Walk Up onto stairs at (17, 4) to B1F
    print("Stepping onto B1F stairs...")
    pos = move(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position on B1F:", pos)

# Now we should be on B1F. Spawning at (21, 3) or (21, 2)
if pos['x'] == 21:
    print("Successfully on B1F!")
    # 2. Walk Right to Column 25
    print("Walking Right to Column 25...")
    for _ in range(4):
        pos = move(["Right"])
        
    # 3. Walk Down Column 25 as much as possible to reach the elevator
    print("Walking Down Column 25...")
    for i in range(25):
        old_pos = pos
        pos = move(["Down"])
        if pos == old_pos:
            print(f"Blocked going Down Column 25 at: {pos}")
            # Try to walk Right to Column 28 if Column 25 is blocked
            if pos['x'] < 28:
                print("Trying to walk Right...")
                pos = move(["Right"])
            else:
                break

    # If we reached around Y = 24, let's check if we can walk Left to Column 24
    pos = mgba.get_coordinates()
    if pos['y'] == 24 and pos['x'] > 24:
        print("Walking Left to Column 24...")
        pos = move(["Left"])
        
    # 4. If we are at (24, 24) or (25, 24), stand facing UP and press A to open door
    pos = mgba.get_coordinates()
    if pos['x'] in [24, 25] and pos['y'] == 24:
        print(f"At elevator door ({pos['x']}, {pos['y']})! Facing UP and opening door...")
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Step UP into elevator
        print("Walking UP into elevator...")
        pos = move(["Up"])
        time.sleep(2.0)
        pos = mgba.get_coordinates()
        print("Final position inside elevator:", pos)

mgba.take_screenshot()
