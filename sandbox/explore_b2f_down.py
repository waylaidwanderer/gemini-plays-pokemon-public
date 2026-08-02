import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B2F southern exploration from:", pos)

if pos['x'] == 25 and pos['y'] == 15:
    # 1. Walk Left to Column 21
    print("Walking Left to Column 21...")
    for _ in range(4):
        pos = move(["Left"])
        
    # 2. Walk Up to Row 14
    pos = move(["Up"])
    
    # 3. Walk Left to Column 19
    print("Walking Left to Column 19...")
    for _ in range(2):
        pos = move(["Left"])
        
    # 4. Walk Up 3 steps to Row 11
    print("Walking Up to Row 11...")
    for _ in range(3):
        pos = move(["Up"])
        
    # 5. Step Left onto (17, 11) LEFT spinner to slide to (2, 9)
    print("Stepping onto (17, 11) LEFT spinner...")
    pos = move(["Left"])
    pos = move(["Left"])
    time.sleep(4.0)
    pos = mgba.get_coordinates()
    print("Position on Left side:", pos)

# We should be at (2, 9) on B2F.
if pos['x'] == 2 and pos['y'] == 9:
    # 6. Navigate spinner maze to (15, 18)
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

# We should be at (15, 18).
if pos['x'] == 15 and pos['y'] == 18:
    # 7. Walk Left to Column 12 (via (13, 18) LEFT spinner) to land at (11, 20)
    print("Walking Left to Column 12 via spinner...")
    pos = move(["Left"])
    pos = move(["Left"]) # onto (13, 18) LEFT spinner
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print("Arrived at Row 20:", pos)

# We should be at (11, 20).
if pos['y'] == 20:
    # 8. Walk Right along Row 20 as far as possible to find the elevator!
    print("Walking Right along Row 20...")
    for i in range(15):
        old_pos = pos
        pos = move(["Right"])
        if pos == old_pos:
            print(f"Blocked going Right along Row 20 at: {pos}")
            # Try to walk Down/Up if blocked to see if we can find a way
            break

mgba.take_screenshot()
