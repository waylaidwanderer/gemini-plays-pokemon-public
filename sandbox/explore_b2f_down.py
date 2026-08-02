import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B1F elevator exploration from B2F (14, 15):", pos)

if pos['x'] == 14 and pos['y'] == 15:
    # 1. Walk to (16, 13) on B2F
    pos = move(["Right"])
    pos = move(["Right"])
    print("Stepping onto (16, 14) UP spinner...")
    pos = move(["Up"])
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print("Arrived at:", pos)

if pos['x'] == 16 and pos['y'] == 13:
    # 2. Walk to stairs at (27, 8) on B2F
    print("Walking Right to Column 27...")
    for _ in range(11):
        pos = move(["Right"])
        
    print("Walking Up to Row 8...")
    for _ in range(5):
        pos = move(["Up"])
        
    # Take stairs to B1F
    print("Taking stairs to B1F...")
    pos = move(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Spawning on B1F:", pos)

# We should be on B1F at (23, 2) (or (23, 3))
if pos['x'] == 23 and (pos['y'] == 2 or pos['y'] == 3):
    print("Successfully on B1F!")
    # 3. Walk to (28, 15) on B1F
    # If we are at (23, 2), walk Down to Row 8 (6 steps)
    dist_y = 8 - pos['y']
    print(f"Walking Down {dist_y} steps...")
    for _ in range(dist_y):
        pos = move(["Down"])
        
    # Walk Right to Column 28 (5 steps)
    print("Walking Right to Column 28...")
    for _ in range(5):
        pos = move(["Right"])
        
    # Walk Down to Row 15 (7 steps)
    print("Walking Down to Row 15...")
    for _ in range(7):
        pos = move(["Down"])
        
    # Walk Left to Column 25 (3 steps)
    print("Walking Left to Column 25...")
    for _ in range(3):
        pos = move(["Left"])
        
    # 4. Try walking Down Column 25 on B1F as far as possible!
    print("Testing walking Down Column 25 on B1F...")
    for i in range(10):
        old_pos = pos
        pos = move(["Down"])
        if pos == old_pos:
            print(f"Blocked going Down on B1F Column 25 at: {pos}")
            break
            
    # If we reached around Row 19, let's turn Left and open the elevator door!
    pos = mgba.get_coordinates()
    if pos['x'] == 25 and pos['y'] == 19:
        print("At (25, 19) on B1F! Facing Left and pressing A to open elevator...")
        mgba.press_buttons(["Left"])
        time.sleep(0.3)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Step Left into the elevator
        print("Stepping Left into the elevator...")
        pos = move(["Left"])
        time.sleep(2.0)
        print("Final position inside elevator:", mgba.get_coordinates())

mgba.take_screenshot()
